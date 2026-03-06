"""
Identify articles in articles/original/ that have no matched summary in data/,
then generate summaries + keywords for each using the llm library (Claude).

Usage:
    uv run python summarize_unmatched.py [--dry-run] [--model MODEL]

Writes results to data/supplements.json (slug-keyed).
Existing entries in supplements.json are preserved (idempotent re-runs).
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from slugify import slugify

REPO_ROOT = Path(__file__).resolve().parent
ORIG_DIR = REPO_ROOT / "articles" / "original"
DATA_DIR = REPO_ROOT / "data"
SUPPLEMENTS_PATH = DATA_DIR / "supplements.json"

MONTH_NAMES = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]

ARTICLE_ARRAY_KEYS = ["articles", "stories", "news_stories", "newsletter", "content", "data"]

SYSTEM_PROMPT = (
    "Given the full text of a journalism newsletter article, return a JSON object "
    "with two keys: \"summary\" (a 1-2 sentence description of the article) and "
    "\"keywords\" (an array of exactly 3 single words). No other text."
)


def normalize_month(month):
    s = str(month).lower().strip()
    try:
        num = int(s)
        if 1 <= num <= 12:
            return MONTH_NAMES[num - 1]
    except ValueError:
        pass
    m = re.match(r"^([a-z]+)", s)
    return m.group(1) if m else s


def match_key(year, month, headline):
    return f"{year}|{normalize_month(month)}|{headline.lower().strip()}"


def make_slug(year, month, headline):
    return slugify(f"{year}-{month}-{headline}")


def normalize_articles(data):
    if isinstance(data, list):
        return data
    for key in ARTICLE_ARRAY_KEYS:
        if key in data and isinstance(data[key], list):
            return data[key]
    return [data]


def load_original_articles():
    """Load all articles from articles/original/*.json, grouped by file."""
    by_file = {}
    all_articles = []
    for f in sorted(ORIG_DIR.glob("*.json")):
        raw = f.read_text().strip()
        if not raw:
            continue
        data = json.loads(raw)
        articles = normalize_articles(data)
        file_articles = []
        for a in articles:
            if not a.get("headline") or not a.get("full_text"):
                continue
            article = {
                "year": int(str(a["year"]).split("/")[0]),
                "month": a["month"],
                "headline": a["headline"],
                "full_text": a["full_text"],
                "source_file": f.name,
            }
            file_articles.append(article)
            all_articles.append(article)
        if file_articles:
            by_file[f.name] = file_articles
    return by_file, all_articles


def load_summaries():
    """Load all summaries from data/*.json, grouped by file and as a match-key map."""
    summary_map = {}
    by_file = {}
    for f in sorted(DATA_DIR.glob("*.json")):
        if f.name == "supplements.json":
            continue
        raw = f.read_text().strip()
        if not raw:
            continue
        data = json.loads(raw)
        articles = normalize_articles(data)
        file_summaries = []
        for a in articles:
            if not a.get("headline"):
                continue
            key = match_key(a.get("year", 0), a.get("month", ""), a["headline"])
            obj = {"headline": a["headline"], "summary": a.get("summary"), "keywords": a.get("keywords"), "matched": False}
            summary_map[key] = obj
            file_summaries.append(obj)
        if file_summaries:
            by_file[f.name] = file_summaries
    return summary_map, by_file


def find_unmatched():
    """Replicate consolidate.mjs two-pass matching, return list of unmatched articles."""
    by_file, all_articles = load_original_articles()
    summary_map, summary_by_file = load_summaries()

    matched = set()

    # Pass 1: exact headline match
    for i, article in enumerate(all_articles):
        key = match_key(article["year"], article["month"], article["headline"])
        s = summary_map.get(key)
        if s and not s["matched"]:
            matched.add(i)
            s["matched"] = True

    # Pass 2: positional match within same file
    for filename, file_articles in by_file.items():
        file_sums = summary_by_file.get(filename, [])
        unmatched_articles = [(i, a) for i, a in enumerate(all_articles) if a["source_file"] == filename and i not in matched]
        # Need indices within file_articles that are unmatched
        unmatched_arts_in_file = [a for a in file_articles if all_articles.index(a) not in matched]
        unmatched_sums = [s for s in file_sums if not s["matched"]]
        limit = min(len(unmatched_arts_in_file), len(unmatched_sums))
        for j in range(limit):
            idx = all_articles.index(unmatched_arts_in_file[j])
            matched.add(idx)
            unmatched_sums[j]["matched"] = True

    unmatched = [a for i, a in enumerate(all_articles) if i not in matched]
    return unmatched, len(all_articles), len(matched)


def generate_summary(model, article):
    """Call LLM to generate summary + keywords for one article."""
    # Truncate very long texts to keep costs down
    text = article["full_text"][:3000]
    response = model.prompt(text, system=SYSTEM_PROMPT)
    raw = response.text().strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = re.sub(r"^```\w*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description="Generate summaries for unmatched articles")
    parser.add_argument("--dry-run", action="store_true", help="Just show unmatched articles, don't call LLM")
    parser.add_argument("--model", default="anthropic/claude-3-5-haiku-latest", help="LLM model to use")
    args = parser.parse_args()

    unmatched, total, matched_count = find_unmatched()
    print(f"Total articles: {total}, matched: {matched_count}, unmatched: {len(unmatched)}")

    if args.dry_run:
        for a in unmatched:
            print(f"  {a['year']} {a['month']:20s} {a['headline'][:60]}")
        return

    # Load existing supplements
    existing = {}
    if SUPPLEMENTS_PATH.exists():
        existing = json.loads(SUPPLEMENTS_PATH.read_text())

    import llm
    model = llm.get_model(args.model)

    to_process = []
    for a in unmatched:
        slug = make_slug(a["year"], a["month"], a["headline"])
        if slug in existing:
            continue
        to_process.append((slug, a))

    print(f"Already in supplements: {len(unmatched) - len(to_process)}, to process: {len(to_process)}")

    for i, (slug, article) in enumerate(to_process):
        print(f"[{i+1}/{len(to_process)}] {slug[:70]}...", end=" ", flush=True)
        try:
            result = generate_summary(model, article)
            existing[slug] = {
                "summary": result.get("summary", ""),
                "keywords": result.get("keywords", [])[:3],
            }
            print("OK")
        except Exception as e:
            print(f"ERROR: {e}")
            continue

        # Write after each successful call (crash-safe)
        SUPPLEMENTS_PATH.write_text(json.dumps(existing, indent=2) + "\n")

        # Small delay to avoid rate limits
        if i < len(to_process) - 1:
            time.sleep(0.5)

    print(f"\nDone. {len(existing)} total entries in {SUPPLEMENTS_PATH}")


if __name__ == "__main__":
    main()
