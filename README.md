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

## How to Run the Complete Project

Run the project from the repository root in the following order.

### Step 1 — Generate the Dataset

Generate the deterministic reseller and order dataset:

```powershell
python data/generate_dataset.py

Expected output:

Wrote 24 resellers and 900 orders. Zero-order reseller: RS024

This creates:

data/resellers.csv
data/orders.csv
data/meesho_reseller.db

The generated dataset contains 24 resellers and 900 orders across April, May, and June 2026.

Step 2 — Run Part 1 SQL Analysis

Run the SQL analysis:

python part1_sql/run_queries.py

The SQL queries are defined in:

part1_sql/queries.sql

The results are written to:

part1_sql/output/

The output files are:

monthly_category_revenue.csv
region_revenue.csv
top_resellers.csv
zero_order_resellers.csv
june_delivered_aov.csv

To run the zero-order reseller verification demo:

python part1_sql/demo_count.py

Part 1 produces the monthly category revenue feed that is used by Part 2.

Step 3 — Run Part 2 Growth and Validation Engine

The Part 2 engine is implemented in:

part2_engine/growth_engine.py

It provides:

mom_growth() for month-on-month revenue growth
is_flagged() for the 8% threshold classification
validate_feed() for input validation

The provided monthly revenue fixture is:

part2_engine/fixtures/monthly_category_revenue.csv

The corrupted validation fixture is:

part2_engine/fixtures/corrupted_feed.csv

Run the Part 2 tests:

python -m pytest part2_engine/test_growth_engine.py

Expected result:

4 passed

Part 2 identifies categories whose month-on-month revenue change exceeds the 8% threshold.

Step 4 — Part 3 Narrative and Masking

Part 3 contains the narrative prompt pack and reseller masking logic:

part3_narrative/
├── prompt_pack.md
├── narrative_report.md
└── masking.py

The prompt pack defines the narrative structure:

Context → Insight → Implication

Narratives are generated only for categories flagged by Part 2.

The masking module converts reseller IDs such as:

RS019

to:

ALIAS-19

and includes a check to ensure raw reseller names do not appear in the final narrative.

The verified narrative output is documented in:

part3_narrative/narrative_report.md
Step 5 — Part 4 Mock Agent Runner

Part 4 is the deterministic mock agent workflow:

part4_agent/
├── agent_spec.md
└── mock_agent_runner.py

The agent workflow is:

Validate the current-month feed.
Hard-stop if validation fails.
Calculate month-on-month growth for each category.
Apply the 8% flagging rule.
Sort flagged categories by absolute MoM percentage.
Draft messages for the top 3 flagged categories.
Suppress remaining flagged categories for manual review.
Escalate exact-boundary cases.
Hold drafts for human approval.

The runner exposes:

run(month, previous_month_csv, current_month_csv)

The Part 4 behavior was verified against:

May vs April
June vs May
corrupted-feed validation

No email, network request, API key, or automatic external action is performed.

Step 6 — Verify the Project

Run the Part 2 automated tests:

python -m pytest part2_engine/test_growth_engine.py

The expected result is:

4 passed

The Part 4 scenarios were also verified for:

valid May feed
valid June feed
corrupted feed
top-3 drafting
suppression
hard-stop behavior
exact numeric traceability
End-to-End Data Flow
data/generate_dataset.py
        ↓
resellers.csv + orders.csv + meesho_reseller.db
        ↓
Part 1 SQL
        ↓
monthly_category_revenue.csv
        ↓
Part 2 Growth + Validation Engine
        ↓
MoM growth + 8% flagging
        ↓
Part 3 Narrative + Masking
        ↓
Narrative drafts using aliases
        ↓
Part 4 Mock Agent Runner
        ↓
Prioritized drafts
        ↓
Human approval checkpoint

This project is deterministic and runs locally without API keys or account-gated services.
```
