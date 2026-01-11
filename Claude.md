# Uplink Newsletter Archive

A historical collection of computer-assisted reporting (CAR) publications from 1990-2007, processed with various LLM pipelines for educational and research purposes.

## Repository Structure

```
articles/          # Structured JSON articles (primary training data)
data/              # Metadata/summaries with keywords
pdfs/              # Original PDF sources (366 MB)
text/              # Plain text extractions
markdown/          # Markdown-formatted content
gemini_text/       # Alternative Gemini-based extractions
src/               # Processing scripts
```

## For Claude Code

When working with this repository:
- Primary data is in `/articles/*.json` - use these for content analysis
- Use `/data/*.json` for metadata, summaries, and keywords
- Processing scripts are in `/src/` and root directory
- Python environment uses `uv` with dependencies in `pyproject.toml`

---

# Model Training Guide

This guide walks you through training a language model on the Uplink newsletter collection.

## Training Options Overview

| Approach | VRAM Needed | Training Time | Best For |
|----------|-------------|---------------|----------|
| **QLoRA Fine-tuning** | 8-16 GB | Hours | Most users, local GPU |
| **LoRA Fine-tuning** | 16-24 GB | Hours | Better quality, mid-range |
| **Full Fine-tuning** | 48+ GB | Days | Maximum quality, cloud |
| **Continued Pretraining** | 80+ GB | Days-Weeks | Deep knowledge injection |

## Recommended Models (Python-friendly)

### Qwen Options (Your Preference)

| Model | Parameters | Use Case |
|-------|------------|----------|
| **Qwen2.5-7B-Instruct** | 7B | Best balance of quality/resources |
| **Qwen2.5-3B-Instruct** | 3B | Limited VRAM, faster training |
| **Qwen2.5-14B-Instruct** | 14B | Higher quality, needs more VRAM |
| **Qwen2.5-Coder-7B** | 7B | If focusing on code examples in articles |

### Alternative Options

| Model | Parameters | Why Consider It |
|-------|------------|-----------------|
| **Llama-3.2-3B** | 3B | Excellent small model, MIT license |
| **Llama-3.1-8B** | 8B | Strong baseline, great community |
| **Mistral-7B-v0.3** | 7B | Fast, efficient, Apache 2.0 |
| **Phi-3-medium** | 14B | Microsoft, strong reasoning |
| **Gemma-2-9B** | 9B | Google, good for text understanding |

---

## Phase 1: Data Preparation

### Step 1.1: Audit Your Data

```bash
# Count articles
find articles -name "*.json" -type f | wc -l

# Check total content size
du -sh articles/ text/ data/

# Sample article structure
cat articles/1995_01.json | python -m json.tool | head -50
```

### Step 1.2: Create Training Dataset

Create a script `prepare_training_data.py`:

