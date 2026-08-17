# Project 05 - Production RAG Foundation

## Objective

Build a production-oriented Retrieval Augmented Generation (RAG) pipeline by progressively improving retrieval quality by chunking, semantic chunking, metadata management, vector indexing and hybrid search.

This project focuses on :
- Chunking Strategies
- Chunk Overlap
- Semantic Chunking
- Metadata MAnagement
- Source Attribution
- FAISS Vector search
- Hybrid Search
- Production Retrieval Architecture

---

## Why this project exists ?

Project 03 succesfully demonstrated RAG : 
```text
Question
    |
    v
Retrieve Documents
    |
    v
Inject Context
    |
    v
LLM
    |
    v
Answer
```

However real world enterprise system face additional challenges :
```text
Large documents
Millions of Chunks
Retrieval Precision
Search Performance
Source Traceability
```

This Project explores the retrieval side of Production AI systems.

---

## Learning Journey

```text
Large Document
    |
    v
Chunking
    |
    v
Chunk Overlap
    |
    v
Semantic Chunking
    |
    v
Vector Indexing (FAISS)
    |
    v
Hybrid Search
    |
    v
Production Retrieval
```

---

## Project Architecture


```text
Document
    |
    v
Chunking
    |
    v
Semantic Chunking
    |
    v
Embeddings
    |
    v
FAISS Index
    |
    v
Metadata Store
    |
    v
Hybrid Search
    |
    v
Retrieved Context
```

---

## Project Structure

```text
05-production-rag
|   
|---data/
|   |---knowledge_base.txt
|   |---chunk_index.faiss
|   |---chunks.pkl
|
|---src/
|   |---chunk.py
|   |---chunker.py
|   |---semantic_chunker.py
|   |---index_chunks.py
|   |---retrieve.py
|   |---hybrid_search.py
|   |---evaluation.py
|
|---.gitignore
|---README.md
|---requirements.txt
```
---

## Phase 1 - Chunking

Problem : 

Embedding an entire document into a single vector reduces retrieval precision.

Example :
```text
40-page migration document
```

One embedding attempt to represent
```text
Overview
Achitecture
Root Cause
Resolution
Runbook
```

simultaneously.

---

### Initial Chunking

Implemented :
```text
chunk_by_paragraph
```

Benefits : 
```text
Preserves meaning
Preserves narrative
```

Drawbacks : 
```text
Paragraph size is unpredictable
Very small chunks
very large chunks
```

---

## Phase 2 - Size Aware Chunking

Introduced : 
```text
max_words
```

Example : 
```text
chunk_by_paragraph_with_limit(
    max_words=30
)
```

Benefits : 
```text
Predictable Chunk Sizes
Controlled prompt usages
```

Trade-off : 
```text
Chunk Size
vs
Context Preservation
```

---

## Phase 3 - Chunk Overlap

Problem :
```text
Root Cause
```

appears at the end of chunk 1.
```text
Resolution
```

appears at the beginning of chunk 2.

Important Context becomes split

---

## Solution

Implemented Overlap
```text
Chunk 1 :
words 1-30

Chunk 2 :
words 21-50
```

Benefits :
```text
Context Continuity
Better retrieval robustness
Reduced information loss
```

---

## Phase 4 - Semantic Chunking

Traditional Chunking uses : 
```text
Word counts
Character counts
```

Semantic uses : 
```text
Meaning
```

---

## Approach

For each sentence :
```text
Sentence
    |
    v
Embeddings
    |
    v
Similarity to Next Sentence
```

Example : 
```text
0.71
0.39
0.05 <-- topic boundary
0.45
0.09 <-- topic boundary
```

---

## Chunking Rule
```python
if similarity < threshold:
    start_new_chunk()
```

Benefits : 
```text
Chunk align with topics
Natural content boundaries
Improved retrieval quality
```

---

## Phase 5 - Metadata Management

Introduced structed chunk metadata.
```python
Chunk(
    chunk_id,
    text,
    source,
    section
)
```

Metadata supports : 
```text
Source Tracking
Filtering
Auditability
Citations
```

---

## Phase 6 - FAISS Vector Search

### Problem : 

Brute-force similarity search : 
```text
Query
    |
    v
Compare against every chunk
```

Complexity : 
```text
O(N)
```

Not practical for large knowledge bases.

---

### Solution

FAISS

Architecture : 
```text
Chunks
    |
    v
Embeddings
    |
    v
FAISS Index
```

Stored : 
```text
chunk_index.faiss
```

Metadata stored separately : 
```text
chunks.pkl
```

---

## Key Learning

FAISS stores : 
```text
Vectors
```

and returns :
```text
Nearest Vector IDs
```

Metadata lookup retrieves : 
```text
Chunk Text
Source
Section
```

This mirrors : 
```text
Database Index
+
Table data
```
architecture.

---

## Phase 7 - Source Attribution

Retrieval results evovled from : 
```text
Chunk text
```

to : 
```text
Score
Source
Section
Chunk Text
```

Example : 
```text
Final Score : 0.9392

Vector Score : 0.4846

Keyword Score : 2.0000
Source : knowledge_base.txt
Migration count mismatch occured due to duplicate records being loaded during reconciliation.
The reconciliation process loaded several rows twice, which infalted the target count.
The issue was resolved by adding deduplication logic before target ingestion.
```

Benefits : 
```text
Trust
Explainability
Auditability
```

---

## Phase 8 - Hybrid Search

### Problem

Vector Search performs well for : 
```text
Meaning
Concepts
Intent
```

but may struggle with  :
```txt
Identifiers
Acronyms
Error Codes
Ticket IDs
```

Examples : 
```text
KafkaTopicV17
JIRA-1234
```

---

### Solution

Combine : 
```text
Vector Search
+
Keyword Search
```

Architecture :
```text
Query 
|---Vector Search
|---Keyword Search

        |
        v

Combined Score

        |
        v

Final Ranking
```

---

## Scoring Strategy
```text
final_score = 
    0.7 * vector_score 
    + 
    0.3 * keyword_score
```

Benefits : 
```text
Semantic Understanding
+
Exact Identifier Match
```

---

## Key Learnings

### Chunking matters more than most people expect

RAG quality is heavily influenced by :
```text
Chunk Size 
Chunk Boundaries
Chunk Overlap
```

---

### Retrieval Quality Drives Answer Quality

Bad Retrieval :
```text
Bad Answer
```
even with powerful LLM

---

### Metadata is essential

Metadata enables :
```text
Filtering
Transperancy
Source Attribution
```

required in enterprise systems.

---

### FAISS solves scale

Instead of:
```text
Brute Force search
```

using :
```text
O(N)
```

retrieval becomes indexed and scalable.

---

### Enterprise search is hybrid

Modern retrieval systems rely on : 
```text
Keyword search
+
Vetor Search
```

instead of choosing one or the other.

---

## Technlogies used : 
```text
Python
SentenceTransformers
Numpy
Scikit-learn
FAISS
Gemini API
```

---

## Connection to the AI Engeering Lab

```text
Project 01
Machine Learning Foundations

Project 02
Semantic Search

Project 03
Retrieval Augmented Generation

Project 04
Tool Calling Agents

Project 05
Production RAG Foundation
```

---

## Next Project

### Evaluation and Observability

Focus Areas : 
```text
Retrieval Evaluation
RAG Evaluation
Tracing
Observability
Hallucination Detection
Production Monitoring
```

Moving from :
```text
Working AI system
```

to : 
```text
Reliable AI system
```