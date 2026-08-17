# Project 06 - Evaluation & Observability

## Objective

Bulid evaluation and obserbability capabilities for AI systems in order to measure retrieval quality, identify regressions and increase trust in AI application.

This project focuses on : 

- Retrieval Evaluation
- Retrieval Accuracy Metrics
- Regression Detection
- AI Observability
- Quality Gates
- Testing AI systems

---

## Why this project exits?

Building AI systems is onyl half the problem.

The other half is understanding : 
```text
Is retrieval working?
Didanswer quality improve?
Did a code change introduce regressions?
Can we trust the system?
```

This project intorduces evaluation and monitoring concepts used in production AI systems.

---

## Learning Journey

```text
AI Application
    |
    v
Evaluation Dataset
    |
    v
Automated Testing
    |
    v
Metrics
    |
    v
Observability
    |
    v
Confidence
```

---

## Project Structure
```text
06-evaluation-observability/
|
|---data/
|   |--- test_cases.json
|   
|---src/
|   |--- retrieval_evaluator.py
|   |--- metrics.py
|   |--- evaluation_running.py
|   
|---README.md
|---requirements.txt
```

---

## Retrieval Evaluation

Example Test Case :
```json
{
    "query" : "How was migration fixed?",
    "expected_keywords": [
        "deduplication"
    ]
}
```

Workflow : 
```text
Query
    |
    v
Hybrid Search
    |
    v
Retrieved Chunks
    |
    v
Expected Keywords Found?
    |
    v
PASS / FAIL
```

---

## Metric

Current Metric : 

```text
Retrieval Accuracy
```

Formula : 
```text
Passed Queries
/
Total Queries
```

Examples :
```text
3 / 3
=
100%
```

---

## Why Evaluation MAtters

Without evaluation : 
```text
Change Chunking Logic
    |
    v
Hope It Works
```

With evaluation : 
```text
Change Chunking Logic
    |
    v
Run Evaluation
    |
    v
Compare Results
```

---

## Observability

Tracked : 
```text
Query
Expected Keywords
Retrieved Chunk
Scores
Pass / Fail
```

This creates a foundation for future AI monitoring systems.

---

## Key Learnings

### AI Systems Need Quality Gates

Working examples are not enough.

Automated validation is required

### Retrieval Quality Directly Impacts RAG Quality

Bad retireval:
```text
Bad Answer
```

even with strong models.

### Evaluation Enables Safe Iteration

Changes can be measured instead of guessed.

---

## Connection to the AI Engineering Lab
```text
Project 01
Machine Learning Foundations

Project 02
Semantic Search

Project 03
RAG

Project 04
Tool Calling Agents

Project 05
Production RAG

Project 06
Evaluation & Observability
```

---

## Final Learning Outcome

Transition from : 
```text
Building AI Systems
```

to : 
```text
Measuring and Trusting AI Systems
```