#!/usr/bin/env python3
"""
Normalize the free-text `technologies` field in issues/*.json against
data/technology_aliases.json (lowercase variant -> canonical name).

The alias map's canonical names should exist in data/technologies.json (the
vocabulary shown to the enrichment model); extend that file when promoting a
new canonical. A variant absent from the map is treated as already canonical.
Mapping a variant to "" drops the tag (vague non-technologies like
"database" or "software").

Curation workflow:
    uv run python src/normalize_technologies.py --dump      # write reports/technology_variants.csv
    # ...fold curated rows into data/technology_aliases.json...
    uv run python src/normalize_technologies.py --apply --dry-run
    uv run python src/normalize_technologies.py --apply     # rewrite issues/*.json
    uv run python src/normalize_technologies.py --check     # CI-able drift check
"""

import argparse
import csv
import json
import sys
from collections import Counter

from pipeline_common import DATA_DIR, ISSUES_DIR, REPORTS_DIR

ALIASES_PATH = DATA_DIR / "technology_aliases.json"
TECHNOLOGIES_PATH = DATA_DIR / "technologies.json"
VARIANTS_CSV = REPORTS_DIR / "technology_variants.csv"


def load_aliases():
    if ALIASES_PATH.exists():
        return json.loads(ALIASES_PATH.read_text())
    return {}


def load_vocabulary():
    if TECHNOLOGIES_PATH.exists():
        return json.loads(TECHNOLOGIES_PATH.read_text())
    return []


def issue_files():
    return [p for p in sorted(ISSUES_DIR.glob("*.json")) if p.stem != "cleaned_stories"]


def iter_articles(data):
    return data.get("articles", [])


def build_lookup(aliases, vocab):
    """Lowercase key -> canonical form. The vocabulary supplies canonical
    casing (so "Gopher" folds into "gopher"); explicit aliases override."""
    lookup = {v.lower(): v for v in vocab}
    lookup.update(aliases)
    return lookup


def normalize_list(technologies, lookup):
    """Map each entry through the lookup, drop ""-mapped entries, and
    dedupe case-insensitively keeping the first occurrence (mirrors
    enrich_article in extract_metadata.py)."""
    seen = set()
    out = []
    for tech in technologies:
        stripped = tech.strip()
        if not stripped:
            continue
        key = stripped.lower()
        canonical = lookup[key] if key in lookup else stripped
        if canonical == "":
            continue
        dedupe_key = canonical.lower()
        if dedupe_key not in seen:
            seen.add(dedupe_key)
            out.append(canonical)
    return out


def cmd_dump():
    aliases = load_aliases()
    vocab = load_vocabulary()
    vocab_by_lower = {v.lower(): v for v in vocab}

    counts = Counter()
    for path in issue_files():
        for article in iter_articles(json.loads(path.read_text())):
            for tech in article.get("technologies", []):
                if tech.strip():
                    counts[tech.strip()] += 1

    REPORTS_DIR.mkdir(exist_ok=True)
    with VARIANTS_CSV.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["count", "variant", "suggested_canonical"])
        for variant, count in counts.most_common():
            key = variant.lower()
            suggestion = aliases.get(key, vocab_by_lower.get(key, ""))
            if suggestion == variant:
                suggestion = ""  # already canonical
            writer.writerow([count, variant, suggestion])

    print(f"Wrote {VARIANTS_CSV} ({len(counts)} distinct values, "
          f"{sum(counts.values())} total tags)")


def cmd_apply(dry_run):
    lookup = build_lookup(load_aliases(), load_vocabulary())
    changed_files = 0
    changed_articles = 0
    dropped = Counter()
    renamed = Counter()

    for path in issue_files():
        data = json.loads(path.read_text())
        modified = False
        for article in iter_articles(data):
            old = article.get("technologies")
            if not old:
                continue
            new = normalize_list(old, lookup)
            if new != old:
                for t in old:
                    key = t.strip().lower()
                    if lookup.get(key) == "":
                        dropped[t.strip()] += 1
                    elif key in lookup and lookup[key] != t.strip():
                        renamed[f"{t.strip()} -> {lookup[key]}"] += 1
                article["technologies"] = new
                changed_articles += 1
                modified = True
        if modified:
            changed_files += 1
            if not dry_run:
                path.write_text(json.dumps(data, indent=2) + "\n")

    label = "Would update" if dry_run else "Updated"
    print(f"{label} {changed_articles} article(s) in {changed_files} file(s).")
    if renamed:
        print(f"Top renames: {renamed.most_common(10)}")
    if dropped:
        print(f"Top drops: {dropped.most_common(10)}")


def cmd_check():
    aliases = load_aliases()
    vocab = load_vocabulary()
    vocab_lower = {v.lower() for v in vocab}
    lookup = build_lookup(aliases, vocab)
    problems = []

    for canonical in set(aliases.values()):
        if canonical and canonical.lower() not in vocab_lower:
            problems.append(
                f"alias target not in data/technologies.json: {canonical!r}"
            )

    # The corpus is normalized iff re-normalizing is a no-op.
    stale = Counter()
    for path in issue_files():
        for article in iter_articles(json.loads(path.read_text())):
            old = article.get("technologies", [])
            if old and normalize_list(old, lookup) != old:
                stale[path.name] += 1
    for name, count in stale.most_common():
        problems.append(f"{name}: {count} article(s) not normalized (run --apply)")

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        sys.exit(1)
    print("OK: corpus technologies are normalized and alias targets are in the vocabulary.")


def main():
    parser = argparse.ArgumentParser(description="Normalize the technologies field against data/technology_aliases.json")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dump", action="store_true", help="Write reports/technology_variants.csv for curation")
    mode.add_argument("--apply", action="store_true", help="Rewrite issues/*.json with normalized technologies")
    mode.add_argument("--check", action="store_true", help="Exit nonzero if the corpus or alias map has drifted")
    parser.add_argument("--dry-run", action="store_true", help="With --apply: report what would change without writing")
    args = parser.parse_args()

    if args.dump:
        cmd_dump()
    elif args.apply:
        cmd_apply(args.dry_run)
    else:
        cmd_check()


if __name__ == "__main__":
    main()
