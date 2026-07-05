#!/usr/bin/env python3
"""
Enrich articles in issues/*.json with affiliation, topics, and technologies,
and migrate legacy author_title values that are actually affiliations.

Reads the topic taxonomy from data/taxonomy.json (the same file
docs/src/topics.mjs reads, so both sides can't drift) and a controlled
technology vocabulary from data/technologies.json.

Usage:
    uv run python src/extract_metadata.py               # only articles missing topics/technologies/affiliation
    uv run python src/extract_metadata.py --force        # redo all
    uv run python src/extract_metadata.py --issue 2001_07
    uv run python src/extract_metadata.py --dry-run
    uv run python src/extract_metadata.py --model claude-haiku-4.5
"""

import argparse
import json
import re
import time

import llm

from pipeline_common import DATA_DIR, ISSUES_DIR

DEFAULT_MODEL = "anthropic/claude-haiku-4-5"

TAXONOMY_PATH = DATA_DIR / "taxonomy.json"
TECHNOLOGIES_PATH = DATA_DIR / "technologies.json"

DEFAULT_TECHNOLOGIES = [
    "SPSS", "SAS", "FoxPro", "Paradox", "dBase", "Access", "Excel",
    "Lotus 1-2-3", "Quattro Pro", "XDB", "ArcView", "ArcInfo", "MapInfo",
    "Atlas GIS", "SQL", "Visual Basic", "Perl", "9-track tape", "CD-ROM",
    "mainframe", "Nexis", "Internet", "World Wide Web", "FTP", "gopher",
    "modem/BBS",
]

TECHNOLOGY_ALIASES = {
    "dbase iv": "dBase", "dbase": "dBase", "msaccess": "Access", "ms access": "Access",
    "excel spreadsheet": "Excel", "spss/pc": "SPSS", "the internet": "Internet",
    "world wide web": "World Wide Web", "www": "World Wide Web", "the web": "World Wide Web",
    "bbs": "modem/BBS", "bulletin board": "modem/BBS", "modem": "modem/BBS",
}


def load_taxonomy():
    return json.loads(TAXONOMY_PATH.read_text())


def load_technologies():
    if TECHNOLOGIES_PATH.exists():
        return json.loads(TECHNOLOGIES_PATH.read_text())
    DATA_DIR.mkdir(exist_ok=True)
    TECHNOLOGIES_PATH.write_text(json.dumps(DEFAULT_TECHNOLOGIES, indent=2) + "\n")
    return DEFAULT_TECHNOLOGIES


def build_system_prompt(taxonomy, technologies):
    topic_lines = "\n".join(
        f"- {name}: {', '.join(keywords[:8])}" for name, keywords in taxonomy.items()
    )
    tech_list = ", ".join(technologies)
    return f"""\
You are tagging one article from a 1990s-2000s journalism newsletter about \
computer-assisted reporting. Given the headline, byline, and article text, \
return a JSON object with:

- author_name: the byline name, cleaned up (empty string if none)
- author_title: the author's JOB TITLE only, e.g. "database editor" \
(NOT a publication or organization name; empty string if unknown or if the \
byline only gives a publication)
- affiliation: the author's PUBLICATION or ORGANIZATION only, e.g. \
"The Oregonian" or "IRE and NICAR" (empty string if unknown)
- topics: an array of 1-3 topics from this exact list, most relevant first:
{topic_lines}
- technologies: an array of software, hardware, or data formats explicitly \
mentioned in the article. Prefer these canonical names when applicable: \
{tech_list}. Add other technologies verbatim (normalized casing) if \
mentioned but not in that list. Empty array if none mentioned.

Return JSON only, matching the schema."""


