#!/usr/bin/env python3
"""
Validate the Uplink archive pipeline and report problems.

Cross-checks pdfs/, text/, and issues/ for coverage, estimates how much of
each issue's extracted text actually made it into issues/*.json, flags
likely truncation, checks the publication schedule for suspicious gaps,
and reports metadata fill rates. Pure stdlib, no LLM calls.

Usage:
    uv run python src/report.py                  # write reports/report.md + report.json
    uv run python src/report.py --check          # same, but exit 1 if any issue is red-flagged
    uv run python src/report.py --issue 2001_07  # print detail for one issue
"""

import argparse
import difflib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = REPO_ROOT / "pdfs"
TEXT_DIR = REPO_ROOT / "text"
ISSUES_DIR = REPO_ROOT / "issues"
WORK_DIR = REPO_ROOT / "work"
DATA_DIR = REPO_ROOT / "data"
REPORTS_DIR = REPO_ROOT / "reports"

SCHEDULE_NOTES_PATH = DATA_DIR / "schedule_notes.json"
COVERAGE_OVERRIDES_PATH = DATA_DIR / "coverage_overrides.json"

RED_THRESHOLD = 0.5
YELLOW_THRESHOLD = 0.65
LOW_ARTICLE_COUNT = 2
LOW_ARTICLE_TEXT_BYTES = 15_000

AFFILIATION_HINTS = [
    "tribune", "times", "post", "star", "herald", "news", "the ",
    "journal", "gazette", "press", "dispatch", "register", "sun",
    "courier", "chronicle", "observer", "record", "bureau", "inc.",
    "associated press", "reuters", "university", "institute",
]
TITLE_HINTS = ["editor", "reporter", "specialist", "director", "analyst", "writer", "producer", "manager"]


def load_json(path):
    return json.loads(path.read_text())


def load_schedule_notes():
    if SCHEDULE_NOTES_PATH.exists():
        return load_json(SCHEDULE_NOTES_PATH)
    return {}


def load_coverage_overrides():
    if COVERAGE_OVERRIDES_PATH.exists():
        return load_json(COVERAGE_OVERRIDES_PATH)
    return {}


# ---------------------------------------------------------------------------
# Text file parsing
# ---------------------------------------------------------------------------

PAGE_HEADER_RE = re.compile(r"^Page \d+\s*$", re.MULTILINE)


def parse_text_pages(stem):
    """Split a text/{stem}.txt file into pages if it has 'Page N' / '---' markers.

    Most text files in this archive came from an alternate OCR pass that
    doesn't include page markers, so this treats the whole file as a single
    page when no markers are present rather than failing.
    """
    path = TEXT_DIR / f"{stem}.txt"
    if not path.exists():
        return []
    raw = path.read_text(errors="replace")
    if "\n\n---\n\n" in raw and PAGE_HEADER_RE.search(raw):
        chunks = raw.split("\n\n---\n\n")
        pages = []
        for chunk in chunks:
            body = PAGE_HEADER_RE.sub("", chunk, count=1).strip()
            pages.append(body)
        return pages
    return [raw]


def effective_text_chars(pages):
    """Character count of page bodies, ignoring the markers themselves."""
    return sum(len(p) for p in pages)


# ---------------------------------------------------------------------------
# Schedule modeling
# ---------------------------------------------------------------------------

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December",
}


def expected_stems():
    """Stems expected under the known publication cadence.

    Monthly October 1990 - December 2000, bimonthly (odd months) January
    2001 - November 2007 (archive ends March 2007).
    """
    stems = []
    for month in range(10, 13):
        stems.append(f"1990_{month:02d}")
    for year in range(1991, 2001):
        for month in range(1, 13):
            stems.append(f"{year}_{month:02d}")
    for year in range(2001, 2008):
        for month in range(1, 12, 2):
            if year == 2007 and month > 3:
                break
            stems.append(f"{year}_{month:02d}")
    return stems


def parse_months_field(data):
    """Best-effort parse of the issue's `month` string into a set of month ints."""
    month_field = data.get("month", "")
    if isinstance(month_field, int):
        return {month_field}
    months = set()
    for num, name in MONTH_NAMES.items():
        if name.lower() in str(month_field).lower():
            months.add(num)
    return months


