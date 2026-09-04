import os
import json
import re
import requests
import time
import torch
import numpy as np
#import google.generativeai as genai
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
from langchain_community.document_loaders import (
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
)
from langchain.schema import Document
from concurrent.futures import ThreadPoolExecutor, as_completed

import itertools  # ✅ NEW: for round-robin node selection

# --- Device info ---
print("CUDA available:", torch.cuda.is_available())
print("Using device:", torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# --- Configuration ---
load_dotenv()
MODE = "generate_only"  # Options: "generate_only", "validate_only", "generate_and_validate"
USE_LOCAL_LLM = True

# ✅ NEW: Multi-node Ollama config (similar to your KG code)
OLLAMA_NODES = [
    "http://10.9.64.22:11434/api/generate",
    "http://192.168.50.140:11434/api/generate",
    
]



# OLLAMA_NODES = [
#     "http://127.0.0.1:11440/api/generate",
#     "http://127.0.0.1:11441/api/generate",
#     "http://127.0.0.1:11442/api/generate",
#     "http://127.0.0.1:11443/api/generate",
   # "http://127.0.0.1:11444/api/generate",
   # "http://127.0.0.1:11445/api/generate",
   # "http://127.0.0.1:11446/api/generate",
   # "http://127.0.0.1:11447/api/generate",
# ] 




LOCAL_LLM_MODEL = "deepseek-r1:32b"
LOCAL_LLM_URL = OLLAMA_NODES[0]  # kept for backward compatibility; not used directly

# ✅ NEW: round-robin node iterator
node_cycle = itertools.cycle(OLLAMA_NODES)

PROCESSED_FILES_PATH = "processed_files.json"
COMPLETED_FILES_PATH = "completed_files.json"  # ✅ NEW: track fully completed files

# --- Processed / Completed files tracking ---
def load_processed_files():
    if os.path.exists(PROCESSED_FILES_PATH):
        with open(PROCESSED_FILES_PATH, "r") as f:
            return set(json.load(f))
    return set()

def save_processed_file(filename):
    processed = load_processed_files()
    processed.add(filename)
    with open(PROCESSED_FILES_PATH, "w") as f:
        json.dump(list(processed), f, indent=2)

# ✅ NEW
def load_completed_files():
    if os.path.exists(COMPLETED_FILES_PATH):
        with open(COMPLETED_FILES_PATH, "r") as f:
            return set(json.load(f))
    return set()

# ✅ NEW
def save_completed_file(filename):
    completed = load_completed_files()
    completed.add(filename)
    with open(COMPLETED_FILES_PATH, "w") as f:
        json.dump(list(completed), f, indent=2)

# --- LLM Query Functions ---
def query_gemini_llm(prompt):
    response = model.generate_content(prompt)
    return response.text

# ✅ UPDATED: now takes endpoint (for multi-node)
def query_local_llm(prompt, endpoint):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": LOCAL_LLM_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": 8192},
    }
    response = requests.post(endpoint, headers=headers, json=payload, timeout=300)
    if response.status_code == 200:
        return response.json().get("response", "[ERROR] No valid response.")
    else:
        raise RuntimeError(f"[ERROR {response.status_code}] {response.text}")

