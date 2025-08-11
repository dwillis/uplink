#!/bin/bash

# Process extracted text files to create individual markdown articles
#
# Requirements:
#   uv add llm
#   uv run llm keys set gemini <YOUR_API_KEY>
#
# This script:
#   * Iterates over all .txt files in ./gemini_text and ./articles
#   * Uses Gemini to identify and separate distinct articles
#   * Creates markdown files with format: yyyy_mm_slug_version_of_title.md
#   * Skips files already processed unless FORCE=1
#
# Usage:
#   ./process_articles.sh
#
# Environment variables (optional):
#   GEMINI_MODEL     - override model name (default: gemini/gemini-2.5-pro)
#   GEMINI_TEXT_DIR  - override gemini_text directory (default: ./gemini_text)
#   ARTICLES_DIR     - override articles directory (default: ./articles)
#   OUT_DIR          - override output directory (default: ./articles)
#   FORCE            - if set to "1", re-process even if output exists

set -euo pipefail

# Configuration
DEFAULT_MODEL="${GEMINI_MODEL:-gemini/gemini-2.5-pro}"
GEMINI_TEXT_DIR="${GEMINI_TEXT_DIR:-./gemini_text}"
ARTICLES_DIR="${ARTICLES_DIR:-./articles}"
OUT_DIR="${OUT_DIR:-./articles}" # Output directory for processed markdown articles
FORCE="${FORCE:-0}"

# Rate limiting delay (seconds)
DELAY=12

PROMPT="Analyze this text and identify each distinct article. For each article found, provide:

1. A suggested slug-friendly title (lowercase, hyphens instead of spaces, no special characters)
2. The complete article text in markdown format
3. Any publication date mentioned in the text

Format your response as follows for each article:
---ARTICLE-START---
TITLE_SLUG: suggested-title-slug
DATE: yyyy_mm (if found, otherwise use 'unknown')
CONTENT:
[Full article content in markdown]
---ARTICLE-END---

If multiple articles are in the text, separate each with the above format. Preserve all article content including headers, bylines, and body text."

# Check if uv and llm are available
if ! uv run llm --version &> /dev/null; then
    echo "Error: 'llm' not available via 'uv'. Install with: uv add llm" >&2
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUT_DIR"

# Function to create slug from filename
create_base_slug() {
    local filename="$1"
    # Remove extension, convert to lowercase, replace non-alphanumeric with hyphens,
    # collapse multiple hyphens, and remove leading/trailing hyphens.
    echo "$filename" | sed 's/\.[^.]*$//' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g' | sed 's/^-\|-$//g'
}