```python
import json
from pathlib import Path
from typing import Literal

def load_articles(articles_dir: Path = Path("articles")) -> list[dict]:
    """Load all articles from JSON files."""
    articles = []
    for json_file in sorted(articles_dir.glob("*.json")):
        # Skip subdirectories (model-specific outputs)
        if json_file.parent != articles_dir:
            continue
        with open(json_file) as f:
            data = json.load(f)
            for article in data.get("articles", []):
                article["source_file"] = json_file.name
                articles.append(article)
    return articles

def format_for_training(
    articles: list[dict],
    format_type: Literal["completion", "instruction", "chat"] = "instruction"
) -> list[dict]:
    """Convert articles to training format."""

    training_data = []

    for article in articles:
        headline = article.get("headline", "")
        author = article.get("author_name", "Unknown")
        author_title = article.get("author_title", "")
        full_text = article.get("full_text", "")
        year = article.get("year", "")
        month = article.get("month", "")

        if not full_text:
            continue

        if format_type == "completion":
            # Simple completion format
            training_data.append({
                "text": f"# {headline}\n\nBy {author}, {author_title}\n{month} {year}\n\n{full_text}"
            })

        elif format_type == "instruction":
            # Alpaca-style instruction format
            training_data.append({
                "instruction": f"Summarize this computer-assisted reporting article from {month} {year}.",
                "input": full_text,
                "output": f"'{headline}' by {author} ({author_title}) discusses..."  # You'll need actual summaries
            })

        elif format_type == "chat":
            # Chat/conversational format
            training_data.append({
                "messages": [
                    {"role": "system", "content": "You are an expert on computer-assisted reporting and data journalism history."},
                    {"role": "user", "content": f"Tell me about the article '{headline}' from Uplink newsletter."},
                    {"role": "assistant", "content": f"'{headline}' was written by {author}, {author_title}, and published in the {month} {year} issue of Uplink. {full_text[:500]}..."}
                ]
            })

    return training_data

def create_qa_pairs(articles: list[dict]) -> list[dict]:
    """Create question-answer pairs for instruction tuning."""
    qa_pairs = []

    for article in articles:
        headline = article.get("headline", "")
        author = article.get("author_name", "")
        full_text = article.get("full_text", "")
        year = article.get("year", "")
        month = article.get("month", "")

        if not full_text:
            continue

        # Generate various QA formats
        qa_pairs.extend([
            {
                "messages": [
                    {"role": "user", "content": f"What was the main topic of '{headline}' from Uplink?"},
                    {"role": "assistant", "content": f"The article '{headline}' published in {month} {year} by {author} covered: {full_text[:1000]}"}
                ]
            },
            {
                "messages": [
                    {"role": "user", "content": f"Who wrote about {headline.lower()} in computer-assisted reporting?"},
                    {"role": "assistant", "content": f"{author} wrote about this topic in the {month} {year} issue of Uplink newsletter."}
                ]
            }
        ])

    return qa_pairs

if __name__ == "__main__":
    articles = load_articles()
    print(f"Loaded {len(articles)} articles")

    # Create different formats
    completion_data = format_for_training(articles, "completion")
    chat_data = format_for_training(articles, "chat")
    qa_data = create_qa_pairs(articles)

    # Save training data
    Path("training_data").mkdir(exist_ok=True)

    with open("training_data/completion.jsonl", "w") as f:
        for item in completion_data:
            f.write(json.dumps(item) + "\n")

    with open("training_data/chat.jsonl", "w") as f:
        for item in chat_data:
            f.write(json.dumps(item) + "\n")

    with open("training_data/qa_pairs.jsonl", "w") as f:
        for item in qa_data:
            f.write(json.dumps(item) + "\n")

    print(f"Created {len(completion_data)} completion examples")
    print(f"Created {len(chat_data)} chat examples")
    print(f"Created {len(qa_data)} QA pairs")
```

### Step 1.3: Enhance with Existing Metadata

Merge article content with summaries from `/data/`:

```python
def merge_with_metadata(articles_dir: Path, data_dir: Path) -> list[dict]:
    """Combine full articles with their metadata summaries."""
    merged = []

    for articles_file in articles_dir.glob("*.json"):
        data_file = data_dir / articles_file.name

        with open(articles_file) as f:
            articles = json.load(f).get("articles", [])

        metadata = []
        if data_file.exists():
            with open(data_file) as f:
                metadata = json.load(f)
                if isinstance(metadata, dict):
                    metadata = [metadata]

        # Match by headline
        meta_by_headline = {m.get("headline", "").lower(): m for m in metadata}

        for article in articles:
            headline = article.get("headline", "").lower()
            if headline in meta_by_headline:
                article["summary"] = meta_by_headline[headline].get("summary", "")
                article["keywords"] = meta_by_headline[headline].get("keywords", [])
            merged.append(article)

    return merged
```

---

## Phase 2: Environment Setup

### Option A: Local Training with Unsloth (Recommended for Qwen)

```bash
# Create environment
uv venv training-env
source training-env/bin/activate

# Install unsloth (optimized for consumer GPUs)
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps trl peft accelerate bitsandbytes

# Or with conda
conda create -n training python=3.11
conda activate training
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

### Option B: Standard Transformers + PEFT

```bash
pip install torch transformers datasets peft trl accelerate bitsandbytes
pip install wandb  # For experiment tracking (optional)
```

### Option C: Axolotl (Config-driven Training)

```bash
git clone https://github.com/OpenAccess-AI-Collective/axolotl
cd axolotl
pip install packaging ninja
pip install -e '.[flash-attn,deepspeed]'
```

### Option D: LLaMA-Factory (GUI + CLI)

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

---

## Phase 3: Training

### Method 1: QLoRA with Unsloth (Fastest, Qwen-optimized)

Create `train_qwen_unsloth.py`:

```python
from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import load_dataset
import torch

# Configuration
MODEL_NAME = "unsloth/Qwen2.5-7B-Instruct-bnb-4bit"  # Pre-quantized
MAX_SEQ_LENGTH = 4096
LOAD_IN_4BIT = True

# Load model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL_NAME,
    max_seq_length=MAX_SEQ_LENGTH,
    dtype=None,  # Auto-detect
    load_in_4bit=LOAD_IN_4BIT,
)