# ✅ UPDATED: uses round-robin over OLLAMA_NODES, with retries
def make_llm_call(prompt, retries=3, delay=5):
    """
    Wrapper for all LLM calls.
    - If USE_LOCAL_LLM = False → use Gemini (as before, with retries)
    - If USE_LOCAL_LLM = True  → use multi-node Ollama in round-robin
    """
    if not USE_LOCAL_LLM:
        # Original Gemini path with retry
        for attempt in range(retries):
            try:
                return query_gemini_llm(prompt)
            except Exception as e:
                print(f"Gemini LLM call failed: {e}")
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    return None

    # Local multi-node Ollama path
    for attempt in range(retries):
        endpoint = next(node_cycle)
        try:
            print(f"🧠 Using Ollama node: {endpoint}")
            return query_local_llm(prompt, endpoint)
        except Exception as e:
            print(f"⚠️ LLM call failed on node {endpoint}: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return None

def append_mcq_to_file(mcq, filename="mcq_database6.jsonl"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(mcq) + "\n")

# --- Configure Gemini if needed ---
if not USE_LOCAL_LLM:
    try:
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print(f"Error configuring Google AI: {e}")
        exit()

# --- Document Loading ---
def load_single_md_file(md_file_path):
    """Loads plain Markdown (.md) text files as LangChain Document objects."""
    documents = []
    try:
        with open(md_file_path, "r", encoding="utf-8") as f:
            md_text = f.read().strip()
            if md_text:
                documents.append(Document(page_content=md_text, metadata={"source": md_file_path}))
                print(f" Loaded Markdown file: {md_file_path}")
            else:
                print(f" Empty Markdown file: {md_file_path}")
    except FileNotFoundError:
        print(f" File not found: {md_file_path}")
    except Exception as e:
        print(f" Error reading Markdown file {md_file_path}: {e}")
    return documents


# ---  Updated Structure-Aware Dynamic Chunking ---
def dynamic_chunk_documents(documents,
                            base_chunk_size=6000,
                            max_chunk_size=10000,
                            similarity_threshold=0.4,
                            model_name="all-MiniLM-L6-v2",
                            overlap_segments=1,
                            print_stats=True):
    """
    Advanced dynamic chunking for Markdown documents.
    NOW processes each Document (file) separately and
    PRESERVES metadata["source"] on each output chunk.
    Advanced dynamic chunking for Markdown documents.
    Combines structure awareness + semantic similarity + adaptive merging
    """

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f" Using device: {device}")

    def structural_split(md_text):
        pattern = (
            r'(?=^# |\n# |\n## |\n### |!\[\]\(images/|<table|'
            r'> \*Image Summary:|> \*Table Summary:)'
        )
        parts = re.split(pattern, md_text, flags=re.MULTILINE)
        return [p.strip() for p in parts if p.strip()]

    def merge_short_segments(segments, min_len=400):
        merged, buffer = [], ""
        for seg in segments:
            if len(seg) < min_len or seg.startswith(("> **Image Summary:", "> **Table Summary:")):
                buffer += "\n\n" + seg
            else:
                if buffer:
                    seg = buffer + "\n\n" + seg
                    buffer = ""
                merged.append(seg)
        if buffer:
            merged.append(buffer)
        return merged

    if not documents:
        print(" No documents provided.")
        return []

    model = SentenceTransformer(model_name, device=device)

    all_dynamic_chunks = []
    all_chunk_lengths = []
    all_similarities = []

    # 🔁 Process EACH file/document separately
    for doc_idx, doc in enumerate(documents, start=1):
        text = doc.page_content
        source = doc.metadata.get("source", f"doc_{doc_idx}")

        segments = structural_split(text)
        segments = merge_short_segments(segments)

        if not segments:
            print(f" No text segments found for document: {source}")
            continue

        embeddings = model.encode(segments, normalize_embeddings=True)
        current_chunk_segments = [segments[0]]
        current_vec = embeddings[0]

        chunk_lengths = []
        avg_similarities = []

        for i in range(1, len(segments)):
            sim = util.cos_sim(current_vec, embeddings[i]).item()
            avg_similarities.append(sim)
            combined_len = sum(len(s) for s in current_chunk_segments) + len(segments[i])

            # New numbered heading → force new chunk
            if re.match(r"^#+\s+\d", segments[i]):
                chunk_text = "\n\n".join(current_chunk_segments)
                all_dynamic_chunks.append(
                    Document(page_content=chunk_text.strip(), metadata={"source": source})
                )

                overlap = current_chunk_segments[-overlap_segments:] if overlap_segments > 0 else []
                current_chunk_segments = overlap + [segments[i]]
                current_vec = embeddings[i]
                continue

            if sim > similarity_threshold and combined_len < max_chunk_size:
                current_chunk_segments.append(segments[i])
                current_vec = (current_vec + embeddings[i]) / 2
            else:
                current_len = sum(len(s) for s in current_chunk_segments)
                chunk_lengths.append(current_len)

                chunk_text = "\n\n".join(current_chunk_segments)
                all_dynamic_chunks.append(
                    Document(page_content=chunk_text.strip(), metadata={"source": source})
                )

                overlap = current_chunk_segments[-overlap_segments:] if overlap_segments > 0 else []
                current_chunk_segments = overlap + [segments[i]]
                current_vec = embeddings[i]

        # Flush last chunk for this doc
        if current_chunk_segments:
            final_len = sum(len(s) for s in current_chunk_segments)
            chunk_lengths.append(final_len)
            chunk_text = "\n\n".join(current_chunk_segments)
            all_dynamic_chunks.append(
                Document(page_content=chunk_text.strip(), metadata={"source": source})
            )

        all_chunk_lengths.extend(chunk_lengths)
        all_similarities.extend(avg_similarities)

    # Global stats
    if print_stats and all_dynamic_chunks and all_chunk_lengths:
        avg_len = int(np.mean(all_chunk_lengths))
        print("\n Chunking Statistics (all docs):")
        print(f"  Total Chunks: {len(all_dynamic_chunks)}")
        print(f"  Avg Length: {avg_len:,} chars")
        print(f"  Min Length: {min(all_chunk_lengths):,} chars")
        print(f"  Max Length: {max(all_chunk_lengths):,} chars")
        if all_similarities:
            print(f"  Avg Semantic Similarity: {np.mean(all_similarities):.3f}")

    print(f" Created {len(all_dynamic_chunks)} structure-aware dynamic chunks (with metadata).")
    return all_dynamic_chunks



