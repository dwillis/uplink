"""
clean.py — Flatten issues/*.json into a single-file "story" format for
external consumers (the "Beat Book" pipeline), stripping HTML from summaries.

Usage:
    uv run python src/clean.py issues/

Output:
    {source_dir}/cleaned_stories.json  (e.g. issues/cleaned_stories.json)
"""

import argparse
import json
import glob
import re
from pathlib import Path
from datetime import datetime


def strip_html(html: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#x27;|&#39;", "'", text)
    text = re.sub(r"&nbsp;", " ", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_date(entry: dict) -> dict:
    """Extract year, month, day and ISO date string."""
    raw = entry.get("published_parsed") or entry.get("published", "")
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except Exception:
        try:
            dt = datetime.strptime(raw[:10], "%Y-%m-%d")
        except Exception:
            return {"date": raw[:10] if len(raw) >= 10 else "", "year": 0, "month": 0, "day": 0}
    return {
        "date": dt.strftime("%Y-%m-%d"),
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
    }


def convert_entry(entry: dict, year: int, month: int) -> dict:
    """Convert one article entry to the standard story dict."""
    date_str = f"{year:04d}-{month:02d}-01"

    content = entry.get("full_text", "").strip() or strip_html(entry.get("summary", ""))
    title   = entry.get("headline", "").strip()
    author  = entry.get("author_name", "").strip()
    tags    = entry.get("keywords", [])

    # Build a content string with header metadata
    header_parts = [title]
    if date_str:
        header_parts.append(date_str)
    if author:
        header_parts.append(f"Author/Byline: {author}")
    content_full = "\n\n".join(header_parts) + "\n\n" + content

    article_id = f"{year}_{month:02d}_{title[:60]}"

    return {
        "title": title,
        "date": date_str,
        "author": author,
        "content": content_full,
        "docref": "",
        "article_id": article_id,
        "content_source": "full_text",
        "year": year,
        "month": month,
        "day": 1,
        "tags": tags if isinstance(tags, list) else [],
    }


def main():
    parser = argparse.ArgumentParser(description="Convert alt-format RSS-style JSONs into the standard story format.")
    parser.add_argument("script_dir", type=Path, help="Directory containing source JSON files")
    args = parser.parse_args()
    script_dir = args.script_dir
    pattern    = str(script_dir / "**" / "*.json")
    out_file   = script_dir / "cleaned_stories.json"

    all_stories = []
    seen_ids    = set()

    files = sorted(glob.glob(pattern, recursive=True))
    # Exclude our own output file
    files = [f for f in files if Path(f).name != "cleaned_stories.json"]

    print(f"Found {len(files)} JSON files in {script_dir}")

    for filepath in files:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"  ⚠ Skipping {filepath}: {e}")
            continue

        entries = data.get("articles", [])
        if not entries:
            continue

        year  = int(data.get("year", 0))
        month_raw = data.get("month", 0)
        try:
            month = int(month_raw)
        except (ValueError, TypeError):
            first_month = re.match(r"[A-Za-z]+", str(month_raw))
            month = datetime.strptime(first_month.group(), "%B").month if first_month else 1

        converted = 0
        for entry in entries:
            story = convert_entry(entry, year, month)

            # Deduplicate by article_id
            aid = story["article_id"]
            if aid in seen_ids:
                continue
            seen_ids.add(aid)

            # Skip entries with no real content
            if len(story["content"]) < 50:
                continue

            all_stories.append(story)
            converted += 1

        print(f"  ✓ {Path(filepath).name}: {converted} stories (from {len(entries)} entries)")

    # Sort by date
    all_stories.sort(key=lambda s: s.get("date", ""))

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_stories, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Wrote {len(all_stories)} stories to {out_file}")


if __name__ == "__main__":
    main()
