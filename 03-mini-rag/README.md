# Project 03 - Mini RAG(Retrieval Augmented Generation)

## Objective

Build a completed Retrieval Augmented Generation (RAG) pipeline from scratch and understand how modern AI assistants answer questions using private knowledge instead of relying on model training data.

This project focuses on:

- Retrieval Augmented Generation ( RAG )
- Semantic Search 
- Prompt Engineering
- Context Injection
- Grounded Responses
- LLM Integration
- Hallucination reduction

-- 

## Why this Project Exists ?

Large Language Models are powerful, but they have limitations :
```text
Knowledge Cutoff
No access to private data
Potential Hallucinations
```

Example :
```text
Why did migration count differ?
```

A standalone LLM do not know anything about our internal migration documents.

To solve this, we first retrieve relevant documents and provide them to LLM.

This pattern is known as :
```text
Retrieval Augmented Generation ( RAG )
```

---

## Learning Journey
```text
                    User Question
                        |
                        v
                  Semantic Search
                        |
                        v
                Relevant Documents
                        |
                        v
                Prompt Construction
                        |
                        v
                       LLM
                        |
                        v
                 Grounded Answer
```

--- 

## Architecture

### High Level Flow
```text
                        Knowledge Base
                            |
                            v
                        Embeddings
                            |
                            v
                      Vector Search
                            |
                            v
                    Retrieved Context
                            |
                            v
                    Prompt Construction
                            |
                            v
                          Gemini
                            |
                            v
                          Answer
```

---

## Project Structure

```text
03-mini-rag/
|
|--data/
|   |---knowledge_base.txt
|   |---documents_embeddings.npy
|   |---documents.pkl
|
|--src/
|   |--index_documents.py
|   |--retrieve.py
|   |--rag.py
|   |--llm_client.py
|   |--test_gemini.py
|
|--.env
|--.env.example
|--README.md
|--requirements.txt
|--.gitignore
```

---

## Knowledge Base

A small knowledge repository was created containing example operational documents.

Examples : 
```text
Migration count mismatch occured due to duplicate records being loaded during reconciliation.

The issue was resolved by adding deduplication logic before target ingestion.

Kafka consumer lag delayed message processing during peak hours.

Redis caching reduced API latency by 40%.

Semantic search retrieves documents using embedding similarity.
```

Think of this as miniature enterprise wiki.

---

## Phase 1 - Document Indexing

Purpose:
```text
Generate embeddings once
store them for reuse
```

Pipeline:
```text
Knowledge Base
    |
    v
Embedding Model
    |
    v
Document Embeddings
    |
    v
Persist to disk
```

Generated files:
```text
documents_embeddings.npy
documents.pkl
```

Learnings :

Retrieval systems should not generate embeddings for every query.

---

## Phase 2 - Retrieval

the retrieval search reuses semantic search developed in Project 02.

Pipeline : 
```text
Question
    |
    v
Query Embeddings
    |
    v
Cosine Similarity
    |
    v
Top K Documents
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

Learning : 

Retrieval is based on meaning and not Keyword matching.

---

## Phase 3 - Prompt Construction

Retrieved documents are converted to context.

Example : 
```text
Use ONLY the provided context

    Context :
    
    Document 1
    Migration count mismatch occured due to duplicate records being loaded during reconciliation.

    Document 2
    Semantic search retrieves documents using embedding similarity.
    
    Question:
    Why did migration counts differ?

    Answer:
```

Learning : 

Prompt quality directly impacts answer quality.

---

## Phase 4 - LLM Integration

Model used : 
```text
Gemini (Google AI Studio API)
```

Integration Flow :
```text
Question
    |
    v
retrieve()
    |
    v
bulid_prompt()
    |
    v
Gemini
    |
    v
Answer
```

Environment Variables :
```env
GEMINI_API_KEY=
```

Stored Locally in:
```text
.env
```

and excluded through :
```text
.gitignore
```

---

## Example Results : 

### Question 
```text
Why did migration count differ ?
```

Answer :
```text
Based on the provided documents, the migration count differed (mismatched) due to duplicate records being loaded during reconciliation.
```

---

### Question
```text
How was the migration issue fixed ?
```

Answer : 
```text
Based on the provided documents, the issue was resolved by adding deduplication logic before target ingestion.
```

Learing :

The answer came from retrieved documents, not from the model's internal knowledge.

---

## Retrieval vs Generation

### Retrieval

Responsible for :
```text
Finding relevant information
```

Example : 
```text
Similarity Search
Embeddings
Top k documents
```

--- 

### Generation

Responsible for : 
```text
Turning retrieved information into a natural language answer.
```

Example :
```text
Gemini
```

---

## Key Insights

A common Misconception :
```text
RAG = LLM
```

Reality:
```text
RAG = 
Retrieval
+
Prompt Construction
+
LLM
```

The LLM is only one component.

---

## What we learned

### Semantic Search Alone is not enough

Project 02 could retrieve:
```text
Migration count mismatch
```

but could not answer questions.

---
### LLM Alone is not enough

The LLM does not know our private documents

---

### Combining Both creates RAG
```text
Retrieval
+
LLM
=
Grounded Answers
```

---

## Limitations Observed

Current Implementation : 
```text
Top-K retrieval
    |
    v
Prompt
    |
    v
Answer
```

Potential future improvements :

- chunking
- chunk overlap
- Hybrid-search
- re-ranking
- Metadata filtering
- Evaluation Metrics

---

## Key takeaways

### Retrieval reduces Hallucinations

Insteam of guessing
```text
LLM
```

receives:
```text
relevant context
```
before generating answer.

---

### Context is temporary knowledge

The retrieved knowledge becomes :
```text
Working memory
```

inside the prompt.

---

### RAG is the foundation of modern AI Assistants

The same pattern powers :
```text
Copilot
ChatGPT Enterprise
Internal Knowledge assistants
Enterprise Search systems
```

---

## Connection to bigger AI journey

### Project 01
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

### Project 02
```text
Text
    |
    v
Embeddings
    |
    v
Semantic Search
    |
    v
Retrieval
```

--- 

### Project 03
```text
Question
    |
    v
Retrieval
    |
    v
Prompt
    |
    v
LLM
    |
    v
Answer
```

---

## Next Project

### Project 04 - Tool Calling and agents

Current System :
```text
Can Answer Questions
```

Next system
```text
Can take Action
```

Example : 
```text
User : Create a JIRA Ticket

Agent : calls JIRA Tool

Tool : Creates Ticket

Agent : Returns Results
```

Project 04 introduces : 
```text
Tool calling
Function calling
Agent Loop
Planning
MCP Concept
```

and marks the transition from an AI Assistant to AI Agent.

