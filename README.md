# PatchMind Proof of Concept

An initial proof of concept for **PatchMind**, a multi-agent AI system for automated bug triage and repair.

This prototype demonstrates the feasibility of the proposed architecture by implementing the core workflow of PatchMind on a small software project.

---

## Overview

The prototype simulates an autonomous bug repair pipeline using specialized agents:

```
GitHub Issue
      │
      ▼
Triage Agent
      │
      ▼
Diagnosis Agent (LLM)
      │
      ▼
Patch Agent (LLM)
      │
      ▼
Validation Agent (pytest)
```

The system:

- Reads a GitHub-style bug report.
- Identifies the most relevant source file using an LLM.
- Generates a candidate patch.
- Applies the generated fix.
- Runs the project's test suite to validate the repair.

---

## Project Structure

```
PatchMind-POC/

├── bookstore/
│   ├── pricing.py
│   ├── checkout.py
│   ├── inventory.py
│   └── __init__.py
│
├── tests/
│   ├── test_pricing.py
│   └── test_checkout.py
│
├── agents.py
├── prompts.py
├── patchmind.py
├── issue.txt
├── requirements.txt
└── README.md
```

---

## Workflow

1. Load a bug report.
2. Diagnose the relevant source file.
3. Generate a repair.
4. Apply the patch.
5. Execute the test suite.
6. Report the result.

---

## Demonstration

Before running PatchMind:

```
2 passed
1 failed
```

After running PatchMind:

```
3 passed
0 failed
```

The prototype successfully repaired the injected bug and validated the generated patch automatically.

---

## Technologies

- Python
- Groq API
- Llama 3.3 70B
- Pytest

---

## Current Scope

This proof of concept validates the orchestration workflow proposed in PatchMind.

The complete project will extend this prototype with:

- Multi-agent coordination
- Bug reproduction
- GraphRAG-based diagnosis
- Adaptive LLM routing
- GitHub integration
- Pull request generation
- Evaluation on SWE-bench

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the API key

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key
```

### Execute the prototype

```bash
python patchmind.py
```

---

## Sample Output

```
PatchMind
Autonomous Bug Triage & Repair Prototype

[Triage Agent]
Issue loaded

[Diagnosis Agent]
Relevant file:
bookstore/pricing.py

[Patch Agent]
Patch generated

[Validation Agent]
3 tests passed

READY FOR PULL REQUEST
```

---

## Relation to the Full Project

This repository represents an **early proof of concept** developed for the PatchMind graduation project.

Its purpose is to validate that an AI-assisted workflow can automatically process a software issue, generate a repair, and verify the generated patch before extending the architecture to larger real-world software repositories.
