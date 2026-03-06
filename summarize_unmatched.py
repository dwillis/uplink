"""
Identify articles in articles/original/ that have no matched summary in data/,
generate summaries + keywords via the llm library (Claude), and merge results
directly into the corresponding data/*.json files.

Usage:
    uv run python summarize_unmatched.py [--dry-run] [--model MODEL]

Idempotent: skips articles whose matchKey already exists in data files.
"""

import argparse
import json
import re
import time
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
ORIG_DIR = REPO_ROOT / "articles" / "original"
DATA_DIR = REPO_ROOT / "data"

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


def normalize_articles(data):
    if isinstance(data, list):
        return data
    for key in ARTICLE_ARRAY_KEYS:
        if key in data and isinstance(data[key], list):
            return data[key]
    return [data]


def detect_wrapper_key(data):
    """Return the array wrapper key if the data uses one, else None."""
    if isinstance(data, list):
        return "__list__"
    for key in ARTICLE_ARRAY_KEYS:
        if key in data and isinstance(data[key], list):
            return key
    return None


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
                "author_name": a.get("author_name") or "",
                "author_title": a.get("author_title") or "",
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
    text = article["full_text"][:3000]
    response = model.prompt(text, system=SYSTEM_PROMPT)
    raw = response.text().strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = re.sub(r"^```\w*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def merge_into_data_file(filepath, new_entries):
    """Add new_entries to an existing (or new) data JSON file."""
    if filepath.exists():
        raw_data = json.loads(filepath.read_text())
        wrapper_key = detect_wrapper_key(raw_data)

        if wrapper_key == "__list__":
            # Top-level list
            raw_data.extend(new_entries)
        elif wrapper_key:
            # Object with array key like "stories" or "articles"
            raw_data[wrapper_key].extend(new_entries)
        else:
            # Single object — convert to "stories" array
            raw_data = {"stories": [raw_data] + new_entries}
    else:
        # New file
        if len(new_entries) == 1:
            raw_data = new_entries[0]
        else:
            raw_data = {"stories": new_entries}

    filepath.write_text(json.dumps(raw_data, indent=4) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Generate summaries for unmatched articles and merge into data files")
    parser.add_argument("--dry-run", action="store_true", help="Just show unmatched articles, don't call LLM")
    parser.add_argument("--model", default="anthropic/claude-3-5-haiku-latest", help="LLM model to use")
    args = parser.parse_args()

    unmatched, total, matched_count = find_unmatched()
    print(f"Total articles: {total}, matched: {matched_count}, unmatched: {len(unmatched)}")

    if args.dry_run:
        for a in unmatched:
            print(f"  {a['year']} {a['month']:20s} {a['headline'][:60]}")
        return

    if not unmatched:
        print("Nothing to do.")
        return

    import llm
    model = llm.get_model(args.model)

    # Group unmatched articles by source file
    by_file = defaultdict(list)
    for a in unmatched:
        by_file[a["source_file"]].append(a)

    processed = 0
    errors = 0
    total_to_process = len(unmatched)

    for filename, articles in sorted(by_file.items()):
        new_entries = []
        for article in articles:
            processed += 1
            label = f"{article['year']} {article['month']} - {article['headline'][:50]}"
            print(f"[{processed}/{total_to_process}] {label}...", end=" ", flush=True)
            try:
                result = generate_summary(model, article)
                entry = {
                    "year": article["year"],
                    "month": article["month"],
                    "headline": article["headline"],
                    "author_name": article["author_name"] if article["author_name"] != "null" else "",
                    "author_title": article["author_title"] if article["author_title"] != "null" else "",
                    "summary": result.get("summary", ""),
                    "keywords": result.get("keywords", [])[:3],
                }
                new_entries.append(entry)
                print("OK")
            except Exception as e:
                print(f"ERROR: {e}")
                errors += 1
                continue

            # Small delay to avoid rate limits
            if processed < total_to_process:
                time.sleep(0.5)

        # Merge all new entries for this file at once
        if new_entries:
            data_path = DATA_DIR / filename
            merge_into_data_file(data_path, new_entries)
            print(f"  -> Wrote {len(new_entries)} entries to {data_path.name}")

    print(f"\nDone. Processed {processed} articles ({errors} errors).")


if __name__ == "__main__":
    main()
