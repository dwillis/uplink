#!/usr/bin/env python3
"""
Two-stage re-extraction of articles from text/*.txt, replacing the single-call
approach in convert_to_json.py that silently truncates output on long issues.

Stage A (inventory): one small-output LLM call per issue that enumerates every
editorial item (headline, byline, approximate location, first/last words) --
never truncates because the response is just a manifest, not full article text.

Stage B (extract): one LLM call per article, given only that article's slice
of the issue text plus its inventory anchors, asking for a verbatim
reconstruction. Output per call is a few KB, so truncation isn't a factor.

Assemble: merges Stage A + Stage B results into issues/{stem}.json (schema
v2), preserving existing summary/keywords for articles that already had them
via fuzzy headline matching.

Usage:
    uv run python src/extract_articles.py --from-report          # red+yellow issues
    uv run python src/extract_articles.py 2001_07 1994_05        # explicit stems
    uv run python src/extract_articles.py --all                  # every issue
    uv run python src/extract_articles.py 2001_07 --stage inventory
    uv run python src/extract_articles.py 2001_07 --stage extract
    uv run python src/extract_articles.py 2001_07 --assemble-only
    uv run python src/extract_articles.py --from-report --dry-run
    uv run python src/extract_articles.py 2001_07 --model qwen3.5:35b
"""

import argparse
import difflib
import json
import re
import time
from datetime import date

import llm

from pipeline_common import ISSUES_DIR, WORK_DIR, is_continuation_fragment, parse_text_pages

INVENTORY_DIR = WORK_DIR / "inventory"
ARTICLES_DIR = WORK_DIR / "articles"

DEFAULT_MODEL = "anthropic/claude-sonnet-4-6"

INVENTORY_SYSTEM_PROMPT = """\
You are cataloging the contents of one issue of a journalism newsletter from \
its OCR-extracted text. List EVERY distinct editorial item in reading order, \
including short items, sidebars, and one-paragraph notices -- not just the \
main feature articles.

For each item, identify:
- headline: its title or heading as printed (verbatim)
- kicker: a short section label printed above the headline, if any (e.g. "TEST SCORES"); empty string if none
- byline: the author name and/or affiliation line(s) as printed, verbatim; empty string if none
- first_words: the first ~10 words of the item's body text, verbatim
- last_words: the last ~10 words of the item's body text, verbatim -- follow \
any "continued on page X" jump to find the true ending
- kind: one of "article", "column", "listing", "masthead", "ad", "toc"

Classify mastheads, subscription/contact boxes, conference ads, and \
tables-of-contents as their own kind rather than skipping them, so the \
inventory accounts for all of the text.

Return JSON only, matching the schema."""

INVENTORY_SCHEMA = {
    "type": "object",
    "properties": {
        "articles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "headline": {"type": "string"},
                    "kicker": {"type": "string"},
                    "byline": {"type": "string"},
                    "first_words": {"type": "string"},
                    "last_words": {"type": "string"},
                    "kind": {
                        "type": "string",
                        "enum": ["article", "column", "listing", "masthead", "ad", "toc"],
                    },
                },
                "required": ["headline", "first_words", "last_words", "kind"],
            },
        }
    },
    "required": ["articles"],
}

EXTRACT_SYSTEM_PROMPT = """\
Reconstruct the complete, verbatim text of ONE article from OCR-extracted \
newsletter text. You are given the full issue text and a description of \
where this article begins and ends.

Rules:
- Join words split by line-end hyphenation (e.g. "medio- cre" -> "mediocre")
- Remove page headers, page numbers, and running footers
- If the article jumps to a "continued on page X" section, join that text in
- Do not summarize, paraphrase, or omit any part of the article
- Do not include unrelated headlines, bylines, or captions from other articles
- Extract the author's name, affiliation (publication or organization), and
  job title as separate fields if determinable from the byline

Return JSON only, matching the schema."""

EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "full_text": {"type": "string"},
        "author_name": {"type": "string"},
        "affiliation": {"type": "string"},
        "author_title": {"type": "string"},
    },
    "required": ["full_text"],
}


def call_with_retry(fn, retries=5, base_delay=5):
    """Retry on transient API errors (rate limits, overload) with exponential backoff."""
    for attempt in range(retries):
        try:
            return fn()
        except Exception as e:
            msg = str(e)
            transient = "429" in msg or "rate_limit" in msg or "overloaded" in msg.lower() or "529" in msg
            if not transient or attempt == retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            print(f"[retry in {delay}s: {msg[:80]}]", end=" ", flush=True)
            time.sleep(delay)


def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


