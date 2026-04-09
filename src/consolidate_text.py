#!/usr/bin/env python3
"""
One-time script: fill gaps in text/ from claude_text/ or gemini_text/.

For each PDF, ensures text/ has a file. Priority:
1. Keep existing text/ file if present
2. Copy from claude_text/ if available
3. Copy from gemini_text/ as fallback

Usage:
    uv run python src/consolidate_text.py              # run
    uv run python src/consolidate_text.py --dry-run    # preview
"""

import argparse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = REPO_ROOT / "pdfs"
TEXT_DIR = REPO_ROOT / "text"
CLAUDE_DIR = REPO_ROOT / "claude_text"
GEMINI_DIR = REPO_ROOT / "gemini_text"


def main():
    parser = argparse.ArgumentParser(description="Fill gaps in text/ from other extraction dirs")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    pdfs = sorted(f.stem for f in PDF_DIR.glob("*.pdf"))
    existing = set(f.stem for f in TEXT_DIR.glob("*.txt"))

    filled = 0
    missing = 0

    for stem in pdfs:
        if stem in existing:
            continue

        # Try claude_text first, then gemini_text
        source = None
        for candidate_dir in [CLAUDE_DIR, GEMINI_DIR]:
            candidate = candidate_dir / f"{stem}.txt"
            if candidate.exists() and candidate.stat().st_size > 0:
                source = candidate
                break

        if source:
            dest = TEXT_DIR / f"{stem}.txt"
            if args.dry_run:
                print(f"  Would copy {source.parent.name}/{stem}.txt -> text/")
            else:
                shutil.copy2(source, dest)
                print(f"  Copied {source.parent.name}/{stem}.txt -> text/")
            filled += 1
        else:
            print(f"  [MISSING] No text found for {stem}")
            missing += 1

    print(f"\n{'Would fill' if args.dry_run else 'Filled'} {filled} gaps, {missing} still missing")
    print(f"text/ now has {len(existing) + (filled if not args.dry_run else 0)} files (of {len(pdfs)} PDFs)")


if __name__ == "__main__":
    main()