# Add LoRA adapters
model = FastLanguageModel.get_peft_model(
    model,
    r=16,  # LoRA rank
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=42,
)

# Load your data
dataset = load_dataset("json", data_files="training_data/chat.jsonl", split="train")

# Format for Qwen chat template
def format_prompts(examples):
    texts = []
    for messages in examples["messages"]:
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
        texts.append(text)
    return {"text": texts}

dataset = dataset.map(format_prompts, batched=True)

# Training
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=MAX_SEQ_LENGTH,
    dataset_num_proc=2,
    packing=True,  # Pack short sequences together
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=10,
        num_train_epochs=3,
        learning_rate=2e-4,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=10,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=42,
        output_dir="outputs/qwen-uplink",
        save_strategy="epoch",
    ),
)

trainer.train()

# Save
model.save_pretrained("outputs/qwen-uplink-final")
tokenizer.save_pretrained("outputs/qwen-uplink-final")

# Optional: Merge LoRA weights and save full model
model.save_pretrained_merged("outputs/qwen-uplink-merged", tokenizer, save_method="merged_16bit")

# Optional: Export to GGUF for llama.cpp / Ollama
model.save_pretrained_gguf("outputs/qwen-uplink-gguf", tokenizer, quantization_method="q4_k_m")
```

### Method 2: Standard Transformers + PEFT

Create `train_standard.py`:

```python
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
from datasets import load_dataset

# Model selection
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"  # Or your preferred model

# Quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

# Load model
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

# Prepare for training
model = prepare_model_for_kbit_training(model)

# LoRA config
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Load dataset
dataset = load_dataset("json", data_files="training_data/chat.jsonl", split="train")

# Training
training_args = TrainingArguments(
    output_dir="outputs/qwen-uplink-standard",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    weight_decay=0.01,
    warmup_ratio=0.03,
    logging_steps=10,
    save_strategy="epoch",
    bf16=True,
    gradient_checkpointing=True,
    optim="paged_adamw_8bit",
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    tokenizer=tokenizer,
    args=training_args,
    max_seq_length=4096,
)

trainer.train()
trainer.save_model()
```

### Method 3: Axolotl Config

Create `axolotl_config.yaml`:

```yaml
base_model: Qwen/Qwen2.5-7B-Instruct
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer
trust_remote_code: true

load_in_8bit: false
load_in_4bit: true
strict: false

datasets:
  - path: training_data/chat.jsonl
    type: sharegpt
    conversation: chatml

dataset_prepared_path: prepared_data
val_set_size: 0.05
output_dir: outputs/qwen-axolotl

adapter: qlora
lora_r: 16
lora_alpha: 32
lora_dropout: 0.05
lora_target_modules:
  - q_proj
  - k_proj
  - v_proj
  - o_proj
  - gate_proj
  - up_proj
  - down_proj

sequence_len: 4096
sample_packing: true
pad_to_sequence_len: true

wandb_project: uplink-training
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 3
optimizer: paged_adamw_8bit
lr_scheduler: cosine
learning_rate: 2e-4

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 10
xformers_attention:
flash_attention: true

warmup_ratio: 0.03
evals_per_epoch: 2
saves_per_epoch: 1
debug:
deepspeed:
weight_decay: 0.01
special_tokens:
```

Run with: `accelerate launch -m axolotl.cli.train axolotl_config.yaml`

---

## Phase 4: Evaluation

### Basic Evaluation Script

Create `evaluate_model.py`:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

def load_trained_model(base_model: str, adapter_path: str):
    """Load base model with trained LoRA adapter."""
    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(model, adapter_path)
    return model, tokenizer

def test_model(model, tokenizer, test_prompts: list[str]):
    """Generate responses for test prompts."""
    model.eval()

    for prompt in test_prompts:
        messages = [{"role": "user", "content": prompt}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                do_sample=True,
            )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Prompt: {prompt}\n")
        print(f"Response: {response}\n")
        print("-" * 50)

# Test prompts specific to Uplink content
test_prompts = [
    "What is computer-assisted reporting?",
    "Tell me about early data journalism techniques from the 1990s.",
    "Who were notable figures in computer-assisted reporting?",
    "What topics were covered in Uplink newsletter?",
    "Explain how journalists used databases in the early 1990s.",
]

if __name__ == "__main__":
    model, tokenizer = load_trained_model(
        "Qwen/Qwen2.5-7B-Instruct",
        "outputs/qwen-uplink-final"
    )
    test_model(model, tokenizer, test_prompts)
```

---

## Phase 5: Deployment

### Option 1: Local with Ollama