def anchor_found(anchor, haystack):
    """Fuzzy-locate a short anchor phrase inside a larger text (OCR-tolerant)."""
    anchor_n = normalize(anchor)
    haystack_n = normalize(haystack)
    if not anchor_n:
        return False
    if anchor_n in haystack_n:
        return True
    words = anchor_n.split()
    if len(words) < 4:
        return False
    # slide a window and accept a high fuzzy ratio -- handles minor OCR noise
    window = len(anchor_n)
    step = max(1, window // 4)
    for i in range(0, max(1, len(haystack_n) - window), step):
        chunk = haystack_n[i:i + window + 20]
        if difflib.SequenceMatcher(None, anchor_n, chunk).ratio() >= 0.7:
            return True
    return False


def issue_full_text(stem):
    return "\n\n".join(parse_text_pages(stem))


def run_inventory(stem, model, force=False):
    out_path = INVENTORY_DIR / f"{stem}.json"
    if out_path.exists() and not force:
        return json.loads(out_path.read_text())

    text = issue_full_text(stem)
    if not text.strip():
        print(f"  [SKIP] {stem}: no text")
        return None

    response = call_with_retry(lambda: model.prompt(text, system=INVENTORY_SYSTEM_PROMPT, schema=INVENTORY_SCHEMA))
    inventory = json.loads(response.text())

    for item in inventory.get("articles", []):
        found_first = anchor_found(item.get("first_words", ""), text)
        found_last = anchor_found(item.get("last_words", ""), text)
        item["unverified"] = not (found_first and found_last)

    INVENTORY_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(inventory, indent=2) + "\n")
    n = len(inventory.get("articles", []))
    unverified = sum(1 for i in inventory["articles"] if i["unverified"])
    print(f"  [OK] {stem}: {n} item(s) in inventory, {unverified} unverified")
    return inventory


CONTINUATION_JUMP_RE = re.compile(r"continued on page|see .*page \d|cont'?d", re.IGNORECASE)


def _find_in_original(text, norm_text, anchor_norm, search_from_orig=0):
    """Find a normalized anchor's approximate position in the ORIGINAL text.

    normalize() collapses whitespace, so an index into norm_text drifts from
    the true offset in `text` -- by hundreds of characters in a long OCR'd
    issue. Searching the original text directly (allowing free whitespace
    between words) avoids that drift instead of just adding a fixed buffer.
    """
    if not anchor_norm:
        return -1
    words = anchor_norm.split()
    if not words:
        return -1
    pattern = r"\s+".join(re.escape(w) for w in words[:8])
    m = re.search(pattern, text[search_from_orig:], re.IGNORECASE)
    if m:
        return search_from_orig + m.start()
    return -1


def slice_around_anchors(text, first_words, last_words):
    """Return a bounded slice of the issue text likely to contain one article.

    Falls back to the whole text if anchors can't be located -- Stage B still
    benefits from the first/last-word instructions even without a tight slice.
    """
    start_anchor = normalize(first_words)
    end_anchor = normalize(last_words)

    start_idx = _find_in_original(text, None, start_anchor)
    if start_idx == -1:
        return text  # let the model search the whole issue

    char_start = max(0, start_idx - 200)

    # A short or "continued on page N" anchor means Stage A likely didn't
    # capture the true ending -- give the model the rest of the issue
    # instead of a tight window it might get cut off within.
    unreliable_anchor = len(end_anchor.split()) <= 4 or CONTINUATION_JUMP_RE.search(last_words or "")

    end_idx = -1 if unreliable_anchor else _find_in_original(text, None, end_anchor, start_idx)
    if end_idx != -1 and end_idx > start_idx:
        char_end = min(len(text), end_idx + len(last_words or "") + 500)
    else:
        # Anchor not found at all (as opposed to found-but-unreliable) --
        # rather than guess a window size, give the rest of the issue.
        char_end = len(text)
    return text[char_start:char_end]


MIN_GOOD_LENGTH = 400  # matches report.py's "very short" truncation threshold


def existing_good_articles(stem):
    """Articles already in issues/{stem}.json with substantial, non-truncated
    full_text, keyed by normalized headline -- used to skip re-extracting
    content that's already good rather than reprocessing every issue from
    scratch."""
    from report import looks_truncated

    issue_path = ISSUES_DIR / f"{stem}.json"
    if not issue_path.exists():
        return {}
    old_articles = json.loads(issue_path.read_text()).get("articles", [])
    good = {}
    for a in old_articles:
        full_text = a.get("full_text", "")
        if len(full_text) >= MIN_GOOD_LENGTH and not looks_truncated(full_text):
            norm = re.sub(r"[^a-z0-9 ]", "", a.get("headline", "").lower()).strip()
            good[norm] = a
    return good


