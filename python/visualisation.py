import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# CHARGER DATASET
# -----------------------------

df = pd.read_csv("data/transactions.csv")

# -----------------------------
# FRAUDES PAR VILLE
# -----------------------------

fraud_by_city = (
    df[df["fraud_flag"] == 1]
    .groupby("city")
    .size()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

fraud_by_city.plot(kind="bar")

plt.title("Fraudes par ville")

plt.xlabel("Ville")

plt.ylabel("Nombre de fraudes")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()

# -----------------------------
# FRAUDES PAR PAIEMENT
# -----------------------------

fraud_by_payment = (
    df[df["fraud_flag"] == 1]
    .groupby("payment_method")
    .size()
)

plt.figure(figsize=(8,8))

fraud_by_payment.plot(kind="pie", autopct='%1.1f%%')

plt.title("Répartition des fraudes par moyen de paiement")

plt.ylabel("")

plt.show()

# -----------------------------
# EVOLUTION TEMPORELLE DES FRAUDES
# -----------------------------

df["transaction_datetime"] = pd.to_datetime(
    df["transaction_datetime"]
)

df["transaction_date"] = (
    df["transaction_datetime"].dt.date
)

fraud_over_time = (
    df[df["fraud_flag"] == 1]
    .groupby("transaction_date")
    .size()
)

plt.figure(figsize=(12,6))

fraud_over_time.plot(kind="line")

plt.title("Evolution des fraudes dans le temps")

plt.xlabel("Date")

plt.ylabel("Nombre de fraudes")

plt.tight_layout()

plt.show()

# -----------------------------
# TOP CLIENTS SUSPECTS
# -----------------------------

top_suspicious = (
    df[df["fraud_flag"] == 1]
    .groupby("customer_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

top_suspicious.plot(kind="bar")

plt.title("Top 10 clients suspects")

plt.xlabel("Client")

plt.ylabel("Transactions frauduleuses")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()