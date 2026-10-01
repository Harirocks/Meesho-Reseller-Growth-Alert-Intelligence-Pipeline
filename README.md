# Meesho Reseller Growth & Alert Intelligence Pipeline

## Project Overview

This project implements an end-to-end reseller monitoring and alert intelligence
pipeline for Meesho.

The pipeline follows this workflow:

1. Generate and seed the reseller and order dataset.
2. Compute business metrics using SQL.
3. Calculate month-on-month growth and validate feeds.
4. Generate controlled narrative drafts and apply reseller-name masking.
5. Run a mock agent that validates the feed, identifies flagged categories,
   drafts messages for the top flagged categories, and holds them for human approval.

The project uses deterministic local data and does not require API keys,
external accounts, network services, or email sending.

---

## Business Problem

A reseller monitoring workflow needs to identify meaningful month-on-month
revenue movements, validate incoming data before analysis, and provide
category managers with controlled and traceable alert narratives.

This project demonstrates how verified SQL business results can flow through:

- Data generation
- SQL business analysis
- Data validation
- Month-on-month growth calculation
- Threshold-based classification
- Controlled narrative generation
- Reseller-name masking
- Agent-based alert drafting
- Human approval

The agent does not automatically send alerts. Draft messages are held for
human approval.

---

## Project Objectives

The project aims to:

1. Generate a deterministic reseller and order dataset.
2. Calculate business metrics using SQL.
3. Calculate month-on-month revenue growth.
4. Validate incoming monthly revenue feeds.
5. Identify categories whose revenue movement exceeds the 8% threshold.
6. Generate controlled stakeholder narratives for flagged categories.
7. Mask reseller names using coded aliases.
8. Implement a mock agent workflow with validation and human approval.
9. Ensure drafted numerical information is traceable to verified project data.
10. Provide a reproducible local workflow without API keys or external services.

---

## End-to-End Architecture

The complete workflow is:

````text
Deterministic Dataset
        |
        v
Part 1 — SQL Business Analysis
        |
        v
Verified Monthly Category Revenue
        |
        v
Part 2 — Growth & Validation Engine
        |
        +---- Validate Feed
        |
        +---- Calculate MoM Growth
        |
        +---- Classify Categories
        |
        v
Part 3 — Narrative Generation
        |
        +---- Context → Insight → Implication
        |
        +---- Privacy Masking
        |
        v
Part 4 — Mock Agent
        |
        +---- Validate
        +---- Plan
        +---- Draft Top 3
        +---- Suppress Remaining
        +---- Escalate Exact Boundary
        |
        v
Human Approval

## Project Structure

```text
Meesho-Project/
├── data/
│   ├── generate_dataset.py
│   ├── resellers.csv
│   ├── orders.csv
│   └── meesho_reseller.db
│
├── part1_sql/
│   ├── queries.sql
│   ├── run_queries.py
│   ├── demo_count.py
│   └── output/
│
├── part2_engine/
│   ├── growth_engine.py
│   ├── test_growth_engine.py
│   └── fixtures/
│
├── part3_narrative/
│   ├── prompt_pack.md
│   ├── narrative_report.md
│   └── masking.py
│
├── part4_agent/
│   ├── agent_spec.md
│   └── mock_agent_runner.py
│
└── README.md
````

## Requirements

- Python 3
- pytest

Install pytest if required:

```powershell
python -m pip install pytest
```
