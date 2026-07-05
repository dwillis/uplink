#!/usr/bin/env python3
"""
Extract text from PDFs page-by-page using the llm Python API.

Splits each PDF into individual pages, extracts text from each page separately
via a multimodal LLM, and concatenates the results. This avoids output
truncation that happens when sending entire multi-page PDFs.

Anthropic models can take a single-page PDF attachment directly. Local
Ollama vision models generally can't, so --images renders each page to a
PNG instead (via pypdfium2, an optional dependency: `uv sync --group local`).

Usage:
    uv run python src/extract_pdf_pages.py 2006_07 2006_11
    uv run python src/extract_pdf_pages.py --missing
    uv run python src/extract_pdf_pages.py --missing --dry-run

    # Re-OCR specific suspect pages with a local vision model and splice
    # the result back into the existing text/{stem}.txt (requires that file
    # to already have "Page N" markers -- most don't; see README):
    uv run python src/extract_pdf_pages.py 2001_07 --pages 3,7 --images --model qwen3-vl:8b --merge
"""

import argparse
import os
import sys
import tempfile

import llm
import pypdf

sys.path.insert(0, os.path.dirname(__file__))
from pipeline_common import parse_text_pages  # noqa: E402

PDF_DIR = "pdfs"
OUT_DIR = "text"
MODEL = "anthropic/claude-sonnet-4-6"
PROMPT = (
    "Extract all readable textual content from this PDF page. "
    "Preserve paragraph breaks and formatting. "
    "Do not summarize or add commentary."
)


def split_pdf_page(pdf_path, page_num, output_path):
    """Extract a single page from a PDF into a new single-page PDF file."""
    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages[page_num])
    with open(output_path, "wb") as f:
        writer.write(f)


def render_page_png(pdf_path, page_num, output_path, dpi=200):
    """Render a single PDF page to a PNG, for vision models that can't take PDF attachments."""
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[page_num]
    scale = dpi / 72
    bitmap = page.render(scale=scale)
    image = bitmap.to_pil()
    image.save(output_path)


def extract_page_text(page_path, model):
    """Send a single-page PDF or PNG to the LLM and get text back."""
    attachment = llm.Attachment(path=page_path)
    response = model.prompt(PROMPT, attachments=[attachment])
    return response.text()


def extract_one_page(pdf_path, page_num, model, images, tmpdir):
    """Extract text from a single 0-indexed page, as a PDF or PNG attachment."""
    if images:
        page_path = os.path.join(tmpdir, f"page_{page_num}.png")
        render_page_png(pdf_path, page_num, page_path)
    else:
        page_path = os.path.join(tmpdir, f"page_{page_num}.pdf")
        split_pdf_page(pdf_path, page_num, page_path)
    return extract_page_text(page_path, model)


def extract_pdf(stem, model, dry_run=False, force=False, images=False):
    """Extract all pages from a PDF into a single text file."""
    pdf_path = os.path.join(PDF_DIR, f"{stem}.pdf")
    out_path = os.path.join(OUT_DIR, f"{stem}.txt")

    if not os.path.exists(pdf_path):
        print(f"[SKIP] {pdf_path} not found")
        return False

    if os.path.exists(out_path) and not force:
        print(f"[SKIP] {out_path} already exists (use --force to overwrite)")
        return False

    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(f"[START] {stem}.pdf ({num_pages} pages)")

    if dry_run:
        print(f"  Would extract {num_pages} pages to {out_path}")
        return True

    all_text = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for i in range(num_pages):
            print(f"  Extracting page {i + 1}/{num_pages}...", end=" ", flush=True)
            text = extract_one_page(pdf_path, i, model, images, tmpdir)

            if text.strip():
                all_text.append(f"Page {i + 1}\n\n{text.strip()}")
                print(f"({len(text)} chars)")
            else:
                print("(empty)")

    full_text = "\n\n---\n\n".join(all_text)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(full_text)

    print(f"[DONE] {out_path} ({len(full_text)} chars, {num_pages} pages)")
    return True


