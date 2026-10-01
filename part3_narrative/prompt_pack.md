# Reusable Narrative Prompt Pack

## Trigger

Run this prompt when a category's `is_flagged` result is `"flagged"`.

## Input list

The prompt requires these placeholder variables:

- `{category}` — category name
- `{previous_revenue}` — revenue for the previous month
- `{current_revenue}` — revenue for the current month
- `{mom_pct}` — month-on-month percentage change
- `{month}` — current month
- `{prev_month}` — previous month

## Prompt

Write a concise stakeholder update for a regional manager using the
Context → Insight → Implication structure.

Context:
State what category is being measured and the comparison period using
`{month}` and `{prev_month}`.

Insight:
State the month-on-month revenue change using `{mom_pct}` and clearly
label the percentage as a fact.

Implication:
Provide one specific and actionable next step based on the supplied
information. If a possible cause is proposed but is not directly proven
by the supplied data, label it explicitly as a hypothesis.

Rules:

- Use only the supplied placeholder values.
- Never invent or calculate a number that is not one of the supplied
  placeholders.
- Do not introduce additional numerical values.
- Do not present an unsupported cause as a fact.
- Keep the update suitable for a regional manager.
- If a reseller is referenced, use only its coded alias and never its
  raw reseller name.

## Checklist

Before the narrative is used, verify:

1. Every number in the draft matches a supplied placeholder value exactly.
2. The category name and comparison months match the supplied inputs.
3. Every numerical insight is clearly presented as a fact.
4. Any proposed cause that is not proven by the data is labeled as a hypothesis.
5. The recommendation is specific and actionable rather than vague.
6. No raw reseller name appears in the narrative; coded aliases are used instead.
