CREATE TABLE transactions (

    transaction_id INT,

    customer_id VARCHAR(50),

    transaction_datetime TIMESTAMP,

    city VARCHAR(50),

    payment_method VARCHAR(50),

    transaction_type VARCHAR(50),

    device_type VARCHAR(50),

    amount NUMERIC,

    risk_score INT,

    fraud_flag INT,

    fraud_reason VARCHAR(100)

);