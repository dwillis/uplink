#!/usr/bin/env python3
"""
Process extracted text files into structured issue JSON using the llm library.

Reads text from text/*.txt, uses an LLM to extract and reconstruct complete
articles (merging page continuations), and writes normalized JSON to issues/.

Each output file follows the unified schema:
{
    "year": 1990,
    "month": "October",
    "articles": [
        {
            "headline": "...",
            "author_name": "...",
            "author_title": "...",
            "full_text": "...",
            "summary": "...",
            "keywords": ["...", "...", "..."]
        }
    ]
}

Usage:
    uv run python src/convert_to_json.py claude-sonnet-4-6
    uv run python src/convert_to_json.py claude-sonnet-4-6 --skip-existing
    uv run python src/convert_to_json.py --list-models
    uv run python src/convert_to_json.py claude-sonnet-4-6 --test 3
"""

import argparse
import json
import os

import llm

TEXT_DIR = "text"
OUTPUT_DIR = "issues"

SYSTEM_PROMPT = """\
You are tasked with extracting and reconstructing complete articles from a text \
file that may contain multiple stories. Some articles may be split across \
different sections of the file (e.g., "Story continues on page X" or similar \
indicators).

PROCESS:
1. Read through the entire text file to identify all articles and their components
2. For each article, reconstruct the complete, continuous text by following any \
continuation markers or jumps
3. Create one entry per complete article (not per fragment)

IMPORTANT:
- Combine all fragments of an article into a single "full_text" field
- Do not create separate entries for article fragments
- Include the complete article text, not summaries
- Extract year as integer if available, month as string if available
- If author information is not available, leave those fields as empty strings
- For each article, also provide a 1-2 sentence "summary" and exactly 3 "keywords"\
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "year": {"type": "integer", "description": "Publication year of the issue"},
        "month": {"type": "string", "description": "Publication month of the issue"},
        "articles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "headline": {"type": "string", "description": "Article headline"},
                    "author_name": {"type": "string", "description": "Author name"},
                    "author_title": {"type": "string", "description": "Author title/affiliation"},
                    "full_text": {"type": "string", "description": "Complete article text"},
                    "summary": {"type": "string", "description": "1-2 sentence summary"},
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Exactly 3 keywords",
                    },
                },
                "required": ["headline", "full_text", "summary", "keywords"],
            },
        },
    },
    "required": ["year", "month", "articles"],
}


def process_file(filename, model_name):
    """Extract articles from a text file using the LLM."""
    with open(os.path.join(TEXT_DIR, filename)) as f:
        text = f.read()

    model = llm.get_model(model_name)
    response = model.prompt(text, system=SYSTEM_PROMPT, schema=SCHEMA)
    return json.loads(response.text())


def main():
    parser = argparse.ArgumentParser(description="Process text files into issue JSON using LLM")
    parser.add_argument("model", nargs="?", help="Model to use (e.g., claude-sonnet-4-6)")
    parser.add_argument("--list-models", action="store_true", help="List available models and exit")
    parser.add_argument("--test", type=int, default=0, help="Process only the first N files")
    parser.add_argument("--output-dir", default=OUTPUT_DIR, help=f"Output directory (default: {OUTPUT_DIR})")
    parser.add_argument("--skip-existing", action="store_true", help="Skip files where output already exists with adequate content")
    parser.add_argument("--min-fulltext", type=int, default=1000, help="Minimum avg full_text length to consider adequate (default: 1000)")

    args = parser.parse_args()

    if args.list_models:
        print("Available models:")
        for model in llm.get_models():
            print(f"  - {model.model_id}")
        return

    if not args.model:
        parser.error("model is required (unless using --list-models)")

    print(f"Using model: {args.model}")
    print(f"Output directory: {args.output_dir}")
    os.makedirs(args.output_dir, exist_ok=True)

    text_files = sorted(fn for fn in os.listdir(TEXT_DIR) if fn.endswith(".txt"))
    if args.test > 0:
        text_files = text_files[: args.test]
        print(f"Test mode: processing first {len(text_files)} file(s)")

    for filename in text_files:
        out_path = os.path.join(args.output_dir, filename.replace(".txt", ".json"))

        if args.skip_existing and os.path.exists(out_path):
            try:
                existing = json.load(open(out_path))
                items = existing.get("articles", [])
                if items:
                    avg_len = sum(len(a.get("full_text", "")) for a in items) / len(items)
                    if avg_len >= args.min_fulltext:
                        print(f"Skipping {filename} (avg full_text {avg_len:.0f} chars >= {args.min_fulltext})")
                        continue
                    else:
                        print(f"Re-processing {filename} (avg full_text {avg_len:.0f} chars < {args.min_fulltext})")
            except Exception:
                pass

        try:
            print(f"Processing {filename}")
            result = process_file(filename, args.model)
            with open(out_path, "w") as f:
                json.dump(result, f, indent=2)
                f.write("\n")
            n = len(result.get("articles", []))
            print(f"  -> wrote {n} article(s) to {out_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    main()
