# MCQ-genration
LLM-based MCQ generation from 3GPP technical specifications using semantic chunking, cross-chunk retrieval, and automated QA/critique.


# SpecMCQ: LLM-Based MCQ Generation from 3GPP Specifications

An LLM-based framework for automatically generating high-quality, reasoning-oriented multiple-choice questions (MCQs) from technical specifications such as 3GPP documents.

The system combines structure-aware semantic chunking, embedding-based cross-chunk retrieval, local LLM inference, and iterative MCQ refinement to generate specification-grounded questions.

## Overview

Technical specifications such as 3GPP documents contain large amounts of highly structured and domain-specific information. Creating high-quality examination questions manually from these documents is time-consuming.

SpecMCQ automates this process by:

1. Loading technical specification documents converted to Markdown.
2. Splitting documents using structure-aware semantic chunking.
3. Generating semantic embeddings for document segments.
4. Identifying important topics and test points.
5. Generating reasoning-oriented MCQs using an LLM.
6. Performing a self-answer/QA step.
7. Critiquing the generated question using an MCQ quality rubric.
8. Refining the question based on the critique.
9. Optionally retrieving semantically related chunks to provide additional context.

## Pipeline

```text
3GPP Specification
        │
        ▼
Document Loading
        │
        ▼
Structure-Aware Chunking
        │
        ▼
Sentence Embeddings
        │
        ├───────────────┐
        │               │
        ▼               ▼
Topic/Test-Point    Cross-Chunk
Identification      Retrieval
        │               │
        └───────┬───────┘
                ▼
        MCQ Generation
                │
                ▼
             Self-QA
                │
                ▼
             Critique
                │
                ▼
             Refinement
                │
                ▼
        Final MCQ Database
```

## Key Features

### Structure-Aware Semantic Chunking

The system combines document structure with semantic similarity to create meaningful chunks instead of relying only on fixed-size text splitting.

The chunking process preserves document-source metadata and uses sentence embeddings to determine whether neighboring sections should be merged.

### Cross-Chunk Retrieval

The cross-chunk implementation computes embeddings for all chunks and retrieves the most semantically similar chunks for a given source chunk.

This allows the question-generation model to use related information that may be distributed across different sections of the specification.

### Reasoning-Oriented MCQs

The generator is designed to avoid simple definition-based questions.

Questions are encouraged to test:

* Component behavior
* Interface responsibilities
* Cause-and-effect relationships
* Control-loop behavior
* Fault and anomaly reasoning
* KPI/performance degradation
* Specification-driven behavior

### MCQ Refinement

The generation pipeline follows an iterative process:

```text
Topic Identification
        ↓
Initial MCQ Generation
        ↓
Model Self-QA
        ↓
Expert Critique
        ↓
MCQ Correction
        ↓
Final MCQ
```

The generated MCQ contains:

* Context
* Question
* Four answer options
* Correct answer
* Topics
* Test points
* QA feedback
* Critique information

## Models and Technologies

* Python
* PyTorch
* Sentence Transformers
* LangChain
* Ollama
* DeepSeek
* NumPy
* JSON/JSONL
* Concurrent processing

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/SpecMCQ.git
cd SpecMCQ
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## LLM Configuration

This project supports local LLM inference through Ollama.

Install Ollama and make sure the required model is available:

```bash
ollama pull deepseek-r1:32b
```

Create a `.env` file:

```env
OLLAMA_NODES=http://localhost:11434/api/generate
LOCAL_LLM_MODEL=deepseek-r1:32b
```

For multiple Ollama servers, configure multiple comma-separated endpoints:

```env
OLLAMA_NODES=http://localhost:11434/api/generate,http://localhost:11435/api/generate
```

Do not commit your `.env` file.

## Input Documents

The system expects technical documents converted to Markdown.

Example:

```text
data/
├── specification_1.md
├── specification_2.md
└── specification_3.md
```

The documents are processed independently before chunking and MCQ generation.

## Running the Generator

Place the Markdown specification files in the configured input directory and run:

```bash
python src/mcq_generation.py
```

For cross-chunk semantic retrieval:

```bash
python src/mcq_crosschunk.py
```

Generated questions can be stored in JSONL format for further processing.

Example:

```json
{
  "question": "...",
  "options": [
    "A. ...",
    "B. ...",
    "C. ...",
    "D. ..."
  ],
  "correct_answer": "B. ..."
}
```

## Example Question Characteristics

The framework aims to generate questions where:

* The answer depends on the specification content.
* Multiple concepts must be connected.
* Distractors are plausible.
* The question cannot be reliably answered from generic domain knowledge alone.
* The question requires reasoning rather than simple memorization.

## Project Structure

```text
SpecMCQ/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── src/
│   ├── mcq_generation.py
│   └── mcq_crosschunk.py
├── data/
│   └── README.md
├── outputs/
│   └── README.md
└── examples/
    └── sample_mcq.json
```

## Research Motivation

The project explores the use of LLMs for automatically creating high-quality assessment material from complex telecommunications specifications.

The primary focus is on improving:

* Question quality
* Specification grounding
* Reasoning difficulty
* Context selection
* Distractor quality
* MCQ reliability

## Disclaimer

This project is an independent research/software project.

3GPP specifications and related standards are the property of their respective organizations and contributors. Users should obtain and use specification documents according to the applicable terms and licenses.

## Author

**Abdulla Ovais**

Graduate Researcher
Indian Institute of Technology Hyderabad
