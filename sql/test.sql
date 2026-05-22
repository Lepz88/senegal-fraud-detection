-- nbre total de transactions
SELECT
    COUNT(*) AS total_transactions
FROM transactions;

-- taux de fraudes
SELECT

    COUNT(CASE WHEN fraud_flag = 1 THEN 1 END) * 100.0
    / COUNT(*) AS fraud_rate

FROM transactions;

-- nbre total de fraudes    
SELECT
    COUNT(*) AS total_frauds
FROM transactions
WHERE fraud_flag = 1;

-- Fraudes par ville
SELECT
    city,
    COUNT(*) AS fraud_count
FROM transactions
WHERE fraud_flag = 1
GROUP BY city
ORDER BY fraud_count DESC;

-- Transactions nocturnes
SELECT
    transaction_id,
    customer_id,
    amount,
    city,
    transaction_datetime
FROM transactions
WHERE EXTRACT(HOUR FROM transaction_datetime)
BETWEEN 1 AND 4
AND fraud_flag = 1;

-- fraude par méthode de paiement
SELECT
    payment_method,
    COUNT(*) AS fraud_count
FROM transactions
WHERE fraud_flag = 1
GROUP BY payment_method
ORDER BY fraud_count DESC;

-- comportement habituel vs transaction actuelle.
WITH customer_avg AS (

    SELECT
        customer_id,
        AVG(amount) AS avg_amount
    FROM transactions
    GROUP BY customer_id

)

SELECT

    t.customer_id,

    t.amount,

    ROUND(c.avg_amount, 2) AS avg_amount,

    t.risk_score,

    t.city,

    t.transaction_datetime,

    CASE

        WHEN t.amount > c.avg_amount * 5 THEN 'Très élevé'

        WHEN t.amount > c.avg_amount * 3 THEN 'Elevé'

        WHEN t.amount > c.avg_amount * 2 THEN 'Moyen'

        ELSE 'Normal'

    END AS anomaly_level

FROM transactions t

JOIN customer_avg c
ON t.customer_id = c.customer_id

WHERE t.amount > c.avg_amount * 2

ORDER BY t.amount DESC;
-- Top clients suspects
SELECT
    customer_id,
    COUNT(*) AS suspicious_transactions
FROM transactions
WHERE fraud_flag = 1
GROUP BY customer_id
ORDER BY suspicious_transactions DESC
LIMIT 10;

-- Analyser les scores de risque
SELECT
    fraud_reason,
    AVG(risk_score) AS avg_risk
FROM transactions
WHERE fraud_flag = 1
GROUP BY fraud_reason
ORDER BY avg_risk DESC;

-- WINDOW FUNCTION

SELECT

    customer_id,

    transaction_datetime,

    amount,

    LAG(amount) OVER (
        PARTITION BY customer_id
        ORDER BY transaction_datetime
    ) AS previous_amount

FROM transactions;


-- Détection de pics anormaux
WITH transaction_comparison AS (

    SELECT

        customer_id,

        transaction_datetime,

        amount,

        LAG(amount) OVER (
            PARTITION BY customer_id
            ORDER BY transaction_datetime
        ) AS previous_amount

    FROM transactions

)

SELECT *
FROM transaction_comparison
WHERE amount > previous_amount * 10;


DELETE FROM transactions;