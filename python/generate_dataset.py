import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------

NUM_TRANSACTIONS = 10000

cities = [
    "Dakar",
    "Thiès",
    "Saint-Louis",
    "Kaolack",
    "Ziguinchor"
]

payment_methods = [
    "Wave",
    "Orange Money",
    "Free Money",
    "Carte Bancaire"
]

transaction_types = [
    "Transfert",
    "Paiement",
    "Retrait"
]

device_types = [
    "Android",
    "iPhone"
]

# -----------------------------
# CLIENTS
# -----------------------------

customers = [f"CUST_{i}" for i in range(1, 1001)]

# historique simple des habitudes client
customer_profiles = {}

for customer in customers:
    customer_profiles[customer] = {
        "home_city": random.choice(cities),
        "avg_amount": random.randint(3000, 50000)
    }

# -----------------------------
# GENERATION DATASET
# -----------------------------

transactions = []

start_date = datetime(2025, 1, 1)

for transaction_id in range(1, NUM_TRANSACTIONS + 1):

    customer_id = random.choice(customers)

    profile = customer_profiles[customer_id]

    city = profile["home_city"]

    avg_amount = profile["avg_amount"]

    # heure normale majoritairement journée
    hour = random.choices(
        population=range(24),
        weights=[
            1,1,1,1,1,2,
            4,5,6,7,8,8,
            8,8,7,7,6,5,
            4,3,2,2,1,1
        ]
    )[0]

    minute = random.randint(0, 59)

    transaction_datetime = start_date + timedelta(
        days=random.randint(0, 180),
        hours=hour,
        minutes=minute
    )

    amount = round(
        np.random.normal(avg_amount, avg_amount * 0.5)
    )

    amount = max(amount, 500)

    payment_method = random.choice(payment_methods)

    transaction_type = random.choice(transaction_types)

    device_type = random.choice(device_types)

    fraud_flag = 0

    fraud_reason = "Normal"

    # ---------------------------------
    # LOGIQUE FRAUDE
    # ---------------------------------

    risk_score = 0

    # nuit
    if hour >= 1 and hour <= 4:
        risk_score += 25

    # gros montant inhabituel
    if amount > avg_amount * 5:
        risk_score += 40

    # ville inhabituelle
    if random.random() < 0.03:
        city = random.choice(cities)

        if city != profile["home_city"]:
            risk_score += 35

    # rafale transactions
    if random.random() < 0.02:
        risk_score += 30

    # fraude si score élevé
    if risk_score >= 35:
        fraud_flag = 1

        if amount > avg_amount * 5:
            fraud_reason = "Montant inhabituel"

        elif hour >= 1 and hour <= 4:
            fraud_reason = "Transaction nocturne"

        else:
            fraud_reason = "Comportement suspect"

    transactions.append({
        "transaction_id": transaction_id,
        "customer_id": customer_id,
        "transaction_datetime": transaction_datetime,
        "city": city,
        "payment_method": payment_method,
        "transaction_type": transaction_type,
        "device_type": device_type,
        "amount": amount,
        "risk_score": risk_score,
        "fraud_flag": fraud_flag,
        "fraud_reason": fraud_reason
    })

# -----------------------------
# DATAFRAME
# -----------------------------

df = pd.DataFrame(transactions)

# -----------------------------
# EXPORT CSV
# -----------------------------

df.to_csv(
    "data/transactions.csv",
    index=False
)

print("Dataset généré avec succès.")
print(df.head())