```bash
# Convert to GGUF (if using Unsloth, already done)
# Or use llama.cpp convert script

# Create Modelfile
cat > Modelfile << 'EOF'
FROM ./outputs/qwen-uplink-gguf/qwen-uplink-q4_k_m.gguf

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""

PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.7

SYSTEM "You are an expert on computer-assisted reporting and data journalism history, trained on the Uplink newsletter archive (1990-2007)."
EOF

# Create and run
ollama create uplink-expert -f Modelfile
ollama run uplink-expert
```

### Option 2: vLLM Server

```bash
pip install vllm

# Serve the model
python -m vllm.entrypoints.openai.api_server \
    --model outputs/qwen-uplink-merged \
    --port 8000
```

### Option 3: Hugging Face Hub

```python
from huggingface_hub import HfApi

api = HfApi()
api.upload_folder(
    folder_path="outputs/qwen-uplink-final",
    repo_id="your-username/qwen-uplink-expert",
    repo_type="model",
)
```

---

## Hardware Requirements

| Method | Minimum VRAM | Recommended | Training Time* |
|--------|--------------|-------------|----------------|
| QLoRA (4-bit) | 8 GB | 12 GB | 2-4 hours |
| LoRA (8-bit) | 16 GB | 24 GB | 3-6 hours |
| Full Fine-tune | 48 GB | 80 GB | 8-24 hours |

*Estimates for ~500 articles, 3 epochs, batch size 2

### Cloud Options

| Provider | GPU | Cost/hr | Best For |
|----------|-----|---------|----------|
| **RunPod** | RTX 4090 | ~$0.74 | QLoRA training |
| **Lambda Labs** | A100 40GB | ~$1.29 | Larger models |
| **Vast.ai** | Various | $0.20+ | Budget option |
| **Google Colab Pro** | A100 | $10/mo | Experimentation |

---

## Troubleshooting

### Common Issues

1. **CUDA Out of Memory**
   - Reduce batch size
   - Enable gradient checkpointing
   - Use 4-bit quantization
   - Reduce max sequence length

2. **Slow Training**
   - Enable flash attention
   - Use sequence packing
   - Increase batch size if VRAM allows

3. **Poor Results**
   - Increase training epochs
   - Adjust learning rate (try 1e-4 to 3e-4)
   - Improve data quality/formatting
   - Add more diverse training examples

4. **Model Not Learning Domain Knowledge**
   - Consider continued pretraining first
   - Create more QA pairs from content
   - Use RAG instead for retrieval tasks

---

---

# Hybrid Approach: RAG + Fine-tuning for History Writing & Exploration

This section covers the recommended approach for:
1. **Writing a history of data journalism** (1990-2007) - your primary use case
2. **Public exploration** - letting others search and discover the archive

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Your Workflow                            │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  RAG Search  │───▶│ Fine-tuned   │───▶│   History    │      │
│  │  (Research)  │    │ Model (Write)│    │   Document   │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     Public Interface                            │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Web App    │───▶│  RAG + LLM   │───▶│   Answers    │      │
│  │  (Explore)   │    │  (Retrieve)  │    │ + Citations  │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

## Step 1: Build the RAG System

### 1.1 Install Dependencies

```bash
# Add to pyproject.toml or install directly
uv add chromadb sentence-transformers langchain langchain-community

# Or with pip
pip install chromadb sentence-transformers langchain langchain-community
```

### 1.2 Create the Vector Store

Create `build_vectorstore.py`:

```python
import json
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

def load_all_articles(articles_dir: Path = Path("articles")) -> list[Document]:
    """Load articles as LangChain Documents with metadata."""
    documents = []

    for json_file in sorted(articles_dir.glob("*.json")):
        # Skip model-specific subdirectories
        if json_file.parent != articles_dir:
            continue

        with open(json_file) as f:
            data = json.load(f)

        for article in data.get("articles", []):
            # Skip empty articles
            if not article.get("full_text"):
                continue

            # Create document with rich metadata
            doc = Document(
                page_content=article["full_text"],
                metadata={
                    "headline": article.get("headline", ""),
                    "author": article.get("author_name", "Unknown"),
                    "author_title": article.get("author_title", ""),
                    "year": article.get("year", 0),
                    "month": article.get("month", ""),
                    "source_file": json_file.name,
                    # Create a citation string
                    "citation": f"{article.get('author_name', 'Unknown')}, "
                               f"\"{article.get('headline', 'Untitled')},\" "
                               f"Uplink, {article.get('month', '')} {article.get('year', '')}."
                }
            )
            documents.append(doc)

    return documents

def build_vectorstore(
    documents: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    persist_directory: str = "vectorstore"
) -> Chroma:
    """Build and persist a Chroma vector store."""

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    splits = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(splits)} chunks")

    # Use a good embedding model
    # Options: all-MiniLM-L6-v2 (fast), all-mpnet-base-v2 (better),
    #          BAAI/bge-base-en-v1.5 (best for retrieval)
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5",
        model_kwargs={"device": "cuda"},  # or "cpu"
        encode_kwargs={"normalize_embeddings": True}
    )

    # Build vector store
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory,
    )

    print(f"Created vector store with {vectorstore._collection.count()} vectors")
    return vectorstore

if __name__ == "__main__":
    print("Loading articles...")
    documents = load_all_articles()
    print(f"Loaded {len(documents)} articles")

    print("Building vector store...")
    vectorstore = build_vectorstore(documents)
    print("Done! Vector store saved to ./vectorstore")
```

