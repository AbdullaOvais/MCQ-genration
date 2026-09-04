import os
import re
import json
import time
import requests
import torch
import numpy as np
#import google.generativeai as genai
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
from langchain_core.documents import Document
from concurrent.futures import ThreadPoolExecutor, as_completed
import itertools

# --- Device info ---
print("CUDA available:", torch.cuda.is_available())
print("Using device:", torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# ===========================================================
#                   CONFIG
# ===========================================================
load_dotenv()

USE_LOCAL_LLM = True

# Multi-node Ollama configuration
# OLLAMA_NODES = [
#     "http://10.9.64.22:11434/api/generate",
#     "http://192.168.50.140:11434/api/generate",
    
# ]

OLLAMA_NODES = [
    "http://127.0.0.1:11440/api/generate",
    "http://127.0.0.1:11441/api/generate",
    "http://127.0.0.1:11442/api/generate",
    "http://127.0.0.1:11443/api/generate",
  # "http://127.0.0.1:11444/api/generate",
  # "http://127.0.0.1:11445/api/generate",
  # "http://127.0.0.1:11446/api/generate",
  # "http://127.0.0.1:11447/api/generate",
] 
LOCAL_LLM_MODEL = "deepseek-r1:32b"

# Round-robin node iterator
node_cycle = itertools.cycle(OLLAMA_NODES)

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-1.5-flash"

INPUT_MD_DIR = "/export/home/suguna/MCQ/final_parsed_oran_latest_with_image"
OUTPUT_JSONL = "qa_dataset2.jsonl"

BASE_CHUNK_SIZE = 4000
MAX_CHUNK_SIZE = 10000
SIMILARITY_THRESHOLD = 0.4
OVERLAP_SEGMENTS = 1

# Tracking files
PROCESSED_FILES_PATH = "processed_files_qa.json"
COMPLETED_FILES_PATH = "completed_files_qa.json"

# Number of refinement rounds
REFINEMENT_ROUNDS = 1


# ===========================================================
#               FILE TRACKING FUNCTIONS
# ===========================================================
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


def load_completed_files():
    if os.path.exists(COMPLETED_FILES_PATH):
        with open(COMPLETED_FILES_PATH, "r") as f:
            return set(json.load(f))
    return set()


def save_completed_file(filename):
    completed = load_completed_files()
    completed.add(filename)
    with open(COMPLETED_FILES_PATH, "w") as f:
        json.dump(list(completed), f, indent=2)


# ===========================================================
#               LLM CALL FUNCTIONS
# ===========================================================
def query_local_llm(prompt, endpoint):
    """Query a specific Ollama node"""
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": LOCAL_LLM_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": 2048}
    }
    response = requests.post(endpoint, headers=headers, json=payload, timeout=300)
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        raise RuntimeError(f"[ERROR {response.status_code}] {response.text}")


def query_gemini_llm(prompt):
    """Query Gemini API"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        result = model.generate_content(prompt)
        return result.text
    except Exception as e:
        print(f"Gemini error: {e}")
        return None


def llm_call(prompt, retries=3, delay=5):
    """
    Wrapper for all LLM calls with round-robin multi-node support
    """
    if not USE_LOCAL_LLM:
        # Gemini path with retry
        for attempt in range(retries):
            try:
                return query_gemini_llm(prompt)
            except Exception as e:
                print(f"Gemini LLM call failed: {e}")
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    return None

    # Local multi-node Ollama path with round-robin
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


# ===========================================================
#               STRUCTURE-AWARE CHUNKING
# ===========================================================
def structural_split(md_text):
    pattern = (
        r'(?=^# |\n# |\n## |\n### |!\[\]\(images/|<table|'
        r'> \*Image Summary:|> \*Table Summary:)'
    )
    parts = re.split(pattern, md_text, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]


def merge_short_segments(segments, min_len=3000):
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


def dynamic_chunk_documents(documents,
                            base_chunk_size=6000,
                            max_chunk_size=10000,
                            similarity_threshold=0.4,
                            model_name="all-MiniLM-L6-v2",
                            overlap_segments=1,
                            print_stats=True):
    """
    Structure-aware + semantic dynamic chunking with metadata preservation
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🔧 Using device: {device}")

    if not documents:
        print("⚠️ No documents provided.")
        return []

    model = SentenceTransformer(model_name, device=device)
    all_dynamic_chunks = []
    all_chunk_lengths = []
    all_similarities = []

    # Process each document separately
    for doc_idx, doc in enumerate(documents, start=1):
        text = doc.page_content
        source = doc.metadata.get("source", f"doc_{doc_idx}")

        segments = structural_split(text)
        segments = merge_short_segments(segments)

        if not segments:
            print(f"⚠️ No text segments found for document: {source}")
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

        # Flush last chunk
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
        print("\n📊 Chunking Statistics (all docs):")
        print(f"  Total Chunks: {len(all_dynamic_chunks)}")
        print(f"  Avg Length: {avg_len:,} chars")
        print(f"  Min Length: {min(all_chunk_lengths):,} chars")
        print(f"  Max Length: {max(all_chunk_lengths):,} chars")
        if all_similarities:
            print(f"  Avg Semantic Similarity: {np.mean(all_similarities):.3f}")

    print(f"✅ Created {len(all_dynamic_chunks)} structure-aware dynamic chunks (with metadata).")
    return all_dynamic_chunks