# Function to process a single text file
process_text_file() {
    local input_file="$1"
    local base_filename=$(basename "$input_file")
    local base_slug=$(create_base_slug "$base_filename")
    
    echo "Processing: $input_file"
    
    # Create a temporary file for the LLM response
    local temp_response="/tmp/llm_response_$(date +%s%N)_$$" # Unique temp file name
    local temp_error="/tmp/llm_error_$(date +%s%N)_$$"       # Unique temp error file name
    
    # Call LLM to analyze the text
    # The 'set -e' will cause the script to exit if uv run llm fails.
    # We capture stderr to a temp file for debugging.
    if ! uv run llm -m "$DEFAULT_MODEL" "$PROMPT" < "$input_file" > "$temp_response" 2>"$temp_error"; then
        echo "[ERROR] Failed to process $base_filename with LLM." >&2
        if [[ -s "$temp_error" ]]; then
            echo "Error details from LLM:" >&2
            cat "$temp_error" >&2
        else
            echo "No specific error details captured from LLM stderr." >&2
        fi
        rm -f "$temp_response" "$temp_error"
        return 1 # Indicate failure
    fi
    
    # Parse the response and create individual markdown files
    local article_count=0
    local current_title_slug=""
    local current_date=""
    local current_content=""
    local in_content=false
    
    # Read the LLM response line by line
    while IFS= read -r line; do
        if [[ "$line" == "---ARTICLE-START---" ]]; then
            # Reset variables for a new article
            current_title_slug=""
            current_date=""
            current_content=""
            in_content=false
            article_count=$((article_count + 1))
        elif [[ "$line" == "---ARTICLE-END---" ]]; then
            # Save the current article if title and content are present
            if [[ -n "$current_title_slug" && -n "$current_content" ]]; then
                local output_filename
                # Determine output filename based on date or base slug
                if [[ "$current_date" != "unknown" && -n "$current_date" ]]; then
                    output_filename="${current_date}_${current_title_slug}.md"
                else
                    # Fallback if no date or 'unknown' date
                    output_filename="${base_slug}_${current_title_slug}.md"
                fi
                
                local output_path="$OUT_DIR/$output_filename"
                
                # Check if file exists and FORCE is not enabled
                if [[ -f "$output_path" && "$FORCE" != "1" ]]; then
                    echo "[SKIP] $output_filename already exists. Use FORCE=1 to re-process."
                else
                    # Write content to the markdown file
                    echo "$current_content" > "$output_path"
                    echo "[OK] Created $output_filename"
                fi
            else
                echo "[WARN] Skipping an article from $base_filename due to missing title slug or content." >&2
            fi
            in_content=false
        elif [[ "$line" =~ ^TITLE_SLUG:[[:space:]]*(.+)$ ]]; then
            current_title_slug="${BASH_REMATCH[1]// /}"  # Capture slug and remove any spaces
        elif [[ "$line" =~ ^DATE:[[:space:]]*(.+)$ ]]; then
            current_date="${BASH_REMATCH[1]// /}"      # Capture date and remove any spaces
        elif [[ "$line" == "CONTENT:" ]]; then
            in_content=true # Start capturing content
        elif [[ "$in_content" == true ]]; then
            # Append line to current_content, adding a newline if content already exists
            if [[ -n "$current_content" ]]; then
                current_content="$current_content"$'\n'"$line"
            else
                current_content="$line"
            fi
        fi
    done < "$temp_response"
    
    if [[ $article_count -eq 0 ]]; then
        echo "[WARN] No articles found in $base_filename based on LLM response format."
    else
        echo "[INFO] Successfully processed $article_count articles from $base_filename."
    fi
    
    # Clean up temporary files
    rm -f "$temp_response" "$temp_error"
    
    return 0 # Indicate success
}

# Main processing loop
processed_count=0
total_files=0

# Iterate through both specified input directories
for dir in "$GEMINI_TEXT_DIR" "$ARTICLES_DIR"; do
    if [[ -d "$dir" ]]; then
        # Find all .txt files in the current directory
        # Using a glob, which expands to nothing if no files match,
        # so we need to check if $txt_file is actually a file.
        for txt_file in "$dir"/*.txt; do
            # Skip if no files matched the glob (e.g., directory is empty of .txt files)
            [[ -f "$txt_file" ]] || continue
            
            total_files=$((total_files + 1))
            
            # Process the file and check its return status
            if process_text_file "$txt_file"; then
                processed_count=$((processed_count + 1))
                
                # Apply rate limiting delay after each successful file processing
                echo "Sleeping ${DELAY}s for rate limiting..."
                sleep "$DELAY"
            else
                echo "[CRITICAL] Script will terminate due to error processing $txt_file (set -e)." >&2
                # Since set -e is active, the script will exit here.
                # The 'return 1' in process_text_file triggers this.
            fi
        done
    else
        echo "[WARN] Input directory not found: $dir. Skipping." >&2
    fi
done

if [[ $total_files -eq 0 ]]; then
    echo "No .txt files found in $GEMINI_TEXT_DIR or $ARTICLES_DIR to process."
    exit 0
fi

echo "Processing complete. Successfully processed $processed_count of $total_files files."