### 1.3 Create the RAG Query System

Create `rag_query.py`:

```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
import ollama  # Or use any LLM client

class UplinkRAG:
    def __init__(
        self,
        persist_directory: str = "vectorstore",
        model_name: str = "qwen2.5:7b"  # Your Ollama model
    ):
        # Load embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-base-en-v1.5",
            model_kwargs={"device": "cuda"},
            encode_kwargs={"normalize_embeddings": True}
        )

        # Load vector store
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )

        self.model_name = model_name

        # Prompt for RAG responses
        self.rag_prompt = """You are an expert on the history of computer-assisted reporting
and data journalism, with access to the Uplink newsletter archive (1990-2007).

Use the following retrieved context to answer the question. Always cite your sources
using the provided citation information. If you don't know the answer based on the
context, say so.

Context:
{context}

Question: {question}

Answer (include citations):"""

    def search(
        self,
        query: str,
        k: int = 5,
        filter_year: int | None = None,
        filter_author: str | None = None
    ) -> list[Document]:
        """Search the archive with optional filters."""

        # Build filter
        where_filter = {}
        if filter_year:
            where_filter["year"] = filter_year
        if filter_author:
            where_filter["author"] = {"$contains": filter_author}

        # Search
        results = self.vectorstore.similarity_search(
            query,
            k=k,
            filter=where_filter if where_filter else None
        )

        return results

    def query(self, question: str, k: int = 5) -> dict:
        """Answer a question using RAG."""

        # Retrieve relevant documents
        docs = self.search(question, k=k)

        # Format context with citations
        context_parts = []
        citations = []
        for i, doc in enumerate(docs, 1):
            context_parts.append(
                f"[{i}] {doc.page_content}\n"
                f"Source: {doc.metadata.get('citation', 'Unknown')}"
            )
            citations.append({
                "id": i,
                "citation": doc.metadata.get("citation", ""),
                "headline": doc.metadata.get("headline", ""),
                "year": doc.metadata.get("year", ""),
                "author": doc.metadata.get("author", "")
            })

        context = "\n\n".join(context_parts)

        # Generate response
        prompt = self.rag_prompt.format(context=context, question=question)

        response = ollama.generate(
            model=self.model_name,
            prompt=prompt
        )

        return {
            "answer": response["response"],
            "sources": citations,
            "retrieved_docs": len(docs)
        }

    def find_articles_by_topic(self, topic: str, k: int = 10) -> list[dict]:
        """Find articles related to a topic (for research)."""
        docs = self.search(topic, k=k)

        # Deduplicate by headline
        seen = set()
        articles = []
        for doc in docs:
            headline = doc.metadata.get("headline", "")
            if headline not in seen:
                seen.add(headline)
                articles.append({
                    "headline": headline,
                    "author": doc.metadata.get("author", ""),
                    "year": doc.metadata.get("year", ""),
                    "month": doc.metadata.get("month", ""),
                    "citation": doc.metadata.get("citation", ""),
                    "excerpt": doc.page_content[:500] + "..."
                })

        return articles

    def timeline_search(self, topic: str) -> dict[int, list[dict]]:
        """Search for a topic and organize results by year (for history writing)."""
        docs = self.search(topic, k=20)

        by_year = {}
        for doc in docs:
            year = doc.metadata.get("year", 0)
            if year not in by_year:
                by_year[year] = []
            by_year[year].append({
                "headline": doc.metadata.get("headline", ""),
                "author": doc.metadata.get("author", ""),
                "excerpt": doc.page_content[:300]
            })

        return dict(sorted(by_year.items()))


# Example usage
if __name__ == "__main__":
    rag = UplinkRAG()

    # Simple query
    result = rag.query("How did journalists use spreadsheets in the early 1990s?")
    print("Answer:", result["answer"])
    print("\nSources:")
    for src in result["sources"]:
        print(f"  [{src['id']}] {src['citation']}")

    # Research mode - find articles
    print("\n--- Articles about election coverage ---")
    articles = rag.find_articles_by_topic("election coverage data")
    for a in articles[:5]:
        print(f"  • {a['headline']} ({a['year']}) - {a['author']}")

    # Timeline for history writing
    print("\n--- Timeline: Database reporting ---")
    timeline = rag.timeline_search("database reporting investigation")
    for year, items in timeline.items():
        print(f"\n{year}:")
        for item in items:
            print(f"  • {item['headline']}")
```