# ===========================================================
# 🔹 Cross-chunk semantic similarity helpers (NEW)
# ===========================================================

def build_all_chunk_embeddings(chunks, model_name="all-MiniLM-L6-v2"):
    """
    Build embeddings for ALL chunks once.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SentenceTransformer(model_name, device=device)
    texts = [c.page_content for c in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True)
    return embeddings


def get_top_k_similar_chunks(
    query_idx,
    all_embeddings,
    similarity_threshold=0.50,
    top_k=4
):
    """
    Given a chunk index, find Top-K similar chunks above threshold.
    Returns: List[(chunk_index, similarity_score)]
    """
    scores = util.cos_sim(all_embeddings[query_idx], all_embeddings)[0]

    candidates = []
    for idx, score in enumerate(scores):
        if idx == query_idx:
            continue
        score_val = float(score)
        if score_val >= similarity_threshold:
            candidates.append((idx, score_val))

    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[:top_k]


def build_cross_chunk_context(
    query_chunk,
    top_k_chunks,
    all_chunks,
    max_chars=15000
):
    """
    Merge query chunk + Top-K similar chunks.
    Track source files.
    """
    texts = [query_chunk.page_content]
    source_files = {query_chunk.metadata.get("source")}

    for idx, score in top_k_chunks:
        chunk = all_chunks[idx]
        texts.append(chunk.page_content)
        source_files.add(chunk.metadata.get("source"))

    combined_text = "\n\n".join(texts)
    if len(combined_text) > max_chars:
        combined_text = combined_text[:max_chars]

    return combined_text, list(source_files)



# ===========================================================
#    HELPER FUNCTIONS FOR SREFINE METHODOLOGY
# ===========================================================
# def extract_json_block(text):
#     """
#     Utility: best-effort JSON extraction from LLM outputs that may
#     contain <think>...</think>, markdown fences, etc.
#     """
#     if not text:
#         return None
#     # Remove DeepSeek-style thinking tags if present
#     text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
#     # Strip markdown fences
#     text = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE)
#     text = re.sub(r"```$", "", text.strip())
#     # Try to find a JSON array
#     m = re.search(r"(\[.*\])", text, re.DOTALL)
#     if m:
#         return m.group(1)
#     return None

def extract_json_block(text):
    if not text:
        return None

    # Remove <think> blocks
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    # Remove markdown fences
    text = re.sub(r"```.*?\n", "", text)
    text = re.sub(r"```", "", text)

    # Find FIRST valid JSON array
    matches = re.findall(r"\[[\s\S]*?\]", text)
    for m in matches:
        try:
            json.loads(m)
            return m
        except:
            continue
    return None


def safe_extract_json_object(text):
    if not text:
        return None
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    matches = re.findall(r"\{[\s\S]*?\}", text)
    for m in matches:
        try:
            return json.loads(m)
        except:
            continue
    return None



# def identify_topics_and_testpoints(chunk):
#     """
#     Step 1: Topic and Test Point Identification
#     """
#     prompt = f"""
# You are an expert instructor. The following text may belong to any domain
# (e.g., "O-RAN", "3GPP", "4G", "5G", networking, etc.).