# ============================================================
# MCQG-SRefine-style helpers (domain-aware)
# ============================================================

def extract_json_block(text):
    """
    Utility: best-effort JSON extraction from LLM outputs that may
    contain <think>...</think>, markdown fences, etc.
    """
    if not text:
        return None
    # Remove DeepSeek-style thinking tags if present
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Strip markdown fences
    text = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE)
    text = re.sub(r"```$", "", text.strip())
    # Try to find a JSON object or array
    m = re.search(r"(\{.*\})", text, re.DOTALL)
    if not m:
        m = re.search(r"(\[.*\])", text, re.DOTALL)
    if not m:
        return None
    return m.group(1)


def normalize_str_list(x):
    """
    Flattens lists and converts dicts safely to strings.
    ALWAYS returns List[str]
    """
    if not x:
        return []

    out = []
    for item in x:
        if isinstance(item, dict):
            out.append(
                str(
                    item.get("topic")
                    or item.get("name")
                    or item.get("value")
                    or item
                )
            )
        elif isinstance(item, list):
            for sub in item:
                out.append(str(sub))
        else:
            out.append(str(item))
    return out



def identify_topics_and_testpoints(chunk):
    """
    Step 1: Topic and Test Point Identification (domain-agnostic).
    Topics/test points are in the SAME domain as the document text.
    """
    prompt = f"""
You are an expert instructor. The following text may belong to any domain
(e.g., "O-RAN", "3GPP", "4G", "5G", networking, etc.).

Given the text, do ONE things:

1. Identify 3 to 5 high-level topics in the SAME domain as the text
   (e.g., "O-RAN", "3GPP", "4G", "5G").


Return STRICTLY in JSON:

{{
  "topics": ["...", "..."],
  "test_points": ["...", "...", "..."]
}}

Text:
\"\"\"{chunk}\"\"\"
"""
    raw = make_llm_call(prompt)
    json_block = extract_json_block(raw)
    topics, test_points = [], []
    if json_block:
        try:
            data = json.loads(json_block)
            topics = data.get("topics", []) or []
            test_points = data.get("test_points", []) or []
        except Exception as e:
            print(f"[topics/test_points] JSON parse error: {e}\nRaw: {raw[:500]}")
    else:
        print("[topics/test_points] No JSON found in LLM output.")
    return topics, test_points