def run_extract(stem, model, force=False):
    inv_path = INVENTORY_DIR / f"{stem}.json"
    if not inv_path.exists():
        print(f"  [SKIP] {stem}: no inventory, run --stage inventory first")
        return

    inventory = json.loads(inv_path.read_text())
    text = issue_full_text(stem)
    out_dir = ARTICLES_DIR / stem
    out_dir.mkdir(parents=True, exist_ok=True)

    items = [
        item for item in inventory.get("articles", [])
        if item.get("kind") in ("article", "column", "listing")
    ]
    good_by_headline = {} if force else existing_good_articles(stem)
    good_headlines = list(good_by_headline.keys())

    for idx, item in enumerate(items):
        out_path = out_dir / f"{idx:02d}.json"
        if out_path.exists() and not force:
            continue

        norm = re.sub(r"[^a-z0-9 ]", "", item["headline"].lower()).strip()
        match = difflib.get_close_matches(norm, good_headlines, n=1, cutoff=0.85)
        if match:
            old = good_by_headline[match[0]]
            out_path.write_text(json.dumps({
                "full_text": old.get("full_text", ""),
                "author_name": old.get("author_name", ""),
                "affiliation": old.get("affiliation", ""),
                "author_title": old.get("author_title", ""),
                "headline": item["headline"],
                "kicker": item.get("kicker", ""),
                "unverified": False,
                "reused": True,
            }, indent=2) + "\n")
            print(f"  [{idx + 1}/{len(items)}] {item['headline'][:60]}... (reusing existing text)")
            continue

        slice_text = slice_around_anchors(text, item["first_words"], item["last_words"])
        last_words = item.get("last_words", "")
        unreliable_end = len(normalize(last_words).split()) <= 4 or CONTINUATION_JUMP_RE.search(last_words or "")
        end_hint = (
            f"Article ends: \"{last_words}\" -- this hint may be incomplete or approximate. "
            f"If the article's content clearly continues past that point on the same topic, "
            f"keep going until you reach a natural conclusion, a byline/headline for a "
            f"different article, or the end of the provided text."
            if unreliable_end else
            f"Article ends: \"{last_words}\""
        )
        prompt = (
            f"Headline: {item['headline']}\n"
            f"Byline: {item.get('byline', '')}\n"
            f"Article begins: \"{item['first_words']}\"\n"
            f"{end_hint}\n\n"
            f"--- ISSUE TEXT (may include other articles; extract only this one) ---\n\n"
            f"{slice_text}"
        )
        print(f"  [{idx + 1}/{len(items)}] {item['headline'][:60]}...", end=" ", flush=True)
        try:
            response = call_with_retry(lambda: model.prompt(prompt, system=EXTRACT_SYSTEM_PROMPT, schema=EXTRACT_SCHEMA))
            result = json.loads(response.text())
        except Exception as e:
            print(f"ERROR: {e}")
            continue

        full_text = result.get("full_text", "")
        # An unreliable end anchor means the model was told to use its own
        # judgment on where to stop, so requiring the (bad) anchor to appear
        # at the end would just penalize a correct, longer extraction.
        ends_ok = (
            True if unreliable_end or not last_words
            else anchor_found(last_words, full_text[-300:])
        )
        result["headline"] = item["headline"]
        result["kicker"] = item.get("kicker", "")
        result["unverified"] = not ends_ok

        out_path.write_text(json.dumps(result, indent=2) + "\n")
        print(f"OK ({len(full_text)} chars{'' if ends_ok else ', UNVERIFIED ending'})")
        time.sleep(0.3)