# Given the text, identify 3 to 5 high-level topics in the SAME domain as the text.

# Return STRICTLY in JSON:

# {{
#   "topics": ["...", "..."],
#   "test_points": ["...", "...", "..."]
# }}

# Text:
# \"\"\"{chunk[:8000]}\"\"\"   # ← IMPORTANT LIMIT
# """
#     raw = llm_call(prompt)
#     json_block = safe_extract_json_object(raw)
    
#     # Try to extract as object if array extraction failed
#     if not json_block:
#         m = re.search(r"(\{.*\})", raw, re.DOTALL) if raw else None
#         json_block = m.group(1) if m else None
    
#     topics, test_points = [], []
#     if json_block:
#         try:
#             data = json.loads(json_block)
#             topics = data.get("topics", []) or []
#             test_points = data.get("test_points", []) or []
#         except Exception as e:
#             print(f"[topics/test_points] JSON parse error: {e}")
#     else:
#         print("[topics/test_points] No JSON found in LLM output.")
#     return topics, test_points

def identify_topics_and_testpoints(chunk):
    prompt = f"""
You are an expert instructor.

Given the text, identify 3 to 5 high-level topics
and 3 to 5 concrete test points.

Return STRICTLY in JSON:

{{
  "topics": ["...", "..."],
  "test_points": ["...", "..."]
}}

Text:
\"\"\"{chunk[:8000]}\"\"\"
"""

    raw = llm_call(prompt)

    # Case 1: already parsed dict
    obj = safe_extract_json_object(raw)
    if isinstance(obj, dict):
        return obj.get("topics", []), obj.get("test_points", [])

    # Case 2: raw JSON string
    try:
        data = json.loads(obj)
        return data.get("topics", []), data.get("test_points", [])
    except:
        print("[topics/test_points] Failed to parse JSON")
        return [], []

def is_valid_qa_pair(obj):
    return (
        isinstance(obj, dict)
        and "question" in obj
        and "answer" in obj
        and isinstance(obj["question"], str)
        and isinstance(obj["answer"], str)
        and len(obj["question"].strip()) > 5
        and len(obj["answer"].strip()) > 5
    )


def qa_answer_own_question(qa_pair):
    """
    Step 3: QA-Answer - Model answers its own question with reasoning.
    """
    q = qa_pair["question"]

    prompt = f"""
You are an expert in O-RAN, 3GPP, 4G, and 5G technical domains.

Question:
{q}

Instructions:
- Think step by step using correct domain knowledge & logic
- Provide detailed reasoning for your answer
- Consider all aspects of the question
- Finally provide your answer

Format your response as:
Reasoning: [your step-by-step reasoning]
Answer: [your final answer]
"""
    raw = llm_call(prompt)
    return raw or ""


def critique_qa(chunk, topics, test_points, qa_pair, qa_feedback):
    """
    Step 4: Critique - The LLM critiques the question and answer quality.
    """
    q = qa_pair["question"]
    a = qa_pair["answer"]

    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"

    prompt = f"""
You are an expert exam designer acting as a critic for a question-answer pair.

Source text (n):
\"\"\"{chunk}\"\"\"

Target topics (t): {topics_str}
Target test points (k): {tpoints_str}

CURRENT Q/A:
Question: {q}
Answer: {a}

Model's own QA attempt and reasoning:
{qa_feedback}

Using the following rubrics:

- Question: Relevance, Clarity, whether it truly tests key concepts/reasoning,
            Difficulty level (Easy/Medium/Hard), Ambiguity issues, 
            Alignment with topics and test points
- Answer: Correctness, Completeness, Technical accuracy, 
          Justification quality, Depth of understanding,
          Whether it fully addresses the question
- Reasoning: Logical flow, Evidence-based reasoning, Technical correctness

For EACH component, provide:
1. A short CRITIQUE (bullet points)
2. A score from 1-5 for quality
3. A short summary of how to improve it

Return a well-structured plain-text critique. DO NOT rewrite the Q/A here.
"""
    raw = llm_call(prompt)
    return raw or ""