def reextract_pages(stem, page_nums, model, images=False, merge=False):
    """Re-OCR specific 1-indexed pages (e.g. suspected of poor OCR) and
    optionally splice the result back into text/{stem}.txt.

    Splicing requires the existing text file to already have "Page N" /
    "---" markers -- most text/ files in this archive don't (see README),
    so without --merge this just prints the freshly extracted text.
    """
    pdf_path = os.path.join(PDF_DIR, f"{stem}.pdf")
    if not os.path.exists(pdf_path):
        print(f"[SKIP] {pdf_path} not found")
        return

    results = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        for page_num in page_nums:
            print(f"  Re-extracting page {page_num}...", end=" ", flush=True)
            text = extract_one_page(pdf_path, page_num - 1, model, images, tmpdir)
            results[page_num] = text.strip()
            print(f"({len(text)} chars)")

    if not merge:
        for page_num, text in results.items():
            print(f"\n--- Page {page_num} ---\n{text}\n")
        return

    existing_pages = parse_text_pages(stem)
    if len(existing_pages) < 2:
        print(f"[ERROR] text/{stem}.txt has no 'Page N' markers to splice into; "
              f"rerun with --force (no --pages) to regenerate the whole file instead.")
        return

    for page_num, text in results.items():
        if page_num < 1 or page_num > len(existing_pages):
            print(f"[SKIP] page {page_num} out of range (file has {len(existing_pages)} pages)")
            continue
        existing_pages[page_num - 1] = text

    full_text = "\n\n---\n\n".join(f"Page {i + 1}\n\n{p}" for i, p in enumerate(existing_pages))
    out_path = os.path.join(OUT_DIR, f"{stem}.txt")
    with open(out_path, "w") as f:
        f.write(full_text)
    print(f"[MERGED] {out_path} updated ({len(page_nums)} page(s) replaced)")


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDFs page-by-page")
    parser.add_argument("stems", nargs="*", help="PDF stems to process (e.g., 2006_07 2006_11)")
    parser.add_argument("--missing", action="store_true", help="Process all PDFs that lack a text/ file")
    parser.add_argument("--dry-run", action="store_true", help="Preview without extracting")
    parser.add_argument("--force", action="store_true", help="Overwrite existing text files")
    parser.add_argument("--model", default=MODEL, help=f"LLM model to use (default: {MODEL})")
    parser.add_argument("--images", action="store_true",
                         help="Render pages to PNG instead of single-page PDF attachments "
                              "(needed for local vision models via llm-ollama; requires pypdfium2)")
    parser.add_argument("--pages", help="Comma-separated 1-indexed page numbers to re-extract, "
                                         "e.g. --pages 3,7 (requires exactly one stem)")
    parser.add_argument("--merge", action="store_true",
                         help="With --pages, splice re-extracted pages back into the existing text file")
    args = parser.parse_args()

    if args.pages:
        if len(args.stems) != 1:
            parser.error("--pages requires exactly one stem")
        model = llm.get_model(args.model)
        page_nums = [int(p) for p in args.pages.split(",")]
        reextract_pages(args.stems[0], page_nums, model, images=args.images, merge=args.merge)
        return

    if args.missing:
        stems = []
        for f in sorted(os.listdir(PDF_DIR)):
            if f.endswith(".pdf"):
                stem = f[:-4]
                text_path = os.path.join(OUT_DIR, f"{stem}.txt")
                if not os.path.exists(text_path):
                    stems.append(stem)
        print(f"Found {len(stems)} PDFs without text/ files")
    elif args.stems:
        stems = args.stems
    else:
        parser.print_help()
        return

    model = llm.get_model(args.model)

    for stem in stems:
        extract_pdf(stem, model, dry_run=args.dry_run, force=args.force, images=args.images)


if __name__ == "__main__":
    main()
