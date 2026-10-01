# Meesho Reseller Growth & Alert Intelligence Pipeline

## Project Overview

This project implements an end-to-end reseller monitoring pipeline for Meesho.

The pipeline follows this workflow:

1. Generate and seed the reseller and order dataset.
2. Compute business metrics using SQL.
3. Calculate month-on-month growth and validate feeds.
4. Generate controlled narrative drafts and apply reseller-name masking.
5. Run a mock agent that validates the feed, identifies flagged categories,
   drafts messages for the top flagged categories, and holds them for human approval.

The pipeline does not require any API keys.

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
```