def refine_qa_once(chunk, topics, test_points, qa_pair, qa_feedback, critique_text):
    """
    Step 5: Correction - Use critique + QA feedback to improve the Q/A pair.
    """
    q = qa_pair["question"]
    a = qa_pair["answer"]

    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"

    prompt = f"""
You are now a Q/A reviser improving the previous question-answer pair.

Original text (n):
\"\"\"{chunk}\"\"\"

Target topics (t): {topics_str}
Target test points (k): {tpoints_str}

CURRENT Q/A:
Question: {q}
Answer: {a}

Model's QA attempt and reasoning:
{qa_feedback}

Critique of this Q/A (from another expert):
{critique_text}

Your task:
1. FIX all issues raised in the critique while keeping the same core topic & test point focus
2. Make the Q/A more aligned with realistic, high-quality technical documentation
3. Increase or maintain difficulty (do NOT make it trivial)
4. Ensure the answer is comprehensive, technically accurate, and unambiguous
5. Keep the question clear and well-framed

Return STRICTLY as a JSON array with ONE object:

[
  {{
    "question": "....",
    "answer": "...."
  }}
]
"""
    raw = llm_call(prompt)
    json_block = extract_json_block(raw)
    if not json_block:
        print("[CORRECTION] Failed to extract JSON.")
        return None

    try:
        data = json.loads(json_block)
        if isinstance(data, list) and data:
            return data[0]
        elif isinstance(data, dict):
            return data
        else:
            print("[CORRECTION] Unexpected JSON structure.")
            return None
    except Exception as e:
        print(f"[CORRECTION] JSON parse error: {e}")
        return None


# ===========================================================
#     ORIGINAL Q/A GENERATION FUNCTIONS WITH SREFINE
# ===========================================================
def generate_normal_qa(chunk):
    """
    Generate normal Q/A pairs with SRefine methodology
    """
    print("\n--- Generating NORMAL Q/A with SRefine ---")
    
    # Step 1: Identify topics and test points
    topics, test_points = identify_topics_and_testpoints(chunk)
    print(f"📌 Topics: {topics}")
    print(f"📌 Test points: {test_points}")
    
    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"
    
    # Step 2: INIT - Generate initial Q/A
    prompt = f"""
Generate some (one or more Q/As based on content length) normal questions from below text that require multi-step or multi-conceptual understanding related to O-RAN/3GPP/5G/4G.
Generate maximum of 2 Q/As which are hard and require deep understanding of 3GPP, O-RAN, 4G, 5G specs to answer.
Make framing of questions and answers clear and unambiguous, don't make them as they are generated by using a chunks as context.

 You are generating a high-quality, professional normal question STRICTLY for the purpose of:
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

Target topics: {topics_str}
Target test points: {tpoints_str}

Return ONLY JSON in format of:
[
  {{"question": "...", "answer": "..."}}
]

TEXT:
\"\"\"{chunk}\"\"\"
"""
    resp = llm_call(prompt)
    json_block = extract_json_block(resp)
    # ✅ Fallback: try to force JSON recovery
    if not json_block:
        try:
            start = resp.index("[")
            end = resp.rindex("]") + 1
            json_block = resp[start:end]
        except:
            return []


    try:
        qa_pairs = json.loads(json_block)
    except Exception as e:
        print(f"⚠️ JSON parse error: {e}")
        return []
    
    # Step 3-5: Refine each Q/A pair
    # Step 3-5: Refine each Q/A pair (SAFE)
    refined_pairs = []

    for qa_pair in qa_pairs:

        # 🔒 HARD VALIDATION
        if not is_valid_qa_pair(qa_pair):
            print("⚠️ Skipping invalid QA pair:", qa_pair)
            continue

        # Step 3: Model answers its own question
        qa_feedback = qa_answer_own_question(qa_pair)

        # If model failed to answer, skip refinement
        if not isinstance(qa_feedback, str) or not qa_feedback.strip():
            print("⚠️ Empty QA feedback, skipping refinement")
            refined_pairs.append(qa_pair)
            continue

        # Step 4-5: Iterative refinement
        last_critique = ""
        for r in range(REFINEMENT_ROUNDS):
            print(f"  → Refinement round {r+1}/{REFINEMENT_ROUNDS}")

            critique_text = critique_qa(
                chunk,
                topics,
                test_points,
                qa_pair,
                qa_feedback
            )
            last_critique = critique_text

            refined = refine_qa_once(
                chunk,
                topics,
                test_points,
                qa_pair,
                qa_feedback,
                critique_text
            )

            # 🔒 Validate refined output
            if refined and is_valid_qa_pair(refined):
                qa_pair = refined
                qa_feedback = qa_answer_own_question(qa_pair)
            else:
                print("  ⚠️ Refinement failed or invalid → keeping previous version")
                break

        refined_pairs.append(qa_pair)
    return refined_pairs


