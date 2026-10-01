# Narrative Report

## Worked Narrative 1 — May Ethnic Wear

### Context

This measures Ethnic Wear revenue growth from April to May.

### Insight

**Fact:** Ethnic Wear revenue increased by **77.1% month-on-month** from April to May.

### Implication

**Hypothesis:** The increase may warrant checking whether reseller demand or order activity contributed to the growth, but the available revenue data alone does not establish the cause.

**Action:** Review the May Ethnic Wear reseller and order-level data to identify which coded reseller aliases and order activity contributed to the increase before making inventory or regional allocation decisions.

---

## Worked Narrative 2 — June Ethnic Wear

### Context

This measures Ethnic Wear revenue growth from May to June.

### Insight

**Fact:** Ethnic Wear revenue decreased by **58.74% month-on-month** from May to June.

### Implication

**Hypothesis:** The decrease may be associated with changes in reseller demand or order activity, but the available revenue data alone does not establish the cause.

**Action:** Review June Ethnic Wear reseller and order-level data against May activity to identify where the decline occurred before making inventory or regional allocation decisions.

---

# Self-Score Against the Refinement Checklist

## Specificity

Pass — The narratives identify the exact category, comparison months, and exact MoM percentages: 77.1% for May and -58.74% for June.

## Audience Fit

Pass — The narratives are written for a regional manager and focus on what should be reviewed or acted upon rather than describing implementation details for a data engineer.

## Completeness

Pass — Each narrative contains Context, Insight, and Implication sections.

## Actionability

Pass — Each narrative specifies a concrete next step: review reseller and order-level data against the relevant comparison month before making inventory or regional allocation decisions.

---

# Chart-Choice Justification

## 1. Which month had the highest total revenue?

A **bar chart** should be used because this is a univariate comparison of total revenue across three discrete months. The x-axis would contain April, May, and June, while the y-axis would show total revenue in INR and start at zero. A bar chart makes the comparison clear within 10 seconds, without unnecessary 3D effects. The totals are April = INR 419417.43, May = INR 444594.25, and June = INR 398055.24.

## 2. What percentage share does Ethnic Wear represent of April's total revenue?

A **pie chart** could be used to communicate the percentage share because the question concerns one component's share of a whole. Ethnic Wear represents **24.92%** of April's total revenue, based on INR 104520.77 out of INR 419417.43. The visualization should remain simple and avoid unnecessary decoration.

## 3. How do the four regions compare on total revenue?

A **bar chart** should be used because this is a univariate comparison of total revenue across four discrete regions. The regions would be placed on the categorical axis and revenue on the y-axis, with the y-axis starting at zero. A single series means a legend is unnecessary, and the chart should make the regional comparison clear within 10 seconds.

# Top-Reseller Narrative

## Context

The top-reseller view summarizes revenue by the five resellers returned by Part 1's
HAVING query. The narrative uses coded aliases and regions so that raw reseller
names are not exposed in an external-facing summary.

## Insight

**Fact:** The five top-reseller results are represented by the following
coded aliases, regions, and revenue values:

- ALIAS-19 — Mumbai — INR 75295.09
- ALIAS-22 — Mumbai — INR 73882.33
- ALIAS-12 — Hyderabad — INR 69936.46
- ALIAS-06 — Lucknow — INR 64238.97
- ALIAS-05 — Jaipur — INR 61825.02

## Implication

**Action:** A regional manager can use these coded aliases and regional information
to review the corresponding reseller-level performance while keeping raw reseller
names out of the external-facing narrative.
