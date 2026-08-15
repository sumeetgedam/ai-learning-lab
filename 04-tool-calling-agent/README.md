# Project 04 - Tool Calling Agent

## Objective

Build an AI Agent capable of reasoning, selecting tools, executing actions, observing results, and generating user facing responses.

This project extends the concept learned in previous projects : 

```text
Project 01
Classification

Project 02
Semantic Retrieval

Project 03
Retrieval Augmented Generation

Project 04
Tool Calling Agents
```

---

## Why This Project Exists 

Traditional LLM application can : 
```text
Answer Quesitons
```

but cannot :
```text
Perform Actions
```

Example : 
```text
Create a JIRA ticket
Check server status
send email
Query database
```

To perform actions, an AI system must interact with external tools.

The Project introduces : 
```text
Tool Calling
Agent Loops
ReAct Workflow
```

---

## Learning Journey

```text
Natural Language Query
    |
    v
Tool Selection
    |
    v
Validation
    |
    v
Tool Execution
    |
    v
Observation
    |
    v
Reasoning
    |
    v
Final Response
```

---

## Architecture Overview

```text
User Query
    |
    v
Gemini
    |
    v
Structured Tool Request
    |
    v
Validation Layer
    |
    v
Tool Registry
    |
    v
Tool Execution
    |
    v
Observation
    |
    v
Gemini
    |
    v
Final User response
```

---

## Project Structure

```text
04-tool-calling-agent/
|
|-- src/
|   |----tools.py
|   |----tool_registry.py
|   |----validator.py
|   |----llm_decision.py
|   |----agent.py
|   |----trace_logger.py
|   |----main.py
|
|---README.md
|---requirements.txt
|---.env
|---.git
```

---

## Implemented Tools

### Server Status Tool

```python
get_server_status(system)
```

Example response : 
```json
{
    "system" : "production",
    "status" : "UP"
}
```

---

### JIRA Ticket Tool

```python
create_jira_ticket(title, description)
```

Example response : 
```json
{
    "ticket_id" : "JIRA-101",
    "status" : "created"
}
```

---

## Tool Registry Pattern

Tools are registered centrally : 
```python
TOOLS = {
    "get_server_status" : get_server_status,
    "create_jira_ticket" : create_jira_ticket
}
```

Benefits : 
- Extensible
- Clean Architecture
- Simple routing
- Easy testing

--- 

## LLM-driven Tool Selection

The model converts natural language to structured JSON.

User:
```text
Create a JIRA ticket for migration count mismatch.
```

LLM :
```json
{
    "tool" : "create_jira_ticket",
    "arguments" : {
        "title" : "Migration count mismatch",
        "decription" : "..."
    }
}
```

The LLM does not execute tools directly

--- 

## Validation Layer

Before Execution : 
```text
Tool Exists ?
Required Arguments present ?
Request Structure Valid ? 
```

Example :
```json
{
    "tool" : "unknown_tool"
}
```

Rejected before execution.

---

## Multi-Step Agent Loop

```text
Reason
    |
    v
Act
    |
    v
Observe
    |
    v
Reason
    |
    v
Respond
```

Example Query : 
```text
Create a JIRA ticket if the production server is down.
```

Workflow : 
```text
Check Server Status
    |
    v
Observe Status
    |
    v
Create JIRA ticket
    |
    v
Generate Final Response
```

---

## Example Execution

### Scenario 1 - Server Down

```text
Step 1:
get_server_status

Observation:
DOWN

Step 2:
create_jira_ticket

Observation : 
JIRA-101 created.

Step 3:
Final Response
```

Agent Response :
```text
The production server status was checked and found to be DOWN. As a result, JIRA ticket JIRA-101 ('Production Server Down') has been successfully created.
```

---

### Scenario 2 - Server UP

```text
Step 1:
get_server_status

Observation:
UP

Step 2:
Final response
```

Agent Response :
```text
The production server is currently UP, so no JIRA ticket was created.
```

---

## Trace Logging

Agent Execution is fully traceable.

Example :
```text
============================================================
AGENT EXECUTION TRACE
============================================================

Step 1

Action :
{'type': 'tool_call', 'tool': 'get_server_status', 'arguments': {'system': 'production'}}

Observation :
{'system': 'production', 'status': 'UP'}

Step 2

Action :
{'type': 'final_answer', 'answer': 'The production server is currently UP, so no JIRA ticket has been created.'}

Observation :
None

============================================================
```

This mirrors production AI observability systems.

---

## Key Learnings

### LLM Should not execute tools

Instead :
```text
LLM = Planner
```

```text
Orchestrator = Validator + Executor
```

This improves safety and reliability.

---

### Agents use Observations

Unlike simple tool calling.

```text
Tool 
    |
    v
Answer
```

Agents Perform : 
```text
Tool
    |
    v
Obvservation
    |
    v
Decision
    |
    v
Tool
    |
    v
Answer
```

This enables Multi-Step Workflow.

---

### Production Agents Need Guardrails

Implemented : 
```text
Validation
Tool Registry
Execution trace
MAX_STEPS protection
```

These prevent uncontrolled agent behaviour.

--- 

## Connection To the Bigger AI Journey

```text
Project 01
Classification

Project 02
Semantic Search

Project 03
RAG

Project 04
Tool Calling Agent
```

---

## Next Project

### Project 05 - Production RAG

Focus Areas : 
```text
Chunking
Chunk Overlap
Vector DB
FAISS / Chroma
Hybrid search
Re-Racking
RAG Evaluation
Observability
``` 

Transition from : 
```text
Learning RAG
```

to
```text
Production AI Systems
```
