import os
import json
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
    
    args = parser.parse_args()
    
    # If user wants to list models, do that and exit
    if args.list_models:
        print("Available models:")
        for model in llm.get_models():
            print(f"  - {model.model_id}")
        return
    
    print(f"Using model: {args.model}")
    
    for filename in os.listdir("text"):
        if filename.endswith(".txt"):
            print(f"Processing {filename}")
            with open(f"articles/{filename.replace('.txt', '.json')}", 'w') as file:
                articles = combine_stories(filename, args.model)
                json.dump(articles, file, indent=4)
    

if __name__ == "__main__":
    main()