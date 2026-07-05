"""Shared paths and text-file parsing used across the extraction/report scripts."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = REPO_ROOT / "pdfs"
TEXT_DIR = REPO_ROOT / "text"
ISSUES_DIR = REPO_ROOT / "issues"
WORK_DIR = REPO_ROOT / "work"
DATA_DIR = REPO_ROOT / "data"
REPORTS_DIR = REPO_ROOT / "reports"

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


MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December",
}


def parse_months_field(data):
    """Best-effort parse of an issue's `month` string into a set of month ints."""
    month_field = data.get("month", "")
    if isinstance(month_field, int):
        return {month_field}
    months = set()
    for num, name in MONTH_NAMES.items():
        if name.lower() in str(month_field).lower():
            months.add(num)
    return months