def schedule_gaps(actual_stems, issues_by_stem, schedule_notes):
    """Expected stems with no corresponding issue file, minus confirmed non-publications.

    A gap at YYYY_MM is also considered covered if any actual issue's parsed
    `month` field includes MM for that year (bimonthly issues like "July-August"
    filed under 2001_07 satisfy the 2001_08 slot).
    """
    covered_year_months = set()
    for stem, data in issues_by_stem.items():
        year = data.get("year")
        for month in parse_months_field(data):
            covered_year_months.add((year, month))

    gaps = []
    for stem in expected_stems():
        if stem in actual_stems:
            continue
        year, month = int(stem[:4]), int(stem[5:7])
        if (year, month) in covered_year_months:
            continue
        if stem in schedule_notes:
            continue
        gaps.append(stem)
    return gaps


# ---------------------------------------------------------------------------
# Coverage + truncation
# ---------------------------------------------------------------------------

SENTENCE_END_RE = re.compile(r'["\')\]]?[.!?]["\')\]]?\s*$')
CONTINUATION_RE = re.compile(r"continued on page|see .*page \d|cont'?d", re.IGNORECASE)


def looks_truncated(full_text):
    """Heuristics for a mid-cut or continuation-pointer ending."""
    text = full_text.strip()
    if not text:
        return "empty"
    if CONTINUATION_RE.search(text[-120:]):
        return "continuation marker at end"
    if len(text) < 400:
        return "very short"
    if not SENTENCE_END_RE.search(text):
        return "no sentence-ending punctuation"
    if text[-1].isalpha() and text.rstrip().endswith("-"):
        return "ends mid-hyphenation"
    return None


def analyze_issue(stem, overrides):
    issue_path = ISSUES_DIR / f"{stem}.json"
    data = load_json(issue_path)
    articles = data.get("articles", [])

    pages = parse_text_pages(stem)
    text_chars = effective_text_chars(pages)
    captured_chars = sum(len(a.get("full_text", "")) for a in articles)
    ratio = (captured_chars / text_chars) if text_chars else 1.0

    override = overrides.get(stem)
    if override:
        band = "override"
    elif ratio < RED_THRESHOLD:
        band = "red"
    elif ratio < YELLOW_THRESHOLD:
        band = "yellow"
    else:
        band = "green"

    flags = []
    if len(articles) <= LOW_ARTICLE_COUNT and text_chars > LOW_ARTICLE_TEXT_BYTES and not override:
        flags.append(f"only {len(articles)} article(s) from {text_chars} chars of text")

    truncated = []
    for i, a in enumerate(articles):
        reason = looks_truncated(a.get("full_text", ""))
        if reason:
            truncated.append({"index": i, "headline": a.get("headline", ""), "reason": reason})

    return {
        "stem": stem,
        "data": data,
        "num_articles": len(articles),
        "text_chars": text_chars,
        "captured_chars": captured_chars,
        "ratio": ratio,
        "band": band,
        "override_reason": override,
        "flags": flags,
        "truncated": truncated,
    }


# ---------------------------------------------------------------------------
# TOC / inventory cross-check (only active once work/inventory/*.json exists)
# ---------------------------------------------------------------------------

def normalize_headline(h):
    return re.sub(r"[^a-z0-9 ]", "", h.lower()).strip()


def toc_diff(stem, articles):
    inv_path = WORK_DIR / "inventory" / f"{stem}.json"
    if not inv_path.exists():
        return None
    inventory = load_json(inv_path).get("articles", [])
    inv_headlines = [
        item["headline"] for item in inventory
        if item.get("kind", "article") in ("article", "column", "listing")
    ]
    issue_headlines = [normalize_headline(a.get("headline", "")) for a in articles]

    missing = []
    for h in inv_headlines:
        norm = normalize_headline(h)
        best = difflib.get_close_matches(norm, issue_headlines, n=1, cutoff=0.85)
        if not best:
            missing.append(h)
    return missing


# ---------------------------------------------------------------------------
# Metadata fill rates
# ---------------------------------------------------------------------------

def looks_like_affiliation(title):
    t = title.lower()
    if any(h in t for h in TITLE_HINTS):
        return False
    return any(h in t for h in AFFILIATION_HINTS)


def metadata_fill(issue_results):
    total = 0
    missing_author = 0
    missing_keywords = 0
    missing_summary = 0
    missing_topics = 0
    missing_technologies = 0
    mislabeled_title = 0

    for result in issue_results:
        for a in result["data"].get("articles", []):
            total += 1
            if not a.get("author_name"):
                missing_author += 1
            if not a.get("keywords"):
                missing_keywords += 1
            if not a.get("summary"):
                missing_summary += 1
            if "topics" not in a or not a.get("topics"):
                missing_topics += 1
            if "technologies" not in a or not a.get("technologies"):
                missing_technologies += 1
            if a.get("author_title") and looks_like_affiliation(a["author_title"]) and not a.get("affiliation"):
                mislabeled_title += 1

    return {
        "total": total,
        "missing_author": missing_author,
        "missing_keywords": missing_keywords,
        "missing_summary": missing_summary,
        "missing_topics": missing_topics,
        "missing_technologies": missing_technologies,
        "mislabeled_title": mislabeled_title,
    }


