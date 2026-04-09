#!/usr/bin/env python3
"""
Extract text from PDFs page-by-page using the llm Python API.

Splits each PDF into individual pages, extracts text from each page separately
via a multimodal LLM, and concatenates the results. This avoids output
truncation that happens when sending entire multi-page PDFs.

Usage:
    uv run python src/extract_pdf_pages.py 2006_07 2006_11
    uv run python src/extract_pdf_pages.py --missing
    uv run python src/extract_pdf_pages.py --missing --dry-run
"""

import argparse
import os
import sys
import tempfile

import llm
import pypdf

PDF_DIR = "pdfs"
OUT_DIR = "text"
MODEL = "claude-sonnet-4-6"
PROMPT = (
    "Extract all readable textual content from this PDF page. "
    "Preserve paragraph breaks and formatting. "
    "Do not summarize or add commentary."
)


def split_pdf_page(pdf_path, page_num, output_path):
    """Extract a single page from a PDF into a new PDF file."""
    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages[page_num])
    with open(output_path, "wb") as f:
        writer.write(f)


def extract_page_text(page_pdf_path, model):
    """Send a single-page PDF to the LLM and get text back."""
    attachment = llm.Attachment(path=page_pdf_path)
    response = model.prompt(PROMPT, attachments=[attachment])
    return response.text()


def extract_pdf(stem, model, dry_run=False, force=False):
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
            page_pdf = os.path.join(tmpdir, f"page_{i}.pdf")
            split_pdf_page(pdf_path, i, page_pdf)

            print(f"  Extracting page {i + 1}/{num_pages}...", end=" ", flush=True)
            text = extract_page_text(page_pdf, model)

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


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDFs page-by-page")
    parser.add_argument("stems", nargs="*", help="PDF stems to process (e.g., 2006_07 2006_11)")
    parser.add_argument("--missing", action="store_true", help="Process all PDFs that lack a text/ file")
    parser.add_argument("--dry-run", action="store_true", help="Preview without extracting")
    parser.add_argument("--force", action="store_true", help="Overwrite existing text files")
    parser.add_argument("--model", default=MODEL, help=f"LLM model to use (default: {MODEL})")
    args = parser.parse_args()

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
        extract_pdf(stem, model, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()
