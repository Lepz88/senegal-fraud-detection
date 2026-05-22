import pandas as pd

# Charger le dataset
df = pd.read_csv("data/transactions.csv")

# -------------------------
# APERCU
# -------------------------

print("\n===== APERCU DATASET =====\n")

print(df.head())

# -------------------------
# INFORMATIONS
# -------------------------

print("\n===== INFORMATIONS =====\n")

print(df.info())

# -------------------------
# STATISTIQUES
# -------------------------

print("\n===== STATISTIQUES =====\n")

print(df.describe())

# -------------------------
# NOMBRE TOTAL FRAUDES
# -------------------------

total_frauds = df["fraud_flag"].sum()

print("\n===== TOTAL FRAUDES =====\n")

print(total_frauds)

# -------------------------
# FRAUDES PAR VILLE
# -------------------------

fraud_by_city = (
    df[df["fraud_flag"] == 1]
    .groupby("city")
    .size()
    .sort_values(ascending=False)
)

print("\n===== FRAUDES PAR VILLE =====\n")

print(fraud_by_city)

# -------------------------
# FRAUDES PAR PAIEMENT
# -------------------------

fraud_by_payment = (
    df[df["fraud_flag"] == 1]
    .groupby("payment_method")
    .size()
    .sort_values(ascending=False)
)

print("\n===== FRAUDES PAR PAIEMENT =====\n")

print(fraud_by_payment)