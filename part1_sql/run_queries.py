import sqlite3
import csv
import os


# ---------------------------------
# Project paths
# ---------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "meesho_reseller.db"
)

SQL_FILE = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "queries.sql"
)

OUTPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "output"
)


# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------
# Read SQL file
# ---------------------------------

with open(
    SQL_FILE,
    "r",
    encoding="utf-8"
) as f:

    sql = f.read()


# ---------------------------------
# Split SQL statements
# ---------------------------------

statements = [
    statement.strip()
    for statement in sql.split(";")
    if statement.strip()
]


# ---------------------------------
# Connect to database
# ---------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# ---------------------------------
# Output files for the 5 main queries
# ---------------------------------

output_files = [
    "monthly_category_revenue.csv",
    "region_revenue.csv",
    "top_resellers.csv",
    "zero_order_resellers.csv",
    "june_delivered_aov.csv"
]


# ---------------------------------
# Execute the 5 main queries
# ---------------------------------

query_number = 0

for statement in statements:

    # Skip the Query 4 demonstration
    if "count_star" in statement:
        continue

    query_number += 1

    cursor.execute(statement)

    rows = cursor.fetchall()

    columns = [
        description[0]
        for description in cursor.description
    ]

    output_file = os.path.join(
        OUTPUT_DIR,
        output_files[query_number - 1]
    )

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow(columns)
        writer.writerows(rows)

    print(
        f"Query {query_number} completed successfully. "
        f"Wrote {len(rows)} rows."
    )


# ---------------------------------
# Close database connection
# ---------------------------------

conn.close()