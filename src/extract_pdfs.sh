#!/bin/bash

# Batch extract text from PDFs using the `llm` command-line tool and a Gemini model.
#
# Requirements:
#   uv add llm
#   uv run llm keys set gemini <YOUR_API_KEY>
#
# This script:
#   * Iterates over all .pdf files in ./pdfs
#   * Skips ones already extracted into ./gemini_text/<stem>.txt
#   * Uses the specified Gemini model via llm CLI
#   * Writes raw text output
#
# Usage:
#   ./extract_pdfs.sh
#
# Environment variables (optional):
#   GEMINI_MODEL  - override model name (default: gemini/gemini-2.5-pro)
#   PDF_DIR       - override path to PDF directory (default: ./pdfs)
#   OUT_DIR       - override output directory (default: ./gemini_text)
#   FORCE         - if set to "1", re-extract even if output exists

set -euo pipefail

# Configuration
DEFAULT_MODEL="${GEMINI_MODEL:-gemini/gemini-2.5-pro}"
PDF_DIR="${PDF_DIR:-./pdfs}"
OUT_DIR="${OUT_DIR:-./gemini_text}"
FORCE="${FORCE:-0}"
PROMPT="Extract all readable textual content from this PDF. Preserve page order and paragraph breaks. Do not summarize or add commentary."

# Rate limiting delay (seconds)
DELAY=12

# Check if PDF directory exists
if [[ ! -d "$PDF_DIR" ]]; then
    echo "PDF directory not found: $PDF_DIR" >&2
    exit 1
fi

# Check if llm command is available
if ! uv run llm --version &> /dev/null; then
    echo "llm not available via uv. Install with: uv add llm" >&2
    exit 1
fi

# Note: Skipping model validation - assuming model exists
# You can manually verify with: uv run llm models list

# Create output directory
mkdir -p "$OUT_DIR"

# Process each PDF
extracted_count=0
for pdf_file in "$PDF_DIR"/*.pdf; do
    # Check if any PDFs exist
    [[ -f "$pdf_file" ]] || { echo "No PDF files found in $PDF_DIR"; exit 0; }
    
    # Get basename without extension
    basename=$(basename "$pdf_file" .pdf)
    output_file="$OUT_DIR/${basename}.txt"
    
    echo "Processing: $pdf_file"
    
    # Skip if output exists and not forcing
    if [[ -f "$output_file" && "$FORCE" != "1" ]]; then
        echo "[SKIP] $output_file exists"
        continue
    fi
    
    # Extract text using llm
    if uv run llm -m "$DEFAULT_MODEL" "$PROMPT" -a "$pdf_file" > "$output_file" 2>/tmp/llm_error_$; then
        echo "[OK] $(basename "$output_file")"
        extracted_count=$((extracted_count + 1))
        
        # Rate limiting - only sleep after successful extraction
        if [[ $extracted_count -gt 0 ]]; then
            echo "Sleeping ${DELAY}s for rate limiting..."
            sleep "$DELAY"
        fi
    else
        echo "[ERROR] Failed to extract $(basename "$pdf_file")"
        if [[ -s /tmp/llm_error_$$ ]]; then
            echo "Error details:"
            cat /tmp/llm_error_$$
        fi
        rm -f "$output_file"  # Remove empty/partial output file
    fi
    
    # Clean up error file
    rm -f /tmp/llm_error_$$
done

echo "Extraction complete. Processed $extracted_count files."