---

## Step 2: Build the Public Web Interface

### 2.1 Simple Gradio Interface

Create `app_gradio.py`:

```python
import gradio as gr
from rag_query import UplinkRAG

rag = UplinkRAG()

def search_archive(query: str, num_results: int = 5) -> str:
    """Search the archive and return formatted results."""
    result = rag.query(query, k=num_results)

    output = f"## Answer\n\n{result['answer']}\n\n"
    output += "## Sources\n\n"

    for src in result["sources"]:
        output += f"- **{src['headline']}** ({src['year']}) by {src['author']}\n"

    return output

def browse_by_topic(topic: str) -> str:
    """Browse articles by topic."""
    articles = rag.find_articles_by_topic(topic, k=10)

    output = f"## Articles about: {topic}\n\n"
    for a in articles:
        output += f"### {a['headline']}\n"
        output += f"*{a['author']}, {a['month']} {a['year']}*\n\n"
        output += f"{a['excerpt']}\n\n---\n\n"

    return output

def timeline_view(topic: str) -> str:
    """View topic evolution over time."""
    timeline = rag.timeline_search(topic)

    output = f"## Timeline: {topic}\n\n"
    for year, items in timeline.items():
        output += f"### {year}\n"
        for item in items:
            output += f"- **{item['headline']}** - {item['author']}\n"
        output += "\n"

    return output

# Build interface
with gr.Blocks(title="Uplink Archive Explorer") as demo:
    gr.Markdown("""
    # Uplink Newsletter Archive (1990-2007)

    Explore 17 years of computer-assisted reporting history from the
    IRE's Uplink newsletter.
    """)

    with gr.Tab("Ask a Question"):
        query_input = gr.Textbox(
            label="Your Question",
            placeholder="How did journalists use databases in the 1990s?"
        )
        num_results = gr.Slider(1, 10, value=5, step=1, label="Number of sources")
        query_btn = gr.Button("Search")
        query_output = gr.Markdown()
        query_btn.click(search_archive, [query_input, num_results], query_output)

    with gr.Tab("Browse by Topic"):
        topic_input = gr.Textbox(
            label="Topic",
            placeholder="election data, census, FOIA, spreadsheets..."
        )
        browse_btn = gr.Button("Find Articles")
        browse_output = gr.Markdown()
        browse_btn.click(browse_by_topic, topic_input, browse_output)

    with gr.Tab("Timeline View"):
        timeline_input = gr.Textbox(
            label="Topic to trace through time",
            placeholder="internet, web scraping, GIS mapping..."
        )
        timeline_btn = gr.Button("Show Timeline")
        timeline_output = gr.Markdown()
        timeline_btn.click(timeline_view, timeline_input, timeline_output)

if __name__ == "__main__":
    demo.launch(share=True)  # share=True creates public link
```

### 2.2 FastAPI Backend (for custom frontends)

Create `app_api.py`:

```python
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_query import UplinkRAG

app = FastAPI(title="Uplink Archive API")

# Enable CORS for web frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = UplinkRAG()

class QueryRequest(BaseModel):
    question: str
    num_sources: int = 5

class SearchResult(BaseModel):
    answer: str
    sources: list[dict]

@app.post("/query", response_model=SearchResult)
def query_archive(request: QueryRequest):
    """Answer a question about the archive."""
    result = rag.query(request.question, k=request.num_sources)
    return SearchResult(answer=result["answer"], sources=result["sources"])

@app.get("/search")
def search_articles(
    q: str = Query(..., description="Search query"),
    limit: int = Query(10, le=50),
    year: int | None = Query(None, description="Filter by year")
):
    """Search for articles matching a query."""
    return rag.find_articles_by_topic(q, k=limit)

@app.get("/timeline/{topic}")
def get_timeline(topic: str):
    """Get topic evolution over time."""
    return rag.timeline_search(topic)

@app.get("/years")
def get_available_years():
    """Get list of years in the archive."""
    return {"years": list(range(1990, 2008))}

# Run with: uvicorn app_api:app --reload
```

