# Agent Specification

## Goal

Keep Meesho category managers informed of any category whose month-on-month
revenue moves beyond the 8% threshold, with a human approving every drafted
message before it goes out.

---

## Tools

The monitoring agent uses the following concrete functions:

1. `validate_feed(csv_path)` from Part 2 to validate the monthly revenue feed
   before any other processing.
2. `mom_growth(previous, current)` from Part 2 to calculate month-on-month
   revenue growth.
3. `is_flagged(mom_pct, threshold=8.0)` from Part 2 to classify the result as
   `flagged`, `not_flagged`, or `escalate_exact_boundary`.
4. The Part 3 prompt-pack template-fill logic to create a stakeholder
   narrative for categories that require a draft.

The Part 2 functions are imported and reused without re-implementing their
logic.

---

## Memory / State

The agent must retain the previous month's revenue per category so that the
current month's revenue can be compared against the previous month when
calculating month-on-month growth.

For each category, the relevant state is:

- category
- previous month
- previous revenue
- current month
- current revenue

This state supports the next month's MoM calculation.

---

## Planner

The agent follows this ordered sequence:

1. Load the monthly revenue feed and run `validate_feed`.
2. If the feed is invalid, Hard Stop and report the validation errors.
3. If the feed is valid, compute `mom_growth` for every category against the
   previous month.
4. Run `is_flagged` on every category.
5. Sort flagged categories by `abs(mom_pct)` in descending order.
6. Draft a message using the Part 3 template for at most the top 3 flagged
   categories by magnitude.
7. Log any remaining flagged categories beyond the top 3 as
   `suppressed, review manually` without drafting a message for them.
7b. Separately log any category whose `is_flagged` result is
    `escalate_exact_boundary` into `escalated_categories`, without drafting a
    message for it.
8. Emit one structured JSON object per run.

---

## Feedback Loop

Every drafted message is held for human approval before it is considered sent.

The mock agent does not send email or make any external communication.

The runner represents the approval checkpoint using the action status
`drafted_and_held_for_approval`.

No Gmail, SMTP integration, network call, or API key is required or in scope.

---

## Guardrails

### Input Guardrail

`validate_feed` must pass before anything else runs.

If validation fails, no MoM calculation, flagging, drafting, or suppression
processing is performed.

### Action Guardrail

No message is ever auto-sent.

Messages are only drafted and held for human approval.

### Output Guardrail

Every number in a drafted message must trace back to a Part 1 or Part 2
value.

The agent must not invent numerical values.

---

## Success and Error Stopping Conditions

### Success Condition

The run succeeds when drafts are produced for flagged categories, or when
there are correctly zero drafts because no category crossed the threshold.

Every numerical value in a drafted message must be traceable to the project's
Part 1 or Part 2 values.

### Error Condition

If `validate_feed` returns `False`, the run is a Hard Stop.

The validation errors must be surfaced in the output rather than silently
skipping the invalid data.

No MoM calculation or message drafting is performed after a validation failure.

---

## Agent-Level Given-When-Then Specifications

### Specification 1 — Flagged May Ethnic Wear

**Given** April Ethnic Wear revenue is INR 104520.77 and May Ethnic Wear
revenue is INR 185107.61,

**When** the agent calculates the month-on-month growth and applies the
8% threshold,

**Then** the MoM growth is `77.1%` and the category result is `flagged`.

---

### Specification 2 — Not-Flagged June Beauty & Personal Care

**Given** May Beauty & Personal Care revenue is INR 35542.11 and June
Beauty & Personal Care revenue is INR 37559.07,

**When** the agent calculates the month-on-month growth and applies the
8% threshold,

**Then** the MoM growth is `5.67%` and the category result is
`not_flagged`.

---

### Specification 3 — Exact Boundary

**Given** a category has a month-on-month growth result of exactly `8.0%`,

**When** the agent applies the 8% threshold,

**Then** the category result is `escalate_exact_boundary` and the category
is placed in `escalated_categories` without drafting a message.

---

### Specification 4 — Corrupted Feed

**Given** the current-month feed contains a negative revenue value, a missing
category, and a missing revenue value,

**When** the agent runs `validate_feed` before performing any MoM calculation,

**Then** validation fails, the run becomes a Hard Stop, the validation errors
are surfaced, and no flagged or suppressed categories are produced.