def init_mcq_components(chunk, topics, test_points):
    """
    INIT step: generate context, question, options, correct answer
    given <n=chunk, t=topics, k=test_points> in the same domain as the text.
    """
    # ---- SAFE FLATTENING OF test_points ----
   # def normalize_list(x):
       # flat = []
      # for item in x:
         #   if isinstance(item, list):
        #        for sub in item:
       #             flat.append(str(sub))
      #      else:
     #           flat.append(str(item))
    #    return flat

   # topics = normalize_list(topics) if topics else []
   # test_points = normalize_list(test_points) if test_points else []

    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"
    # ---- END FIX ----


    prompt = f"""
    You are generating a high-quality, professional multiple-choice question STRICTLY for the purpose of:
    1) Testing LLM capability WITHOUT RAG
    2) Testing LLM capability WITH RAG on O-RAN specification chunks
    3)Testing LLM capability WITH Graph RAG on O-RAN specification chunks

    ==================== ✅ ALLOWED QUESTION TYPES ====================
    You are ONLY allowed to generate questions that test:

    1. Functional understanding of O-RAN components  
    (e.g., Near-RT RIC, Non-RT RIC, SMO, O-DU, O-CU, O-RU)

    2. Interface-level behavior and responsibilities  
    (e.g., A1, E2, O1, O2, F1, E1, NG)

    3. Cause → Effect relationships  
    (e.g., misconfiguration → KPI degradation, policy → network behavior)

    4. Control-loop logic  
    (Non-RT RIC → Near-RT RIC → RAN behavior)

    5. Fault, anomaly, KPI, and performance degradation reasoning  
    (latency, packet loss, RLF, PRB utilization, throughput)

    6. Specification-driven behavior  
    (what a component MUST, SHOULD, or SHALL do based strictly on this chunk)

    All questions MUST require:
    ✅ Multi-step reasoning  
    ✅ More than one concept from the chunk  
    ✅ Understanding of system behavior — NOT memorization

    ==================== ❌ DISALLOWED QUESTION TYPES ====================
    You MUST NOT generate:

    ❌ Trivial definition-based questions  
    ❌ Direct copy-paste statements from the text  
    ❌ Yes/No questions  
    ❌ Questions whose answer is explicitly written in a single sentence  
    ❌ Vendor-specific implementation questions  
    ❌ Numerical or formula-based questions  
    ❌ Questions that can be answered using general telecom knowledge  
    ❌ Questions that rely on information NOT present in this chunk  
    ❌ Questions about document structure, tables, figures, clause numbers  
    ❌ Questions about release versions, spec numbers, or filenames
    ❌ Dont genrate question directly from the file name or from the document structure

    ==================== ✅ STRICT RAG EVALUATION RULE ====================
    The question MUST be:
    ✅ Impossible or very difficult to answer correctly WITHOUT this chunk  
    ✅ Straightforward to answer correctly WITH this chunk  
    ✅ Fully derivable ONLY from the provided text  
    ✅ Free from external assumptions

    Source text (n):
    \"\"\"{chunk}\"\"\"

    Target topics (t):
    {topics_str}

    Target test points (k):
    {tpoints_str}

    1. Create a refined CONTEXT that is concise, coherent, and does NOT trivially
   reveal the correct answer (you may hide or paraphrase direct keyword answers,
   but keep enough information to solve the question via understanding).

    2. Generate ONE high-quality MCQ that strictly follows ALL rules above.

    3. The question MUST test reasoning — NOT memory.

    4. Provide exactly FOUR answer OPTIONS (A, B, C, D).

    5. Mark the CORRECT_ANSWER as one of the options using its FULL option text.

    6. If NO valid reasoning-based question is possible from this chunk,
    RETURN EXACTLY:
    []

    Return STRICTLY as a JSON array with ONE object:

    [
    {{
        "context": "....",
        "question": "....",
        "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
        "correct_answer": "B. ..."
    }}
    ]
    """
    raw = make_llm_call(prompt)
    json_block = extract_json_block(raw)
    if not json_block:
        print("[INIT] Failed to extract JSON for MCQ INIT.")
        return None

    try:
        data = json.loads(json_block)
        if isinstance(data, list) and data:
            item = data[0]
        elif isinstance(data, dict):
            item = data
        else:
            print("[INIT] Unexpected JSON structure.")
            return None

        context = item.get("context", "").strip() or chunk
        question = item.get("question", "").strip()
        options = item.get("options", [])
        correct_answer = item.get("correct_answer", "").strip()

        if not (question and options and correct_answer):
            print("[INIT] Missing fields in MCQ INIT.")
            return None

        return {
            "context": context,
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
        }
    except Exception as e:
        print(f"[INIT] JSON parse error: {e}\nRaw: {raw[:500]}")
        return None


