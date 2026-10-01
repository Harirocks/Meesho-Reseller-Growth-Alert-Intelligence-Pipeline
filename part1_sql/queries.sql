SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    CASE category
        WHEN 'Ethnic Wear' THEN 1
        WHEN 'Western Wear' THEN 2
        WHEN 'Kids Wear' THEN 3
        WHEN 'Home & Kitchen' THEN 4
        WHEN 'Beauty & Personal Care' THEN 5
    END;

    -- Query 2: Region-wise total revenue and order count

SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders AS o
JOIN resellers AS r
    ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY
    CASE r.region
        WHEN 'North' THEN 1
        WHEN 'West' THEN 2
        WHEN 'South' THEN 3
        WHEN 'East' THEN 4
    END;

-- Query 3: Top resellers by total spend

SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders AS o
JOIN resellers AS r
    ON o.reseller_id = r.reseller_id
GROUP BY
    r.reseller_id,
    r.reseller_name
HAVING SUM(o.quantity * o.unit_price) > 50000
ORDER BY total_spend DESC
LIMIT 5;

-- Query 4: Zero-order resellers

SELECT
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers AS r
LEFT JOIN orders AS o
    ON r.reseller_id = o.reseller_id
GROUP BY
    r.reseller_id,
    r.reseller_name,
    r.region
HAVING COUNT(o.order_id) = 0;

-- Query 4 demonstration:
-- Why COUNT(*) is wrong for zero-order detection

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

-- Query 5: June Delivered-only AOV

SELECT
    ROUND(
        SUM(quantity * unit_price) / COUNT(*),
        2
    ) AS aov
FROM orders
WHERE month = 'June'
  AND status = 'Delivered';