import os
import json
import time
import argparse
import llm

def combine_stories(filename, model_name):
    with open(f"text/{filename}", 'r') as file:
        text = file.read()
        try:
            # Use the specified model
            model = llm.get_model(model_name)
            
            # Create the system prompt
            system_prompt = """You are tasked with extracting and reconstructing complete articles from a text file that may contain multiple stories. Some articles may be split across different sections of the file (e.g., "Story continues on page X" or similar indicators).

PROCESS:
1. First, carefully read through the entire text file to identify all articles and their components
2. For each article, reconstruct the complete, continuous text by following any continuation markers or jumps
3. Create one entry per complete article (not per fragment)

IMPORTANT:
- Combine all fragments of an article into a single "full_text" field
- Do not create separate entries for article fragments
- Include the complete article text, not summaries
- Extract year as integer if available, month as string if available
- If author information is not available, leave those fields as null"""
            
            # Use direct JSON schema for articles
            schema = {
                "type": "object",
                "properties": {
                    "articles": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "year": {"type": "integer", "title": "Year", "description": "Publication year"},
                                "month": {"type": "string", "title": "Month", "description": "Publication month"},
                                "headline": {"type": "string", "title": "Headline", "description": "Article headline"},
                                "author_name": {"type": "string", "title": "Author Name", "description": "Author name"},
                                "author_title": {"type": "string", "title": "Author Title", "description": "Author title"},
                                "full_text": {"type": "string", "title": "Full Text", "description": "Complete article text"}
                            },
                            "required": ["headline", "full_text"],
                            "title": "Article"
                        }
                    }
                },
                "required": ["articles"],
                "title": "ArticleCollection"
            }
            
            # Generate response using schema parameter
            response = model.prompt(
                text,
                system=system_prompt,
                schema=schema
            )
            
            # Parse the response text as JSON and return
            return json.loads(response.text())
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            raise e

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Process text files using LLM to extract articles')
    parser.add_argument('model', help='Model to use (e.g., gpt-4o, claude-3-sonnet, gpt-3.5-turbo)')
    parser.add_argument('--list-models', action='store_true', help='List available models and exit')
    parser.add_argument('--test', type=int, default=0, help='Quick test: process only the first N .txt files')
    parser.add_argument('--output-dir', default='articles/original', help='Output directory for JSON files (default: articles/original)')
    parser.add_argument('--skip-existing', action='store_true', help='Skip files where output already exists with adequate full text (>= --min-fulltext chars per article)')
    parser.add_argument('--min-fulltext', type=int, default=1000, help='Minimum avg full_text length to consider an existing file adequate (default: 1000)')

    args = parser.parse_args()

    # If user wants to list models, do that and exit
    if args.list_models:
        print("Available models:")
        for model in llm.get_models():
            print(f"  - {model.model_id}")
        return

    print(f"Using model: {args.model}")
    print(f"Output directory: {args.output_dir}")
    os.makedirs(args.output_dir, exist_ok=True)

    # Gather text files and optionally limit for testing
    text_files = [fn for fn in sorted(os.listdir("text")) if fn.endswith('.txt')]
    if args.test and args.test > 0:
        text_files = text_files[:args.test]
        print(f"Test mode: processing first {len(text_files)} text file(s)")

    for filename in text_files:
        out_path = os.path.join(args.output_dir, filename.replace('.txt', '.json'))

        if args.skip_existing and os.path.exists(out_path):
            try:
                existing = json.load(open(out_path))
                ARRAY_KEYS = ['articles', 'stories', 'news_stories', 'newsletter', 'content', 'data']
                items = existing if isinstance(existing, list) else next(
                    (existing[k] for k in ARRAY_KEYS if k in existing and isinstance(existing[k], list)), []
                )
                if items:
                    avg_len = sum(len(a.get('full_text') or '') for a in items) / len(items)
                    if avg_len >= args.min_fulltext:
                        print(f"Skipping {filename} (existing avg full_text {avg_len:.0f} chars >= {args.min_fulltext})")
                        continue
                    else:
                        print(f"Re-processing {filename} (existing avg full_text {avg_len:.0f} chars < {args.min_fulltext})")
            except Exception:
                pass  # Can't read existing file; re-process it

        try:
            print(f"Processing {filename}")
            articles = combine_stories(filename, args.model)
            with open(out_path, 'w') as file:
                json.dump(articles, file, indent=4)
            if isinstance(articles, dict) and 'articles' in articles:
                print(f"  -> wrote {len(articles['articles'])} article(s) to {out_path}")
            else:
                print(f"  -> wrote output to {out_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    

if __name__ == "__main__":
    main()