def qa_answer_mcq(mcq_state):
    """
    QA step: model answers its own MCQ with reasoning.
    We keep the full text as 'qa_feedback'.
    """
    ctx = mcq_state["context"]
    q = mcq_state["question"]
    options = mcq_state["options"]

    options_str = "\n".join(options)

    prompt = f"""
    You are an expert in the SAME technical/domain area as the context below.

    Read the context and the question carefully, reason through the implications,
    and select the SINGLE best answer.

    Context:
    {ctx}

    Question:
    {q}

    Options:
    {options_str}

    Instructions:
    - Think step by step using correct domain knowledge & logic
    - Eliminate options that contradict the context or domain principles
    - Justify your reasoning concisely
    - Finally provide output EXACTLY formatted as:

    Answer: X

    (where X is A, B, C, or D)
    """
    raw = make_llm_call(prompt)
    return raw or ""


def critique_mcq(chunk, topics, test_points, mcq_state, qa_feedback):
    """
    Critique step: the LLM critiques context, question, answer, distractors, reasoning
    using a rubric (adapted from MCQG-SRefine).
    """
    ctx = mcq_state["context"]
    q = mcq_state["question"]
    options = mcq_state["options"]
    correct_answer = mcq_state["correct_answer"]

    options_str = "\n".join(options)
    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"

    prompt = f"""
You are an expert exam designer acting as a critic for a multiple-choice question.

Source text (n):
\"\"\"{chunk}\"\"\"

Target topics (t): {topics_str}
Target test points (k): {tpoints_str}

CURRENT MCQ:
Context:
{ctx}

Question:
{q}

Options:
{options_str}

Correct answer (as currently set):
{correct_answer}

Model's own QA attempt and reasoning:
{qa_feedback}

Using the following rubrics (adapted from MCQG-SRefine):

- Context: Relevance, Conciseness, Coherence, Consistency, Specificity, Fluency,
           Clueing (does it give away answer?), Completeness, Misdirection quality.
- Question: Relevance, Clarity, whether it truly tests a key concept / reasoning,
            Difficulty level (Easy / Medium / Hard), Ambiguity issues.
- Correct Answer: Correctness, Justification from the context, Depth of Understanding,
                  Prevention of trivial guesswork.
- Distractors: Format consistency, Plausibility, Relation to context, Common mistakes,
               Differentiation from correct answer.
- Reasoning (QA step): Logical flow, Evidence-based reasoning, consideration of all options.

For EACH component, provide:
1. A short CRITIQUE (bullet points).
2. 1–5 SCORE for each aspect you think is important (you may group them).
3. A short summary sentence of how to improve it.

Return a well-structured plain-text critique. DO NOT rewrite the MCQ here.
"""
    raw = make_llm_call(prompt)
    return raw or ""


def refine_mcq_once(chunk, topics, test_points, mcq_state, qa_feedback, critique_text):
    """
    Correction step: use critique + QA feedback to improve <context, question, options, correct_answer>.
    Returns a NEW mcq_state dict or None on failure.
    """
    ctx = mcq_state["context"]
    q = mcq_state["question"]
    options = mcq_state["options"]
    correct_answer = mcq_state["correct_answer"]

    options_str = "\n".join(options)
    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"

    prompt = f"""
You are now an MCQ reviser improving the previous question.

Original text (n):
\"\"\"{chunk}\"\"\"

Target topics (t): {topics_str}
Target test points (k): {tpoints_str}

CURRENT MCQ:
Context:
{ctx}

Question:
{q}

Options:
{options_str}

Correct answer:
{correct_answer}

Model's QA attempt and reasoning:
{qa_feedback}

Critique of this MCQ (from another expert):
{critique_text}

Your task:
1. FIX all issues raised in the critique while keeping the same core topic & test point focus.
2. Make the question more aligned with realistic, high-quality professional exam style.
3. Increase or maintain difficulty (do NOT make it trivial).
4. Ensure the correct answer is unambiguously correct and derivable from the context.
5. Ensure distractors are plausible but clearly wrong to an expert.

Return STRICTLY as a JSON array with ONE object:

[
  {{
    "context": "....",
    "question": "....",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "correct_answer": "C. ..."
  }}
]
"""
    raw = make_llm_call(prompt)
    json_block = extract_json_block(raw)
    if not json_block:
        print("[CORRECTION] Failed to extract JSON.")
        return None

    try:
        data = json.loads(json_block)
        if isinstance(data, list) and data:
            item = data[0]
        elif isinstance(data, dict):
            item = data
        else:
            print("[CORRECTION] Unexpected JSON structure.")
            return None

        new_ctx = item.get("context", "").strip() or ctx
        new_q = item.get("question", "").strip() or q
        new_options = item.get("options", []) or options
        new_correct = item.get("correct_answer", "").strip() or correct_answer

        return {
            "context": new_ctx,
            "question": new_q,
            "options": new_options,
            "correct_answer": new_correct,
        }
    except Exception as e:
        print(f"[CORRECTION] JSON parse error: {e}\nRaw: {raw[:500]}")
        return None