---

## Step 3: Fine-tune for History Writing (Optional Enhancement)

Fine-tuning helps when you want the model to:
- Write in a style consistent with journalism history
- Synthesize information across multiple sources
- Understand CAR-specific terminology deeply

### 3.1 Create History-Writing Training Data

Create `prepare_history_training.py`:

```python
import json
from pathlib import Path

def create_synthesis_examples(articles: list[dict]) -> list[dict]:
    """Create examples that teach the model to synthesize information."""

    # Group articles by topic/theme
    by_year = {}
    for article in articles:
        year = article.get("year", 0)
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(article)

    training_data = []

    # Create year-summary examples
    for year, year_articles in by_year.items():
        if len(year_articles) < 2:
            continue

        # Combine article summaries
        article_list = "\n".join([
            f"- \"{a.get('headline', '')}\" by {a.get('author_name', '')}"
            for a in year_articles[:5]
        ])

        training_data.append({
            "messages": [
                {
                    "role": "system",
                    "content": "You are a journalism historian writing about the evolution of computer-assisted reporting."
                },
                {
                    "role": "user",
                    "content": f"Summarize the key themes in computer-assisted reporting from {year} based on these Uplink articles:\n{article_list}"
                },
                {
                    "role": "assistant",
                    "content": f"In {year}, computer-assisted reporting practitioners focused on several key areas..."
                    # You would fill this in with actual summaries
                }
            ]
        })

    return training_data

def create_narrative_examples(articles: list[dict]) -> list[dict]:
    """Create examples that teach historical narrative writing."""

    training_data = []

    # Teach the model to write historical narratives
    training_data.append({
        "messages": [
            {
                "role": "system",
                "content": "You are a journalism historian. Write engaging historical narratives about the development of data journalism."
            },
            {
                "role": "user",
                "content": "Write an introduction to a chapter about how journalists first started using spreadsheets for investigations."
            },
            {
                "role": "assistant",
                "content": """Before the spreadsheet transformed newsrooms, investigative journalists faced a daunting task: making sense of thousands of records by hand. The arrival of Lotus 1-2-3, and later Microsoft Excel, didn't just speed up calculations—it fundamentally changed what stories were possible.

In the pages of Uplink, we can trace this transformation through the experiences of reporters who were there..."""
            }
        ]
    })

    return training_data
```

### 3.2 Workflow for Writing Your History

```
┌─────────────────────────────────────────────────────────────────┐
│                    History Writing Workflow                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. RESEARCH PHASE (RAG)                                        │
│     └─▶ Use timeline_search() to find coverage of a topic      │
│     └─▶ Use find_articles_by_topic() for deep dives            │
│     └─▶ Export citations for your bibliography                  │
│                                                                 │
│  2. SYNTHESIS PHASE (Fine-tuned model OR Claude/GPT)            │
│     └─▶ Feed retrieved articles to model                        │
│     └─▶ Ask for summaries, themes, turning points               │
│     └─▶ Generate draft narrative sections                       │
│                                                                 │
│  3. WRITING PHASE (Your work + AI assistance)                   │
│     └─▶ Use model to suggest connections                        │
│     └─▶ Fact-check against RAG system                           │
│     └─▶ Maintain your voice and editorial judgment              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Research Assistant Script

Create `research_assistant.py`:

```python
from rag_query import UplinkRAG
import json