# ---------------------------------------------------------------------------
# Top-level checks
# ---------------------------------------------------------------------------

def file_coverage():
    pdf_stems = {p.stem for p in PDF_DIR.glob("*.pdf")}
    text_stems = {p.stem for p in TEXT_DIR.glob("*.txt")}
    issue_stems = {p.stem for p in ISSUES_DIR.glob("*.json") if p.stem != "cleaned_stories"}
    return {
        "pdf_stems": pdf_stems,
        "text_stems": text_stems,
        "issue_stems": issue_stems,
        "pdf_no_text": sorted(pdf_stems - text_stems),
        "text_no_issue": sorted(text_stems - issue_stems),
        "issue_no_pdf": sorted(issue_stems - pdf_stems),
        "text_no_pdf": sorted(text_stems - pdf_stems),
    }


def run_report():
    overrides = load_coverage_overrides()
    schedule_notes = load_schedule_notes()
    coverage = file_coverage()

    results = [analyze_issue(stem, overrides) for stem in sorted(coverage["issue_stems"])]
    issues_by_stem = {r["stem"]: r["data"] for r in results}

    gaps = schedule_gaps(coverage["issue_stems"], issues_by_stem, schedule_notes)

    for r in results:
        r["toc_missing"] = toc_diff(r["stem"], r["data"].get("articles", []))

    fill = metadata_fill(results)

    red = [r for r in results if r["band"] == "red"]
    yellow = [r for r in results if r["band"] == "yellow"]
    green = [r for r in results if r["band"] == "green"]
    overridden = [r for r in results if r["band"] == "override"]

    total_articles = sum(r["num_articles"] for r in results)
    total_truncated = sum(len(r["truncated"]) for r in results)
    toc_checked = [r for r in results if r["toc_missing"] is not None]
    total_toc_missing = sum(len(r["toc_missing"]) for r in toc_checked)

    return {
        "coverage": coverage,
        "results": results,
        "gaps": gaps,
        "fill": fill,
        "red": red,
        "yellow": yellow,
        "green": green,
        "overridden": overridden,
        "total_articles": total_articles,
        "total_truncated": total_truncated,
        "toc_checked": toc_checked,
        "total_toc_missing": total_toc_missing,
    }


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_markdown(report):
    lines = []
    lines.append("# Uplink Archive Report\n")

    lines.append("## Summary\n")
    lines.append(f"- Issues: {len(report['results'])} "
                 f"(PDFs: {len(report['coverage']['pdf_stems'])}, "
                 f"text: {len(report['coverage']['text_stems'])})")
    lines.append(f"- Articles: {report['total_articles']}")
    lines.append(f"- Coverage bands: {len(report['green'])} green, "
                 f"{len(report['yellow'])} yellow, {len(report['red'])} red, "
                 f"{len(report['overridden'])} overridden")
    lines.append(f"- Articles flagged as possibly truncated: {report['total_truncated']}")
    if report["toc_checked"]:
        lines.append(f"- TOC cross-check ran on {len(report['toc_checked'])} issue(s), "
                     f"{report['total_toc_missing']} headline(s) enumerated but not extracted")
    else:
        lines.append("- TOC cross-check: not yet available (run Stage A inventory first)")
    lines.append(f"- Unexplained schedule gaps: {len(report['gaps'])}")
    lines.append("")

    lines.append("## File coverage\n")
    c = report["coverage"]
    for label, key in [
        ("PDFs missing text/", "pdf_no_text"),
        ("text/ missing issues/", "text_no_issue"),
        ("issues/ with no source PDF", "issue_no_pdf"),
        ("text/ with no source PDF", "text_no_pdf"),
    ]:
        vals = c[key]
        lines.append(f"- {label}: {len(vals)}" + (f" — {', '.join(vals)}" if vals else ""))
    lines.append("")

    lines.append("## Metadata fill rates\n")
    f = report["fill"]
    total = f["total"] or 1
    lines.append(f"- Total articles: {f['total']}")
    lines.append(f"- Missing author_name: {f['missing_author']} ({f['missing_author']/total:.1%})")
    lines.append(f"- Missing summary: {f['missing_summary']} ({f['missing_summary']/total:.1%})")
    lines.append(f"- Missing keywords: {f['missing_keywords']} ({f['missing_keywords']/total:.1%})")
    lines.append(f"- Missing topics: {f['missing_topics']} ({f['missing_topics']/total:.1%})")
    lines.append(f"- Missing technologies: {f['missing_technologies']} ({f['missing_technologies']/total:.1%})")
    lines.append(f"- author_title values that look like an affiliation (should move to `affiliation`): {f['mislabeled_title']}")
    lines.append("")

    lines.append("## Unexplained schedule gaps\n")
    if report["gaps"]:
        lines.append("Expected issues with no file and no confirmed non-publication note "
                     "(add confirmed ones to `data/schedule_notes.json`):\n")
        for g in report["gaps"]:
            lines.append(f"- {g}")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("## Red-flag issues (coverage < %.0f%%)\n" % (RED_THRESHOLD * 100))
    lines.append("| issue | articles | captured/text chars | ratio | flags |")
    lines.append("|---|---|---|---|---|")
    for r in sorted(report["red"], key=lambda r: r["ratio"]):
        flag_text = "; ".join(r["flags"]) if r["flags"] else ""
        lines.append(f"| {r['stem']} | {r['num_articles']} | "
                     f"{r['captured_chars']}/{r['text_chars']} | {r['ratio']:.2f} | {flag_text} |")
    lines.append("")

    lines.append("## Yellow issues (coverage %.0f%%–%.0f%%)\n" % (RED_THRESHOLD * 100, YELLOW_THRESHOLD * 100))
    lines.append("| issue | articles | captured/text chars | ratio |")
    lines.append("|---|---|---|---|")
    for r in sorted(report["yellow"], key=lambda r: r["ratio"]):
        lines.append(f"| {r['stem']} | {r['num_articles']} | "
                     f"{r['captured_chars']}/{r['text_chars']} | {r['ratio']:.2f} |")
    lines.append("")

    trunc_issues = [r for r in report["results"] if r["truncated"]]
    if trunc_issues:
        lines.append("## Possibly truncated articles\n")
        lines.append("<details><summary>%d issue(s) with flagged articles</summary>\n" % len(trunc_issues))
        for r in trunc_issues:
            lines.append(f"\n**{r['stem']}**")
            for t in r["truncated"]:
                lines.append(f"- [{t['index']}] {t['headline'][:70]} — {t['reason']}")
        lines.append("\n</details>\n")

    if report["overridden"]:
        lines.append("## Coverage overrides in effect\n")
        for r in report["overridden"]:
            lines.append(f"- {r['stem']}: ratio {r['ratio']:.2f} — {r['override_reason']}")
        lines.append("")

    return "\n".join(lines) + "\n"