def mcqg_srefine_pipeline(chunk, refinement_rounds=1):
    """
    Full MCQG-SRefine-style pipeline for ONE chunk:
    1) Topic & test-point identification
    2) INIT (context, question, options, correct_answer)
    3) QA-answer step
    4) Critique
    5) Correction (iterative)
    Returns: list with a single MCQ dict (for compatibility with your main loop)
    """
    topics, test_points = identify_topics_and_testpoints(chunk)
    # ✅ NORMALIZE ONCE HERE (FIXES YOUR CRASH)
    topics = normalize_str_list(topics)
    test_points = normalize_str_list(test_points)
    print(f" Topics: {topics}")
    print(f" Test points: {test_points}")

    mcq_state = init_mcq_components(chunk, topics, test_points)
    if not mcq_state:
        print("[MCQG-SRefine] INIT failed, returning None.")
        return None

    qa_feedback = qa_answer_mcq(mcq_state)

    last_critique = ""
    for r in range(refinement_rounds):
        print(f"--- MCQG-SRefine refinement round {r+1} ---")
        critique_text = critique_mcq(chunk, topics, test_points, mcq_state, qa_feedback)
        last_critique = critique_text
        refined = refine_mcq_once(chunk, topics, test_points, mcq_state, qa_feedback, critique_text)
        if not refined:
            print("[MCQG-SRefine] Correction failed, stopping refinement.")
            break
        mcq_state = refined
        qa_feedback = qa_answer_mcq(mcq_state)

    # Final MCQ object compatible with your pipeline
    final_mcq = {
        "question": mcq_state["question"],
        "options": mcq_state["options"],
        "correct_answer": mcq_state["correct_answer"],
        # extra fields:
        "generated_context": mcq_state["context"],
        "topics": topics,
        "test_points": test_points,
        "qa_feedback": qa_feedback,
        "last_critique": last_critique,
    }

    return [final_mcq]


# --- MCQ Generation using full MCQG-SRefine-style pipeline ---
def generate_mcq(chunk):
    """
    Uses full MCQG-SRefine-style pipeline:
      - topic/test-point identification
      - INIT
      - QA
      - iterative Critique + Correction
    Returns: list of MCQ dicts (usually length 1).
    """
    return mcqg_srefine_pipeline(chunk, refinement_rounds=1)

#for parallel processing in both ollama nodes
def process_chunk_parallel(idx, chunk_doc):
    """
    Runs FULL MCQ pipeline for ONE chunk in parallel.
    Each call will use round-robin Ollama via make_llm_call().
    """
    print(f"🧩 Processing chunk {idx}")

    chunk_text = chunk_doc.page_content
    results = []

    generated_mcqs = generate_mcq(chunk_text)
    if generated_mcqs:
        for mcq in generated_mcqs:
            if "question" in mcq and "options" in mcq and "correct_answer" in mcq:
                mcq["difficulty"] = categorize_mcq(mcq)
            else:
                mcq["difficulty"] = "Uncategorized"

            mcq["source_chunk"] = chunk_text
            results.append(mcq)

            # ✅ Save immediately (crash-safe)
            append_mcq_to_file(mcq)

    return results