class HistoryResearchAssistant:
    def __init__(self):
        self.rag = UplinkRAG()
        self.research_notes = []

    def research_topic(self, topic: str) -> dict:
        """Comprehensive research on a topic for history writing."""

        # Get timeline
        timeline = self.rag.timeline_search(topic)

        # Get detailed articles
        articles = self.rag.find_articles_by_topic(topic, k=15)

        # Get AI synthesis
        synthesis = self.rag.query(
            f"Trace the evolution of {topic} in computer-assisted reporting "
            f"from 1990 to 2007. What were the key developments and turning points?",
            k=10
        )

        research = {
            "topic": topic,
            "timeline": timeline,
            "key_articles": articles,
            "synthesis": synthesis["answer"],
            "sources": synthesis["sources"]
        }

        self.research_notes.append(research)
        return research

    def find_key_figures(self, topic: str) -> list[str]:
        """Find journalists who wrote about a topic."""
        articles = self.rag.find_articles_by_topic(topic, k=20)
        authors = {}
        for a in articles:
            author = a.get("author", "Unknown")
            if author not in authors:
                authors[author] = []
            authors[author].append(a.get("headline", ""))

        # Sort by number of articles
        return sorted(authors.items(), key=lambda x: len(x[1]), reverse=True)

    def export_bibliography(self, filename: str = "bibliography.json"):
        """Export all sources used in research."""
        all_sources = []
        for note in self.research_notes:
            all_sources.extend(note.get("sources", []))

        # Deduplicate
        seen = set()
        unique = []
        for src in all_sources:
            citation = src.get("citation", "")
            if citation not in seen:
                seen.add(citation)
                unique.append(src)

        with open(filename, "w") as f:
            json.dump(unique, f, indent=2)

        print(f"Exported {len(unique)} sources to {filename}")

    def chapter_outline(self, theme: str) -> str:
        """Generate a chapter outline for a theme."""
        timeline = self.rag.timeline_search(theme)

        outline = f"# Chapter: {theme.title()} in Computer-Assisted Reporting\n\n"

        # Group into eras
        early_90s = {y: v for y, v in timeline.items() if 1990 <= y <= 1994}
        mid_90s = {y: v for y, v in timeline.items() if 1995 <= y <= 1999}
        early_00s = {y: v for y, v in timeline.items() if 2000 <= y <= 2007}

        if early_90s:
            outline += "## The Early Days (1990-1994)\n"
            for year, items in early_90s.items():
                for item in items[:2]:
                    outline += f"- {item['headline']} ({year})\n"
            outline += "\n"

        if mid_90s:
            outline += "## Growth and Adoption (1995-1999)\n"
            for year, items in mid_90s.items():
                for item in items[:2]:
                    outline += f"- {item['headline']} ({year})\n"
            outline += "\n"

        if early_00s:
            outline += "## Maturation (2000-2007)\n"
            for year, items in early_00s.items():
                for item in items[:2]:
                    outline += f"- {item['headline']} ({year})\n"

        return outline


# Example usage
if __name__ == "__main__":
    assistant = HistoryResearchAssistant()

    # Research topics for your history
    topics = [
        "spreadsheet analysis",
        "database reporting",
        "FOIA requests",
        "mapping and GIS",
        "internet and web",
        "election coverage",
        "census data"
    ]

    for topic in topics:
        print(f"\n{'='*50}")
        print(f"Researching: {topic}")
        print('='*50)
        research = assistant.research_topic(topic)
        print(f"Found {len(research['key_articles'])} articles")
        print(f"Spans years: {list(research['timeline'].keys())}")

    # Export bibliography
    assistant.export_bibliography()

    # Generate chapter outline
    print("\n" + assistant.chapter_outline("database reporting"))
```

---

## Step 4: Deployment Options

### For Personal Use (History Writing)
```bash
# Just run locally
python research_assistant.py
python rag_query.py
```

### For Public Exploration

| Option | Effort | Cost | Best For |
|--------|--------|------|----------|
| **Gradio + HF Spaces** | Low | Free | Quick demo |
| **Streamlit Cloud** | Low | Free | Simple apps |
| **FastAPI + Vercel** | Medium | Free tier | API-first |
| **Docker + Fly.io** | Medium | ~$5/mo | Full control |
| **Static site + API** | Higher | Varies | Custom UX |

### Deploy to Hugging Face Spaces (Easiest)

```bash
# Install
pip install huggingface_hub

# Login
huggingface-cli login

# Create and upload
huggingface-cli repo create uplink-explorer --type space --space-sdk gradio
git clone https://huggingface.co/spaces/YOUR_USERNAME/uplink-explorer
cp app_gradio.py uplink-explorer/app.py
cp -r vectorstore uplink-explorer/
cd uplink-explorer
git add . && git commit -m "Initial deploy" && git push
```

---

## Recommended Implementation Order

1. **Week 1: Build RAG foundation**
   - Run `build_vectorstore.py` to index all articles
   - Test with `rag_query.py`
   - Start using for your research immediately

2. **Week 2: Create exploration interface**
   - Build Gradio app for others to explore
   - Deploy to Hugging Face Spaces
   - Get feedback from beta users

3. **Week 3+: Optional fine-tuning**
   - Only if RAG + base model isn't sufficient
   - Focus on synthesis and narrative writing
   - Train on examples that teach historical writing style

4. **Ongoing: Write your history**
   - Use research assistant for each chapter
   - Let RAG system cite sources
   - Build bibliography automatically
