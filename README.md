# Uplink

An archive of **Uplink**, the newsletter of the National Institute for Computer-Assisted Reporting (NICAR), published from October 1990 through March 2007. The archive contains 145 issues and 662 articles covering the early history of computer-assisted reporting in American journalism.

## Repository structure

```
pdfs/       Original PDF scans of each newsletter issue
text/       Extracted plain text (one file per issue)
issues/     Structured JSON (one file per issue, containing all articles)
src/        Processing scripts
docs/       Static site generator
```

## Issue JSON schema

Each file in `issues/` follows this format:

```json
{
  "year": 1990,
  "month": "October",
  "articles": [
    {
      "headline": "Ghostbusting in East St. Louis",
      "author_name": "George Landau",
      "author_title": "Computer-assisted reporting specialist for the St. Louis Post-Dispatch",
      "full_text": "A man named Admiral Wherry...",
      "summary": "George Landau and Tim Novak investigated voter fraud...",
      "keywords": ["voter fraud", "East St. Louis", "computer-assisted reporting"]
    }
  ]
}
```

## Pipeline

The processing pipeline has three steps, all using the [llm](https://llm.datasette.io/) Python library with Anthropic models:

1. **Extract text from PDFs** (`src/extract_pdf_pages.py`): Splits each PDF into individual pages and extracts text page-by-page to avoid LLM output truncation.

2. **Extract articles from text** (`src/convert_to_json.py`): Sends extracted text to an LLM that identifies individual articles, merges text that continues across pages, and returns structured JSON with full text, summaries, and keywords.

3. **Backfill missing summaries** (`src/summarize_unmatched.py`): Finds articles in `issues/` that lack a summary or keywords and generates them.

### Running the pipeline

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/):

```bash
# Install dependencies
uv sync

# Configure your Anthropic API key for the llm library
uv run llm keys set anthropic

# Extract text from PDFs (only processes missing files)
uv run python src/extract_pdf_pages.py --missing

# Generate issue JSON from text (skips existing files with adequate content)
uv run python src/convert_to_json.py claude-sonnet-4.6 --skip-existing

# Backfill any missing summaries
uv run python src/summarize_unmatched.py
```

### Building the site

```bash
cd docs
npm install
npm run build
```

Output is written to `docs/build/`.

## Utility scripts

- `src/migrate.py` — One-time migration script used to consolidate the original separate article and summary JSON files into the unified `issues/` format.
- `src/consolidate_text.py` — One-time script used to fill gaps in `text/` from alternate extraction sources.
