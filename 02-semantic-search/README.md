# Project 02 - Semantic Search

## Objective

Build a Semantic Search Engine from scratch and understand how modern AI systems retrieve information based on meaning instead of keyword matching. 

This project focuses on : 

- Embeddings
- Vector Representations
- Cosine Similarity
- Semantic Search
- Embedding persistence
- Foundations of Vector databases
- Foundations of Retrieval Augmented Generation (RAG)

---

## Why this project exists

In project 01 (Spam Classifier), we discovered limitations of TF-IDF :

```text
win != won
car != automobile
migration != data transfer
```

TF-IDF treats words as independent features

This project explore how Embeddings allow machines to search using meaning rather than exact word

---

## Learning journey

```text
                            Raw text
                                |
                                v
                            Embeddings
                                |
                                v
                          Vector Space
                                |
                                v
                        Cosine Similarity
                                |
                                v
                         Semantic Search
                                |
                                v
                          Vector Store
```

---

## Project Architecture

### Phase 1 - Embedding Generation

Input : 
```text
Migration count mismatch due to duplicate records
```

Embedding Model:
```text
all-MiniLM-L6-v2
```

Output : 
```text
[ 0.00856206 -0.08774728  0.043294....]
```

Shape : 
```text
(384,)
```

Each sentence is represented as 384-dimensional vector

---

## Important learning

Embeddings are not
```text
Dimension 1 = migration
Dimension 2 = count
Dimension 3 = issue
...
```

Instead : 
```text
Meaning is distributed across all dimensions
```

The vector represents the semantic meaning of a sentence

---

## Phase 2 - Understanding Similarity

Example Sentences : 
```text
"Migration count mismatch due to duplicate records",
"Reconciliation data discrepancy found after data transfer",
"Dog is playing in the garden"
```

Cosine Similarity Result : 
```text
Migration <-> Reconciliation : 0.4374
Migration <-> Dog : -0.0391
```


Key learnings : 

Even without sharing keywords :
```text
Migration count mismatch
```

and
```text
Reconciliation discrepancy
```

are recognized semantically related.

---

## What is Cosine Similarity ?

Consine Similarity compares the direction of vectors.

Very Simplified : 
```text
1.0 => very similar
0.8 => similar
0.5 => somewhat related
0.0 => unrelated
-1.0 => opposited direction
```

Semantic search relies on similarity between vector directions rather than keyword overlap.

---

## Phase 3 - Building Semantic Search

Search Workflow : 
```text
                            User Query
                                |
                                v
                     Generate Query Embeddings
                                |
                                v
                Compare Against Documents Embeddings
                                |
                                v
                        Cosine Similarity
                                |
                                v
                           Sort By Score
                                |
                                v
                          Top k Results
```

Example Query : 
```text
migration count issue
```

Results : 
```text
0.8097 -> Migration count mismatch due to duplicate records
0.6358 -> Source and traget count differed after migration
0.2711 -> Reconciliation data discrepancy found after data transfer
```

Example Query  :
```text
data transfer discrepancy
```

Results : 
```text
0.7346 -> Reconciliation data discrepancy found after data transfer
0.3986 -> Migration count mismatch due to duplicate records
0.2136 -> Kafka consumer lag causing delayed processing
```

Key learning :

The model retrieves relevant documents based on meaning even when keywords differ.

---

## Phase 4 - Embedding Persistence

Intially :
```text
                            Documents
                                |
                                v
                        Generate Embeddings
                                |
                                v
                              Search
```

Embeddings were being recalculated for every search.

To mimic real-world systems, embeddings were persisted.

---

### Indexing Phase
```text
documents.txt
    |
    v
Embedding Model
    |
    v
documents_embedding.npy

documents.pkl
```

Generated once

---

### Search Phase

```text
                    Load Storage Embeddings
                            |
                            v
                   Generate Query Embeddings
                            |
                            v
                      Cosine Similarity
                            |
                            v
                      Search Results
```

This separates :
```text
Indexing
```

from 
```text
Searching
```

Which mmirrors how real system operates

---

## Files

### index_documents.py

Responsible for : 
```text
Read documents
    |
    v
Generate Embeddings
    |
    v
Persist Embeddings
```

Outputs:
```text
documents_embeddings.npy
documents.pkl
```

---

### search.py

Responsible for : 
```text
                  Load Persisted Embeddings
                            |
                            v
                  Generate Query Embeddings
                            |
                            v
                    Semantic Search
                            |
                            v
                    Return Top Results
```

---

## What we built

Conceptually : 
```text
                       documents.txt
                            |
                            v
                        Embeddings
                            |
                            v
                       Vector Store
                            |
                            v
                      Semantic Search
```

This is effectively a miniature version of 

```text
FAISS
ChromoDB
PineCone
Weaviate
Milvus
pgvector
```

without specialized indexing structures.

---


## Key takeways

### Semantic Search > Keywords Search

Keyword search :
```text
Matches word
```

Semantic Search : 
```text
Matches meaning
```

---

### Embeddings Represent Meaning

Not :
```text
Words
```

but :
```text
Semantic concepts
```

represented in vector space.

---

### Retrieval is the foundation of RAG

The retrieval mechanism built in this project is the same principle used by : 

```text
Enterprise Search
Copilot
AI assistants
RAG Systems
Knowledge search platform
```

---

## Connection To The bigger AI journey

Project 01 :
```text
Classification
```

Pipeline : 
```text
                           Text
                            |
                            v
                        Features
                            |
                            v
                    Logistic Regression
                            |
                            v
                        Prediction
```

---

Project 02 :
```text
Semantic Retrieval
```

Pipeline : 
```text
                           Text
                            |
                            v
                        Embeddings
                            |
                            v
                    Similarity Search
                            |
                            v
                    Retrieved Documents
```

---

Next : 

## Project 03 - Mini RAG

```text
                      User Question
                            |
                            v
                      Semantic Search
                            |
                            v
                      Top Documents
                            |
                            v
                           LLM
                            |
                            v
                    Generated Answer
```

Project 03 combines retrieval and generation to build the first complete AI assistant.