def generate_reasoning_qa(chunk):
    """
    Generate reasoning Q/A pairs with SRefine methodology
    """
    print("\n--- Generating REASONING Q/A with SRefine ---")
    
    # Step 1: Identify topics and test points
    topics, test_points = identify_topics_and_testpoints(chunk)
    print(f"📌 Topics: {topics}")
    print(f"📌 Test points: {test_points}")
    
    topics_str = ", ".join(topics) if topics else "key topics from the text"
    tpoints_str = ", ".join(test_points) if test_points else "important fine-grained concepts"
    
    # Step 2: INIT - Generate initial Q/A
    prompt = f"""
Generate some (one or more Q/As based on content length) reasoning questions from Text that require multi-step understanding which are related to O-RAN or 3GPP or 4G/5G.
Generate maximum of 2 Q/As which are hard and require deep understanding of 3GPP, O-RAN, 4G, 5G specs to answer.
Make framing of questions and answers clear and unambiguous, don't make them as they are generated by using a chunks as context.

 You are generating a high-quality, professional reasoning question STRICTLY for the purpose of:
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

    =================== ✅ STRICT RAG EVALUATION RULE ====================
    The question MUST be:
    ✅ Impossible or very difficult to answer correctly WITHOUT this chunk  
    ✅ Straightforward to answer correctly WITH this chunk  
    ✅ Fully derivable ONLY from the provided text  
    ✅ Free from external assumptions

Target topics: {topics_str}
Target test points: {tpoints_str}

Return ONLY JSON:
[
  {{"question": "...", "answer": "..."}}
]

TEXT:
\"\"\"{chunk}\"\"\"
"""
    resp = llm_call(prompt)
    json_block = extract_json_block(resp)
    # ✅ Fallback: try to force JSON recovery
    if not json_block:
        try:
            start = resp.index("[")
            end = resp.rindex("]") + 1
            json_block = resp[start:end]
        except:
            return []


    try:
        qa_pairs = json.loads(json_block)
    except Exception as e:
        print(f"⚠️ JSON parse error: {e}")
        return []
    
    # Step 3-5: Refine each Q/A pair
    refined_pairs = []

    for qa_pair in qa_pairs:

        # 🔒 HARD VALIDATION
        if not is_valid_qa_pair(qa_pair):
            print("⚠️ Skipping invalid QA pair:", qa_pair)
            continue

        # Step 3: Model answers its own question
        qa_feedback = qa_answer_own_question(qa_pair)

        # If model failed to answer, skip refinement
        if not isinstance(qa_feedback, str) or not qa_feedback.strip():
            print("⚠️ Empty QA feedback, skipping refinement")
            refined_pairs.append(qa_pair)
            continue

        # Step 4-5: Iterative refinement
        last_critique = ""
        for r in range(REFINEMENT_ROUNDS):
            print(f"  → Refinement round {r+1}/{REFINEMENT_ROUNDS}")

            critique_text = critique_qa(
                chunk,
                topics,
                test_points,
                qa_pair,
                qa_feedback
            )
            last_critique = critique_text

            refined = refine_qa_once(
                chunk,
                topics,
                test_points,
                qa_pair,
                qa_feedback,
                critique_text
            )

            # 🔒 Validate refined output
            if refined and is_valid_qa_pair(refined):
                qa_pair = refined
                qa_feedback = qa_answer_own_question(qa_pair)
            else:
                print("  ⚠️ Refinement failed or invalid → keeping previous version")
                break

        refined_pairs.append(qa_pair)
    return refined_pairs


