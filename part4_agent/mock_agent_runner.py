import csv

from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged,
)

def fill_prompt_template(
    category: str,
    previous_revenue: float,
    current_revenue: float,
    mom_pct: float,
    month: str,
    prev_month: str,
) -> str:
    return (
        f"Context: {category} revenue is being compared from "
        f"{prev_month} to {month}. "
        f"Insight: Fact — {category} revenue changed by {mom_pct}% "
        f"month-on-month. "
        f"Implication: Action — review the {category} reseller and "
        f"order-level data for the comparison period before making "
        f"inventory or regional allocation decisions."
    )


def run(
    month: str,
    previous_month_csv: str,
    current_month_csv: str,
) -> dict:

    # Subtask 1: Load and validate the current-month feed
    is_valid, validation_errors = validate_feed(current_month_csv)

    # Subtask 2: Hard Stop if validation fails
    if not is_valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": validation_errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    # Load previous-month revenue by category
    with open(previous_month_csv, newline="") as file:
        previous_reader = csv.DictReader(file)
        previous_rows = list(previous_reader)

    previous_revenue = {
        row["category"]: float(row["revenue"])
        for row in previous_rows
    }

    prev_month = previous_rows[0]["month"]

    # Load current-month revenue by category
    with open(current_month_csv, newline="") as file:
        current_reader = csv.DictReader(file)
        current_revenue = {
            row["category"]: float(row["revenue"])
            for row in current_reader
        }

    # Subtask 3: Compute MoM growth for every category
    category_results = []

    for category, current_value in current_revenue.items():
        previous_value = previous_revenue[category]

        mom_pct = mom_growth(previous_value, current_value)

        category_results.append({
            "category": category,
            "previous_revenue": previous_value,
            "current_revenue": current_value,
            "mom_pct": mom_pct,
        })

    flagged_categories = []
    escalated_categories = []

    # Subtask 4: Classify every category
    for result in category_results:
        status = is_flagged(result["mom_pct"])

        if status == "flagged":
            flagged_categories.append(result)

        elif status == "escalate_exact_boundary":
            escalated_categories.append(result["category"])

    # Subtask 5: Sort flagged categories by absolute MoM magnitude
    flagged_categories.sort(
        key=lambda item: abs(item["mom_pct"]),
        reverse=True,
    )

    # Subtasks 6 and 7: Draft only the top 3 and suppress the rest
    top_flagged = flagged_categories[:3]

    suppressed_categories = [
        item["category"]
        for item in flagged_categories[3:]
    ]

    # Subtask 6: Draft messages for the top 3 flagged categories
    for item in top_flagged:
        item["drafted"] = True
        item["message"] = fill_prompt_template(
            category=item["category"],
            previous_revenue=item["previous_revenue"],
            current_revenue=item["current_revenue"],
            mom_pct=item["mom_pct"],
            month=month,
            prev_month=prev_month,
        )
    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": top_flagged,
        "suppressed_categories": suppressed_categories,
        "escalated_categories": escalated_categories,
        "action_taken": "drafted_and_held_for_approval",
    }