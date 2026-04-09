#!/usr/bin/env python3
"""
One-time migration: merge articles/original/ + data/ into issues/.

Each issues/*.json file gets a normalized schema:
{
    "year": 1990,
    "month": "October",
    "articles": [
        {
            "headline": "...",
            "author_name": "...",
            "author_title": "...",
            "full_text": "...",
            "summary": "...",
            "keywords": ["...", "...", "..."]
        }
    ]
}

Uses the same two-pass matching logic as consolidate.mjs:
  Pass 1: exact headline match (year|month|headline key)
  Pass 2: positional match within same file for leftovers

Usage:
    uv run python src/migrate.py              # run migration
    uv run python src/migrate.py --dry-run    # preview only
"""

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ORIG_DIR = REPO_ROOT / "articles" / "original"
DATA_DIR = REPO_ROOT / "data"
ISSUES_DIR = REPO_ROOT / "issues"

ARTICLE_ARRAY_KEYS = ["articles", "stories", "news_stories", "newsletter", "content", "data"]

MONTH_NAMES = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]


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
    if isinstance(data, dict) and "headline" in data:
        return [data]
    return []


def extract_summary(full_text):
    """Extract a readable summary from full text (mirrors consolidate.mjs logic)."""
    text = re.sub(r"\s+", " ", full_text).strip()

    # Skip past short leading fragments that look like headers/bylines
    first_period = text.find(".")
    if 0 < first_period < 40:
        rest = text[first_period + 1:].strip()
        if len(rest) > 100:
            text = rest

    sentences = re.findall(r"[^.!?]*[.!?]+", text)
    if not sentences:
        if len(text) <= 250:
            return text
        cut = text.rfind(" ", 0, 250)
        return text[:cut if cut > 100 else 250] + "..."

    summary = ""
    for sentence in sentences:
        trimmed = sentence.strip()
        if not trimmed:
            continue
        if len(summary) + len(trimmed) > 300 and len(summary) > 80:
            break
        summary += (" " if summary else "") + trimmed
        if len(summary) >= 150:
            break

    return summary or sentences[0].strip()


def load_original_articles():
    """Load full-text articles from articles/original/, grouped by file."""
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
            year_raw = str(a.get("year", 0))
            try:
                year = int(year_raw.split("/")[0])
            except (ValueError, IndexError):
                year = 0
            article = {
                "year": year,
                "month": a.get("month", ""),
                "headline": a["headline"],
                "author_name": a.get("author_name") or "",
                "author_title": a.get("author_title") or "",
                "full_text": a["full_text"],
                "source_file": f.name,
            }
            # Clean up "null" strings
            if article["author_name"] == "null":
                article["author_name"] = ""
            if article["author_title"] == "null":
                article["author_title"] = ""
            file_articles.append(article)
            all_articles.append(article)
        if file_articles:
            by_file[f.name] = file_articles
    return by_file, all_articles


def load_summaries():
    """Load summaries from data/, as a match-key map and grouped by file."""
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
            obj = {
                "headline": a["headline"],
                "summary": a.get("summary"),
                "keywords": a.get("keywords"),
                "matched": False,
            }
            summary_map[key] = obj
            file_summaries.append(obj)
        if file_summaries:
            by_file[f.name] = file_summaries
    return summary_map, by_file


def run_migration(dry_run=False):
    by_file, all_articles = load_original_articles()
    summary_map, summary_by_file = load_summaries()

    # Two-pass matching (same as consolidate.mjs)
    article_summaries = {}  # id(article) -> summary obj
    matched_exact = 0
    matched_positional = 0

    # Pass 1: exact headline match
    for article in all_articles:
        key = match_key(article["year"], article["month"], article["headline"])
        s = summary_map.get(key)
        if s and not s["matched"]:
            article_summaries[id(article)] = s
            s["matched"] = True
            matched_exact += 1

    # Pass 2: positional match within same file
    for filename, file_articles in by_file.items():
        file_sums = summary_by_file.get(filename, [])
        unmatched_arts = [a for a in file_articles if id(a) not in article_summaries]
        unmatched_sums = [s for s in file_sums if not s["matched"]]
        limit = min(len(unmatched_arts), len(unmatched_sums))
        for j in range(limit):
            article_summaries[id(unmatched_arts[j])] = unmatched_sums[j]
            unmatched_sums[j]["matched"] = True
            matched_positional += 1

    unmatched_count = len(all_articles) - len(article_summaries)
    print(f"Articles: {len(all_articles)} total")
    print(f"Matched: {matched_exact} exact + {matched_positional} positional = {matched_exact + matched_positional}")
    print(f"Unmatched (will get auto-summary): {unmatched_count}")
    print()

    # Build issues grouped by source file
    if not dry_run:
        ISSUES_DIR.mkdir(exist_ok=True)

    files_written = 0
    total_articles_written = 0
    articles_with_summary = 0
    articles_auto_summary = 0

    for filename, file_articles in sorted(by_file.items()):
        # Determine issue-level year and month from filename (e.g., 1990_10.json)
        stem = Path(filename).stem
        parts = stem.split("_")
        issue_year = int(parts[0]) if len(parts) >= 1 else 0
        issue_month = file_articles[0]["month"] if file_articles else ""

        issue_articles = []
        for article in file_articles:
            summary_obj = article_summaries.get(id(article))
            if summary_obj and summary_obj.get("summary"):
                summary = summary_obj["summary"]
                keywords = summary_obj.get("keywords") or []
                articles_with_summary += 1
            else:
                summary = extract_summary(article["full_text"])
                keywords = []
                articles_auto_summary += 1

            issue_articles.append({
                "headline": article["headline"],
                "author_name": article["author_name"],
                "author_title": article["author_title"],
                "full_text": article["full_text"],
                "summary": summary,
                "keywords": keywords,
            })

        issue = {
            "year": issue_year,
            "month": issue_month,
            "articles": issue_articles,
        }

        out_path = ISSUES_DIR / filename
        if dry_run:
            print(f"  {filename}: {len(issue_articles)} articles")
        else:
            out_path.write_text(json.dumps(issue, indent=2) + "\n")
            files_written += 1
        total_articles_written += len(issue_articles)

    print()
    if dry_run:
        print(f"Dry run: would write {len(by_file)} issue files with {total_articles_written} articles")
    else:
        print(f"Wrote {files_written} issue files with {total_articles_written} articles to {ISSUES_DIR}/")
    print(f"  {articles_with_summary} with matched summaries, {articles_auto_summary} with auto-generated summaries")


def main():
    parser = argparse.ArgumentParser(description="Migrate articles/original + data into issues/")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()
    run_migration(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