def assemble(stem):
    """Merge work/inventory + work/articles into issues/{stem}.json (schema v2)."""
    issue_path = ISSUES_DIR / f"{stem}.json"
    old_data = json.loads(issue_path.read_text()) if issue_path.exists() else {}
    old_articles = old_data.get("articles", [])

    inv_path = INVENTORY_DIR / f"{stem}.json"
    art_dir = ARTICLES_DIR / stem
    if not inv_path.exists() or not art_dir.exists():
        print(f"  [SKIP] {stem}: missing inventory or extracted articles")
        return False

    inventory = json.loads(inv_path.read_text())
    items = [
        item for item in inventory.get("articles", [])
        if item.get("kind") in ("article", "column", "listing")
    ]

    old_by_norm_headline = {re.sub(r"[^a-z0-9 ]", "", a.get("headline", "").lower()).strip(): a for a in old_articles}
    old_norm_headlines = list(old_by_norm_headline.keys())

    new_articles = []
    for idx, item in enumerate(items):
        art_path = art_dir / f"{idx:02d}.json"
        if not art_path.exists():
            continue
        extracted = json.loads(art_path.read_text())

        norm = re.sub(r"[^a-z0-9 ]", "", item["headline"].lower()).strip()
        match = difflib.get_close_matches(norm, old_norm_headlines, n=1, cutoff=0.85)
        old_article = old_by_norm_headline[match[0]] if match else {}

        if is_continuation_fragment(item) and new_articles:
            # Tail of an earlier article that jumped to a later page --
            # append its text to that article instead of listing it
            # separately. The parent isn't always the immediately preceding
            # entry (other short items can be interleaved and may have
            # scrolled far back), so search the whole issue: prefer a
            # quoted title shared between the fragment and a candidate
            # headline (e.g. "From page four: 'Foo' (continued)" -> "...
            # 'Foo'"), falling back to word overlap, then the most recent
            # article if nothing matches at all.
            fragment_text = item["headline"] + " " + item.get("kicker", "")
            quoted = re.findall(r"'([^']{4,})'", fragment_text)
            best, best_score = new_articles[-1], 0
            for candidate in new_articles:
                score = 0
                if any(q.lower() in candidate["headline"].lower() for q in quoted):
                    score += 100
                fragment_words = set(re.findall(r"[a-z0-9]{4,}", fragment_text.lower()))
                candidate_words = set(re.findall(r"[a-z0-9]{4,}", candidate["headline"].lower()))
                score += len(fragment_words & candidate_words)
                if score > best_score:
                    best, best_score = candidate, score
            best["full_text"] = best["full_text"].rstrip() + "\n\n" + extracted.get("full_text", "").lstrip()
            best["provenance"]["verified"] = best["provenance"]["verified"] and not extracted.get("unverified", False)
            continue

        reused = extracted.get("reused", False)
        merged = {
            "headline": item["headline"],
            "kicker": item.get("kicker", ""),
            "author_name": extracted.get("author_name") or old_article.get("author_name", ""),
            "author_title": extracted.get("author_title") or old_article.get("author_title", ""),
            "affiliation": extracted.get("affiliation") or old_article.get("affiliation", ""),
            "full_text": extracted.get("full_text", ""),
            "summary": old_article.get("summary", ""),
            "keywords": old_article.get("keywords", []),
            "topics": old_article.get("topics", []),
            "technologies": old_article.get("technologies", []),
            "provenance": {
                "extracted_by": old_article.get("provenance", {}).get("extracted_by", "pre-v2")
                                if reused else DEFAULT_MODEL,
                "extracted_at": old_article.get("provenance", {}).get("extracted_at", "")
                                if reused else date.today().isoformat(),
                "verified": not extracted.get("unverified", False),
            },
        }
        # Permanent identifiers are minted once (docs/src/mint-ids.mjs) and
        # must survive re-extraction of the issue.
        if old_article.get("id"):
            merged = {"id": old_article["id"], **merged}
        new_articles.append(merged)

    new_data = {
        "schema_version": 2,
        "year": old_data.get("year"),
        "month": old_data.get("month"),
        "articles": new_articles,
    }

    tmp_path = issue_path.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(new_data, indent=2) + "\n")
    tmp_path.replace(issue_path)
    print(f"  [ASSEMBLED] {stem}: {len(new_articles)} article(s) "
          f"({len(old_articles)} before)")
    return True


def stems_from_report():
    report_path = WORK_DIR.parent / "reports" / "report.json"
    data = json.loads(report_path.read_text())
    return sorted({r["stem"] for r in data["red"]} | {r["stem"] for r in data["yellow"]})


def all_stems():
    return sorted(p.stem for p in ISSUES_DIR.glob("*.json") if p.stem != "cleaned_stories")


def main():
    parser = argparse.ArgumentParser(description="Two-stage per-article re-extraction")
    parser.add_argument("stems", nargs="*", help="Issue stems to process, e.g. 2001_07")
    parser.add_argument("--from-report", action="store_true", help="Use red+yellow issues from reports/report.json")
    parser.add_argument("--all", action="store_true", help="Process every issue")
    parser.add_argument("--stage", choices=["inventory", "extract"], help="Run only one stage")
    parser.add_argument("--assemble-only", action="store_true", help="Only merge existing work/ output into issues/")
    parser.add_argument("--force", action="store_true", help="Re-run stages even if output exists")
    parser.add_argument("--dry-run", action="store_true", help="Print the stems that would be processed and exit")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"LLM model to use (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    if args.from_report:
        stems = stems_from_report()
    elif args.all:
        stems = all_stems()
    elif args.stems:
        stems = args.stems
    else:
        parser.error("Provide stems, or use --from-report / --all")

    print(f"{len(stems)} issue(s): {', '.join(stems) if len(stems) <= 10 else stems[0] + ' .. ' + stems[-1]}")
    if args.dry_run:
        for s in stems:
            print(f"  {s}")
        return

    model = None if args.assemble_only else llm.get_model(args.model)

    for stem in stems:
        print(f"=== {stem} ===")
        if args.assemble_only:
            assemble(stem)
            continue
        if args.stage in (None, "inventory"):
            run_inventory(stem, model, force=args.force)
        if args.stage in (None, "extract"):
            run_extract(stem, model, force=args.force)
        if args.stage is None:
            assemble(stem)


if __name__ == "__main__":
    main()