# --- MCQ Validation (unchanged logic) ---
def validate_mcq(chunk, mcq_data):
    """
    Stage 2: Validator LLM. Checks if the generated question is coherent and answerable.
    """
    print(f"\n----- VALIDATOR STAGE -----")
    if not mcq_data:
        print("Skipping validation due to no input.")
        return False

    correct_answer = mcq_data.get("correct_answer", "")

    # Normalize correct_answer to get the letter (A/B/C/D)
    if isinstance(correct_answer, str):
        # Expecting something like "C. It reflects CPU activity."
        match = re.match(r"^([A-Da-d])[\.\)]", correct_answer.strip())
        if match:
            generator_answer_letter = match.group(1).upper()
        else:
            print("Error: Couldn't parse answer letter from string format.")
            return False
    elif isinstance(correct_answer, dict):
        # Accept either "option" or "letter" as valid keys
        generator_answer_letter = (
            correct_answer.get("option")
            or correct_answer.get("letter")
            or ""
        ).strip().upper()
        if generator_answer_letter not in ["A", "B", "C", "D"]:
            print("Error: Missing or invalid 'letter'/'option' key in correct_answer dict.")
            return False
    else:
        print("Error: Unrecognized correct_answer format.")
        return False

    prompt = f"""
You are a validation agent. Verify if a multiple-choice question is valid and answerable based *only* on the provided context.

Context:
\"\"\"{chunk}\"\"\"

Question: {mcq_data['question']}
Options:
{chr(10).join(mcq_data['options'])}

Instructions:
Based *only* on the context, determine the correct option letter (A, B, C, or D). Your answer must be just the single capital letter of the correct option.
"""
    print("Prompting Validator LLM...")
    validator_answer_letter = make_llm_call(prompt)

    if validator_answer_letter:
        validator_answer_letter = validator_answer_letter.strip().upper()
        print(f"Generator's Answer: {generator_answer_letter}")
        print(f"Validator's Answer: {validator_answer_letter}")

        if generator_answer_letter == validator_answer_letter:
            print("Validation successful: Answers match.")
            return True
        else:
            print("Validation failed: Answers do not match.")
            return False
    return False


# --- Categorization ---
def categorize_mcq(mcq_data):
    if not mcq_data:
        return "Uncategorized"

    prompt = f"""
You are a difficulty assessment agent. Classify the following question's difficulty as 'Easy', 'Intermediate', or 'Difficult'
for an exam in the SAME domain as its content.

Question: {mcq_data['question']}
Answer: {mcq_data['correct_answer']}

Difficulty Criteria:
- Easy: Basic concepts, definitions, or directly stated facts.
- Intermediate: Requires comprehension, application, or combining info from a few sentences.
- Difficult: Demands deep understanding, synthesis, or knowledge of subtle details.

Your response must be only one word: 'Easy', 'Intermediate', or 'Difficult'.
"""
    print("Prompting Categorizer LLM...")
    category = make_llm_call(prompt)
    if category:
        category_clean = re.sub(r"<think>.*?</think>", "", category, flags=re.DOTALL).strip()
        match = re.search(r"\b(Easy|Intermediate|Difficult)\b", category_clean)
        if match:
            return match.group(1)
    return "Uncategorized"


# def extract_answer_letter(correct_answer):
#     """
#     Extracts the option letter (A/B/C/D) from a correct_answer string like:
#     "B. Facilitating communication..." -> "B"
#     If it can't parse, returns the original value.
#     """
#     if isinstance(correct_answer, str):
#         # Match the first letter A–D at the start
#         match = re.match(r"^\s*([A-Da-d])[\.\)]?", correct_answer.strip())
#         if match:
#             return match.group(1).upper()
#     return correct_answer    

# def append_simple_mcq_to_file(mcq, filename="mcq_database5.json"):
#     simple_mcq = {
#         "question": mcq.get("question"),
#         "options": mcq.get("options"),
#         "correct_answer": extract_answer_letter(mcq.get("correct_answer")),
#         "difficulty": mcq.get("difficulty"),
#         "source_chunk": mcq.get("source_chunk"),
#     }

#     # If file exists, append to list
#     if os.path.exists(filename):
#         with open(filename, "r", encoding="utf-8") as f:
#             try:
#                 data = json.load(f)
#             except:
#                 data = []
#     else:
#         data = []

#     data.append(simple_mcq)

#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2)

