import sqlite3

DB_PATH = "data/meesho_reseller.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

query = """
SELECT
    r.reseller_id,
    r.reseller_name,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM resellers AS r
LEFT JOIN orders AS o
    ON r.reseller_id = o.reseller_id
WHERE r.reseller_id = 'RS024'
GROUP BY
    r.reseller_id,
    r.reseller_name;
"""

cursor.execute(query)

rows = cursor.fetchall()

print(rows)

conn.close()