def to_jsonable(report):
    def strip(r):
        return {k: v for k, v in r.items() if k != "data"}

    return {
        "total_articles": report["total_articles"],
        "total_truncated": report["total_truncated"],
        "total_toc_missing": report["total_toc_missing"],
        "gaps": report["gaps"],
        "fill": report["fill"],
        "red": [strip(r) for r in report["red"]],
        "yellow": [strip(r) for r in report["yellow"]],
        "green_count": len(report["green"]),
        "overridden": [strip(r) for r in report["overridden"]],
        "file_coverage": {k: (sorted(v) if isinstance(v, set) else v)
                          for k, v in report["coverage"].items()},
    }


def print_issue_detail(stem):
    overrides = load_coverage_overrides()
    r = analyze_issue(stem, overrides)
    r["toc_missing"] = toc_diff(stem, r["data"].get("articles", []))
    print(json.dumps({k: v for k, v in r.items() if k != "data"}, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Validate the Uplink archive and report problems")
    parser.add_argument("--check", action="store_true", help="Exit 1 if any issue is red-flagged")
    parser.add_argument("--issue", help="Print detail for a single issue stem, e.g. 2001_07")
    args = parser.parse_args()

    if args.issue:
        print_issue_detail(args.issue)
        return

    report = run_report()

    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "report.md").write_text(render_markdown(report))
    (REPORTS_DIR / "report.json").write_text(json.dumps(to_jsonable(report), indent=2) + "\n")

    print(f"Issues: {len(report['results'])}, articles: {report['total_articles']}")
    print(f"Coverage: {len(report['green'])} green, {len(report['yellow'])} yellow, "
          f"{len(report['red'])} red, {len(report['overridden'])} overridden")
    print(f"Possibly truncated articles: {report['total_truncated']}")
    print(f"Unexplained schedule gaps: {len(report['gaps'])}")
    print(f"Wrote {REPORTS_DIR / 'report.md'} and {REPORTS_DIR / 'report.json'}")

    if args.check and report["red"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