# --- Main Pipeline ---
if __name__ == "__main__":
    # Only require GOOGLE_API_KEY if Gemini is used
    if not USE_LOCAL_LLM:
        if "GOOGLE_API_KEY" not in os.environ or not os.environ["GOOGLE_API_KEY"]:
            print("Execution stopped. Please configure your GOOGLE_API_KEY or set USE_LOCAL_LLM = True.")
            exit()

    md_dir_path = "/home/abdulla-ovais/Desktop/MCQ/data"

    processed_files = load_completed_files()
    documents = []
    new_files = []  # ✅ NEW: track which files are in this run

    for filename in os.listdir(md_dir_path):
        if filename.endswith(".md"):
            if filename in processed_files:
                print(f"⏭ Skipping already completed file: {filename}")
                continue

            file_path = os.path.join(md_dir_path, filename)
            docs = load_single_md_file(file_path)
            documents.extend(docs)
            save_processed_file(filename)
            new_files.append(filename)  # ✅ NEW: mark for completion tracking
            print(f" Marked '{filename}' as processed and saved.")

    if not documents:
        print(f"No new Markdown documents found in '{md_dir_path}'. Exiting.")
        exit()

    print(f" Loaded {len(documents)} Markdown documents.")

    # Use structure-aware chunking
    text_chunks = dynamic_chunk_documents(documents)

    # ✅ Build file → chunk mapping for per-file completion tracking
    file_chunk_map = {}

    for chunk in text_chunks:
        source_file = os.path.basename(chunk.metadata.get("source", ""))
        if source_file not in file_chunk_map:
            file_chunk_map[source_file] = []
        file_chunk_map[source_file].append(chunk)

    # ✅ PRINT NUMBER OF CHUNKS PER FILE
    print("\n📊 Chunks per file:")
    for source_file, chunks in file_chunk_map.items():
        print(f"  {source_file} → {len(chunks)} chunks")
    


    final_mcq_database = []

    # if MODE == "generate_only":
    #     for chunk_doc in text_chunks:
    #         generated_mcqs = generate_mcq(chunk_doc.page_content)
    #         if generated_mcqs:
    #             for mcq in generated_mcqs:
    #                 # Categorize only if MCQ has all required fields
    #                 if "question" in mcq and "options" in mcq and "correct_answer" in mcq:
    #                     mcq["difficulty"] = categorize_mcq(mcq)
    #                 else:
    #                     print(" Invalid MCQ structure, skipping categorization")
    #                     mcq["difficulty"] = "Uncategorized"
    #                 mcq["source_chunk"] = chunk_doc.page_content
    #                 final_mcq_database.append(mcq)
    #                 append_mcq_to_file(mcq)
                    # append_simple_mcq_to_file(mcq) # ALSO save simplified MCQ in a different JSON file
    if MODE == "generate_only":

        for source_file, chunks in file_chunk_map.items():
            print(f"\n🚀 Processing FILE: {source_file}")

            file_results = []

            with ThreadPoolExecutor(max_workers=len(OLLAMA_NODES)) as executor:
                futures = []

                for i, chunk_doc in enumerate(chunks, 1):
                    futures.append(executor.submit(process_chunk_parallel, i, chunk_doc))

                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        file_results.extend(result)

            # ✅ SAVE FILE AS COMPLETED IMMEDIATELY AFTER ITS CHUNKS FINISH
            save_completed_file(source_file)
            print(f" ✅ FILE SAVED AS COMPLETED: {source_file}")

            final_mcq_database.extend(file_results)



    elif MODE == "validate_only":
        if not os.path.exists("mcq_database6.json"):
            print(" 'mcq_database6.json' not found.")
        else:
            with open("mcq_database6.json", "r") as f:
                preloaded_mcqs = json.load(f)
            for mcq in preloaded_mcqs:
                chunk = mcq.get("source_chunk", "")
                if chunk and validate_mcq(chunk, mcq):
                    mcq["difficulty"] = categorize_mcq(mcq)
                    final_mcq_database.append(mcq)
                    append_mcq_to_file(mcq)


                    

    elif MODE == "generate_and_validate":
        for chunk_doc in text_chunks:
            generated_mcqs = generate_mcq(chunk_doc.page_content)
            if generated_mcqs:
                for mcq in generated_mcqs:
                    if validate_mcq(chunk_doc.page_content, mcq):
                        mcq["difficulty"] = categorize_mcq(mcq)
                        mcq["source_chunk"] = chunk_doc.page_content
                        final_mcq_database.append(mcq)
                        append_mcq_to_file(mcq)

    print(f"\nTotal MCQs generated: {len(final_mcq_database)}")
    if final_mcq_database:
        with open("mcq_database6.json", "w") as f:
            json.dump(final_mcq_database, f, indent=2)
        print(" MCQs saved to 'mcq_database6.json'")

    # # ✅ NEW: mark files from this run as COMPLETED
    # for fname in new_files:
    #     save_completed_file(fname)
    #     print(f" ✅ Marked '{fname}' as COMPLETED.")