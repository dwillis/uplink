"""
Generate summaries and keywords for articles in issues/ that are missing them.

Scans issues/*.json for articles where summary is empty or auto-generated
(short, no keywords), calls an LLM to generate proper summaries, and updates
the files in place.

Usage:
    uv run python src/summarize_unmatched.py              # run
    uv run python src/summarize_unmatched.py --dry-run    # preview
    uv run python src/summarize_unmatched.py --model anthropic/claude-sonnet-4-6
"""

import argparse
import json
import re
import time
from pathlib import Path

import llm

ISSUES_DIR = Path(__file__).resolve().parent.parent / "issues"

SYSTEM_PROMPT = (
    "Given the full text of a journalism newsletter article, return a JSON object "
    'with two keys: "summary" (a 1-2 sentence description of the article) and '
    '"keywords" (an array of exactly 3 single words). No other text.'
)


def needs_summary(article):
    """Check if an article needs a better summary."""
    summary = article.get("summary", "")
    keywords = article.get("keywords", [])
    if not summary:
        return True
    if not keywords:
        return True
    return False


def generate_summary(model, article):
    """Call LLM to generate summary + keywords for one article."""
    text = article["full_text"][:3000]
    response = model.prompt(text, system=SYSTEM_PROMPT)
    raw = response.text().strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```\w*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description="Generate summaries for articles missing them")
    parser.add_argument("--dry-run", action="store_true", help="Just show articles needing summaries")
    parser.add_argument("--model", default="claude-haiku-4.5", help="LLM model to use")
    args = parser.parse_args()

    # Find articles needing summaries
    to_process = []
    total = 0
    for f in sorted(ISSUES_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        for i, article in enumerate(data.get("articles", [])):
            total += 1
            if needs_summary(article):
                to_process.append((f, i, article))

    print(f"Total articles: {total}, needing summaries: {len(to_process)}")

    if args.dry_run:
        for f, i, a in to_process:
            print(f"  {f.name} [{i}] {a['headline'][:60]}")
        return

    if not to_process:
        print("Nothing to do.")
        return

    model = llm.get_model(args.model)

    # Group by file so we can batch writes
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
            label = f"{article['headline'][:50]}"
            print(f"[{processed}/{len(to_process)}] {filepath.name}[{idx}] {label}...", end=" ", flush=True)
            try:
                result = generate_summary(model, article)
                data["articles"][idx]["summary"] = result.get("summary", "")
                data["articles"][idx]["keywords"] = result.get("keywords", [])[:3]
                modified = True
                print("OK")
            except Exception as e:
                print(f"ERROR: {e}")
                errors += 1
                continue

            if processed < len(to_process):
                time.sleep(0.5)

        if modified:
            filepath.write_text(json.dumps(data, indent=2) + "\n")
            print(f"  -> Updated {filepath.name}")

    print(f"\nDone. Processed {processed} articles ({errors} errors).")


if __name__ == "__main__":
    main()
