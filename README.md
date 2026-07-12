# Uplink

An archive of **Uplink**, the newsletter of the National Institute for Computer-Assisted Reporting (NICAR), published from October 1990 through March 2007: 145 issues and roughly 1,838 articles, each with headline, full text, byline, affiliation, summary, keywords, topics, and technologies mentioned. Run `uv run python src/report.py` for current, exact numbers and any outstanding data-quality issues (`reports/report.md` is checked in and updated on each run).

## Repository structure

```
pdfs/       Original PDF scans of each newsletter issue
text/       Extracted plain text (one file per issue)
issues/     Structured JSON (one file per issue, containing all articles)
src/        Processing scripts
docs/       Static site generator
data/       Shared reference data (topic taxonomy, technology vocabulary, schedule notes)
reports/    Generated validation report (reports/report.md, checked in)
work/       Intermediate re-extraction artifacts (gitignored, safe to delete)
```

## Issue JSON schema (v2)

Each file in `issues/` follows this format:

```json
{
  "schema_version": 2,
  "year": 1990,
  "month": "October",
  "articles": [
    {
      "headline": "Ghostbusting in East St. Louis",
      "kicker": "",
      "author_name": "George Landau",
      "author_title": "Computer-assisted reporting specialist",
      "affiliation": "St. Louis Post-Dispatch",
      "full_text": "A man named Admiral Wherry...",
      "summary": "George Landau and Tim Novak investigated voter fraud...",
      "keywords": ["voter fraud", "East St. Louis", "computer-assisted reporting"],
      "topics": ["Crime & Justice", "Investigative Methods"],
      "technologies": ["Access"],
      "provenance": {"extracted_by": "anthropic/claude-sonnet-4-6", "extracted_at": "2026-07-05", "verified": true}
    }
  ]
}
```

`author_title` is a job title only; `affiliation` is the publication or organization. All 145 issues are on schema v2 as of this pipeline rework; `src/report.py` and the site build also tolerate the older v1 shape (no `schema_version`, `author_title` sometimes holding an affiliation, no `topics`/`technologies`) in case of future partial re-extraction.

## Pipeline

All scripts use the [llm](https://llm.datasette.io/) Python library. Anthropic models are the default; any script's `--model` flag also accepts a local Ollama model name (see "Running against local models" below).

1. **Extract text from PDFs** (`src/extract_pdf_pages.py`): Splits each PDF into individual pages and extracts text page-by-page to avoid LLM output truncation.

2. **Re-extract articles per issue** (`src/extract_articles.py`): Two-stage extraction that replaces the old single-call approach, which silently truncated output on long issues:
   - **Stage A (inventory)**: one small-output call per issue enumerates every article, its byline, and first/last words -- the response is a manifest, not full text, so it can't truncate.
   - **Stage B (extract)**: one call per article reconstructs that article's complete text from its own slice of the issue, verified against the inventory's first/last-word anchors.
   - **Assemble**: merges Stage A + B output into `issues/{stem}.json`, preserving existing `summary`/`keywords` for articles matched by headline.

3. **Backfill missing summaries** (`src/summarize_unmatched.py`): Finds articles that lack a summary or keywords and generates them.

4. **Enrich metadata** (`src/extract_metadata.py`): Splits `affiliation` from `author_title`, and assigns `topics` (from the shared taxonomy in `data/taxonomy.json`) and `technologies` (era-specific software/hardware/formats).

5. **Validate** (`src/report.py`): Cross-checks `pdfs/` / `text/` / `issues/` coverage, estimates how much of each issue's text made it into the JSON, flags likely truncation, checks the publication schedule for gaps, and reports metadata fill rates. Re-run after any pipeline step; `reports/report.md` is checked in so `git diff` shows progress.

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

# Re-extract issues flagged red/yellow in the report (or --all, or explicit stems)
uv run python src/extract_articles.py --from-report

# Backfill any missing summaries for newly recovered articles
uv run python src/summarize_unmatched.py

# Enrich with affiliation/topics/technologies
uv run python src/extract_metadata.py

# Re-check
uv run python src/report.py --check
```

### Running against local models

Install the optional dependency group once: `uv sync --group local` (adds `llm-ollama`, `pypdfium2`, `pillow`). Every script above accepts `--model <name>` with any locally pulled Ollama model, e.g. `--model qwen3.5:35b` for text stages (extraction, metadata) -- no code changes needed, since `llm.get_model()` resolves either provider.

Ollama vision models are useful specifically for page-image work, not the text stages above:
- `uv run python src/report.py --vision-spotcheck 5 --vision-model qwen2.5vl` -- re-OCRs random pages locally and reports how much they drift from the stored text, as a free sanity check on the original OCR pass.
- `uv run python src/extract_pdf_pages.py 2001_07 --pages 3,7 --images --model qwen3-vl:8b --merge` -- re-OCRs specific suspect pages and splices the result back into `text/{stem}.txt`. Splicing requires that file to already have `Page N` markers; most don't (see "Data quality"), so without `--merge` this just prints the re-extracted text.

Expect local vision models to underperform Claude on these dense two-column 1990s-2000s scans -- use them for spot-checks and gap-filling, not as the default OCR path.

### Building the site

```bash
cd docs
npm install
npm run build
```

Output is written to `docs/build/`. The build prefers `topics`/`affiliation`/`technologies` from `issues/*.json` when present, falling back to keyword-based topic assignment for not-yet-enriched articles.

## Data quality

Run `uv run python src/report.py` for current numbers. As of this pipeline rework, most `text/*.txt` files came from an earlier alternate OCR pass and don't retain page markers, so per-page provenance is only available for issues re-extracted with the current `extract_pdf_pages.py`. Known suspect gaps in the publication schedule (not yet confirmed as genuinely unpublished) are listed in the report; confirmed non-publications go in `data/schedule_notes.json`.

## Utility scripts

- `src/migrate.py` — One-time migration script used to consolidate the original separate article and summary JSON files into the unified `issues/` format.
- `src/consolidate_text.py` — One-time script used to fill gaps in `text/` from alternate extraction sources.
- `src/clean.py` — Flattens `issues/*.json` into a single-file format (`issues/cleaned_stories.json`, gitignored) for an external "Beat Book" pipeline: `uv run python src/clean.py issues/`.
