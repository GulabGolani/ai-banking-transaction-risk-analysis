-- PostgreSQL analysis queries
-- Load data/sample_transactions.csv into a table named transactions.

-- 1. Transaction volume and value by channel
SELECT channel,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr)::numeric, 2) AS total_value_inr,
       ROUND(AVG(amount_inr)::numeric, 2) AS average_value_inr
FROM transactions
GROUP BY channel
ORDER BY transaction_count DESC;

-- 2. Unusual high-value transactions
SELECT transaction_id, customer_id, transaction_date, amount_inr, channel, city
FROM transactions
WHERE amount_inr >= 50000
ORDER BY amount_inr DESC;

-- 3. Overnight activity (00:00–04:59)
SELECT transaction_id, transaction_date, amount_inr, channel, city
FROM transactions
WHERE transaction_hour BETWEEN 0 AND 4
ORDER BY transaction_hour, amount_inr DESC;

-- 4. Customer tenure segmentation
SELECT CASE WHEN customer_tenure_days < 30 THEN 'New (<30 days)'
            WHEN customer_tenure_days < 180 THEN 'Established (30–179 days)'
            ELSE 'Mature (180+ days)' END AS tenure_segment,
       COUNT(*) AS transaction_count,
       ROUND(AVG(amount_inr)::numeric, 2) AS avg_amount_inr
FROM transactions
GROUP BY tenure_segment
ORDER BY transaction_count DESC;

-- 5. Daily monitoring
SELECT DATE(transaction_date) AS transaction_day,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr)::numeric, 2) AS total_value_inr
FROM transactions
GROUP BY DATE(transaction_date)
ORDER BY transaction_day;

-- 6. Illustrative rule-based risk score
WITH scored AS (
  SELECT *,
    (CASE WHEN amount_inr >= 50000 THEN 40 ELSE 0 END) +
    (CASE WHEN transaction_hour BETWEEN 0 AND 4 THEN 25 ELSE 0 END) +
    (CASE WHEN customer_tenure_days < 30 THEN 20 ELSE 0 END) +
    (CASE WHEN channel IN ('UPI','Wallet') THEN 10 ELSE 0 END) AS risk_score
  FROM transactions
)
SELECT *,
       CASE WHEN risk_score >= 60 THEN 'High'
            WHEN risk_score >= 30 THEN 'Medium'
            ELSE 'Low' END AS priority
FROM scored
ORDER BY risk_score DESC, amount_inr DESC;