def build_schema(taxonomy):
    return {
        "type": "object",
        "properties": {
            "author_name": {"type": "string"},
            "author_title": {"type": "string"},
            "affiliation": {"type": "string"},
            "topics": {
                "type": "array",
                "items": {"type": "string", "enum": list(taxonomy.keys()) + ["Other"]},
                "minItems": 1,
                "maxItems": 3,
            },
            "technologies": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["author_name", "author_title", "affiliation", "topics", "technologies"],
    }


def needs_metadata(article):
    return not article.get("topics") or "technologies" not in article or not article.get("affiliation")


def normalize_technology(tech):
    canonical = TECHNOLOGY_ALIASES.get(tech.strip().lower())
    return canonical or tech.strip()


def enrich_article(model, schema, system_prompt, article):
    prompt = (
        f"Headline: {article.get('headline', '')}\n"
        f"Byline: {article.get('author_name', '')} "
        f"({article.get('author_title', '')})\n\n"
        f"{article.get('full_text', '')[:4000]}"
    )
    response = model.prompt(prompt, system=system_prompt, schema=schema)
    result = json.loads(response.text())
    seen = set()
    technologies = []
    for tech in result.get("technologies", []):
        canonical = normalize_technology(tech)
        key = canonical.lower()
        if key not in seen:
            seen.add(key)
            technologies.append(canonical)
    result["technologies"] = technologies
    return result


def main():
    parser = argparse.ArgumentParser(description="Enrich articles with affiliation/topics/technologies")
    parser.add_argument("--force", action="store_true", help="Re-run for every article")
    parser.add_argument("--issue", help="Only process one issue stem, e.g. 2001_07")
    parser.add_argument("--dry-run", action="store_true", help="Preview articles needing enrichment")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"LLM model to use (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    taxonomy = load_taxonomy()
    technologies_vocab = load_technologies()
    system_prompt = build_system_prompt(taxonomy, technologies_vocab)
    schema = build_schema(taxonomy)

    files = [ISSUES_DIR / f"{args.issue}.json"] if args.issue else sorted(ISSUES_DIR.glob("*.json"))
    files = [f for f in files if f.stem != "cleaned_stories" and f.exists()]

    to_process = []
    total = 0
    for f in files:
        data = json.loads(f.read_text())
        for i, article in enumerate(data.get("articles", [])):
            total += 1
            if args.force or needs_metadata(article):
                to_process.append((f, i, article))

    print(f"Total articles: {total}, needing enrichment: {len(to_process)}")

    if args.dry_run:
        for f, i, a in to_process:
            print(f"  {f.name} [{i}] {a.get('headline', '')[:60]}")
        return

    if not to_process:
        print("Nothing to do.")
        return

    model = llm.get_model(args.model)

    by_file = {}
    for f, i, a in to_process:
        by_file.setdefault(f, []).append((i, a))

    processed = 0
    errors = 0

    for filepath, articles in sorted(by_file.items()):
        data = json.loads(filepath.read_text())
        modified = False

        for idx, article in articles:
            processed += 1
            label = article.get("headline", "")[:50]
            print(f"[{processed}/{len(to_process)}] {filepath.name}[{idx}] {label}...", end=" ", flush=True)
            try:
                result = enrich_article(model, schema, system_prompt, article)
            except Exception as e:
                print(f"ERROR: {e}")
                errors += 1
                continue

            a = data["articles"][idx]
            a["affiliation"] = result.get("affiliation") or a.get("affiliation", "")
            # Only overwrite author_title if the old value looks like it was
            # actually an affiliation (the pre-v2 schema conflated the two).
            old_title = a.get("author_title", "")
            if result.get("author_title"):
                a["author_title"] = result["author_title"]
            elif old_title and old_title.strip().lower() == a["affiliation"].strip().lower():
                a["author_title"] = ""
            a["topics"] = result.get("topics", [])
            a["technologies"] = result.get("technologies", [])
            modified = True
            print("OK")

            if processed < len(to_process):
                time.sleep(0.3)

        if modified:
            filepath.write_text(json.dumps(data, indent=2) + "\n")
            print(f"  -> Updated {filepath.name}")

    print(f"\nDone. Processed {processed} articles ({errors} errors).")


if __name__ == "__main__":
    main()
