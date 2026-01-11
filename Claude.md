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

## Alternative: RAG Instead of Fine-tuning

For some use cases, RAG (Retrieval-Augmented Generation) may be better than fine-tuning:

```python
# Simple RAG setup with the articles
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# This may be more effective for question-answering about specific articles
# while fine-tuning is better for adopting the style/knowledge generally
```

Consider RAG when:
- You need precise retrieval of specific articles
- You want to cite sources
- Your content changes frequently
- You have limited compute resources