def append_qa_to_file(qa_entry, filename=OUTPUT_JSONL):
    """Append Q/A entry to JSONL file (crash-safe)"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(qa_entry) + "\n")


# ===========================================================
#           PARALLEL PROCESSING
# ===========================================================
def process_chunk_parallel(idx, chunk_doc, filename):
    """Process a single chunk in parallel"""
    print(f"\n🧩 Processing chunk {idx} from {filename}")

    chunk_text = chunk_doc.page_content
    results = []

    # 🔹 Cross-chunk Top-K selection (NEW)
    top_k_chunks = get_top_k_similar_chunks(
        query_idx=idx - 1,   # idx is 1-based
        all_embeddings=ALL_CHUNK_EMBEDDINGS,
        similarity_threshold=0.50,
        top_k=4
    )

    combined_text, source_files = build_cross_chunk_context(
        chunk_doc,
        top_k_chunks,
        all_chunks
    )

    MAX_QA_CONTEXT = 12000
    qa_context = combined_text[:MAX_QA_CONTEXT]

    normal_qa = generate_normal_qa(qa_context)
    reasoning_qa = generate_reasoning_qa(qa_context)

    # Generate Q/A using combined context
    # normal_qa = generate_normal_qa(combined_text)
    # reasoning_qa = generate_reasoning_qa(combined_text)

    print(f"✅ Normal Q/A: {len(normal_qa)} pairs")
    print(f"✅ Reasoning Q/A: {len(reasoning_qa)} pairs")

    if normal_qa:
        for pair in normal_qa:
            qa_entry = {
                "type": "normal",
                "question": pair["question"],
                "answer": pair["answer"]
            }
            append_qa_to_file(qa_entry)
            results.append(qa_entry)

    if reasoning_qa:
        for pair in reasoning_qa:
            qa_entry = {
                "type": "reasoning",
                "question": pair["question"],
                "answer": pair["answer"]
            }
            append_qa_to_file(qa_entry)
            results.append(qa_entry)

    print(f"💾 Saved Q/As for chunk {idx}")

    return results


# ===========================================================
#                      MAIN
# ===========================================================
if __name__ == "__main__":
    # Load completed files
    completed_files = load_completed_files()
    
    # Get all markdown files
    md_files = [f for f in os.listdir(INPUT_MD_DIR) if f.endswith(".md")]
    print(f"📁 Found {len(md_files)} markdown files")

    # Filter out completed files
    new_files = [f for f in md_files if f not in completed_files]
    
    if not new_files:
        print("✅ All files already completed!")
        exit()

    print(f"📝 Processing {len(new_files)} new files")

    # Load and chunk documents
    documents = []
    file_chunk_map = {}

    for filename in new_files:
        path = os.path.join(INPUT_MD_DIR, filename)
        print(f"\n📄 Loading: {filename}")

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        # Create document with metadata
        doc = Document(page_content=text, metadata={"source": filename})
        documents.append(doc)
        save_processed_file(filename)

    # Dynamic chunking
    all_chunks = dynamic_chunk_documents(documents)
    print("\n🧠 Building embeddings for all chunks (once)...")
    ALL_CHUNK_EMBEDDINGS = build_all_chunk_embeddings(all_chunks)
    print("✅ Chunk embeddings ready")

    # Build file → chunk mapping
    for chunk in all_chunks:
        source_file = chunk.metadata.get("source", "")
        if source_file not in file_chunk_map:
            file_chunk_map[source_file] = []
        file_chunk_map[source_file].append(chunk)

    # Print chunks per file
    print("\n📊 Chunks per file:")
    for source_file, chunks in file_chunk_map.items():
        print(f"  {source_file} → {len(chunks)} chunks")

    # Process each file
    all_qa_entries = []

    for source_file, chunks in file_chunk_map.items():
        print(f"\n🚀 Processing FILE: {source_file}")

        file_results = []

        # Parallel processing with multi-node support
        with ThreadPoolExecutor(max_workers=len(OLLAMA_NODES)) as executor:
            futures = []

            for i, chunk_doc in enumerate(chunks, 1):
                futures.append(
                    executor.submit(process_chunk_parallel, i, chunk_doc, source_file)
                )

            for future in as_completed(futures):
                result = future.result()
                if result:
                    file_results.extend(result)

        # Mark file as completed
        save_completed_file(source_file)
        print(f"✅ FILE COMPLETED: {source_file}")

        all_qa_entries.extend(file_results)

    print(f"\n🎉 Total Q/A entries generated: {len(all_qa_entries)}")
    print(f"💾 Q/A Dataset saved to {OUTPUT_JSONL}")