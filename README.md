# senegal-fraud-detection
# Senegal Fraud Detection Project

## Contexte

Ce projet simule un système de détection de fraude pour une fintech sénégalaise utilisant des transactions mobiles et bancaires.

L’objectif est d’identifier des comportements suspects à partir des données transactionnelles grâce à Python, SQL et Power BI.

---

# Problématique métier

Les services de mobile money et les plateformes fintech au Sénégal peuvent être confrontés à :

- transactions inhabituelles,
- montants anormalement élevés,
- activité nocturne suspecte,
- comportements clients anormaux,
- fraude sur mobile money.

Ce projet reproduit une mini architecture analytique de surveillance des risques.

---

# Technologies utilisées

- Python
- PostgreSQL
- SQL
- Power BI
- Pandas
- Matplotlib
- Faker

---

# Architecture du projet

```text
Python
(génération dataset)
        ↓

CSV
        ↓

PostgreSQL
(stockage)
        ↓

SQL Analytics
        ↓

Power BI Dashboard

Analyses réalisées
SQL
Fraudes par ville
Analyse comportementale client
Détection anomalies
Window Functions
CTE
Transactions nocturnes
Scoring de risque
Python
Génération du dataset
Visualisation des fraudes
Analyse exploratoire
Power BI
KPI transactions
KPI fraudes
Taux de fraude
Fraudes par ville
Evolution temporelle
Top clients suspects
Exemple de logique fraude
WITH customer_avg AS (

    SELECT
        customer_id,
        AVG(amount) AS avg_amount
    FROM transactions
    GROUP BY customer_id

)

SELECT *
FROM transactions t
JOIN customer_avg c
ON t.customer_id = c.customer_id
WHERE t.amount > c.avg_amount * 2;

Dashboard Power BI
Vue globale

https://github.com/Lepz88/senegal-fraud-detection/blob/main/images/dashboard_overview.png

Structure du projet
senegal-fraud-detection/
│
├── data/
├── python/
├── sql/
├── powerbi/
├── images/
├── README.md
└── requirements.txt
Résultats

Le projet permet :

d’identifier des comportements transactionnels suspects,
de détecter des anomalies,
de visualiser les risques fraude,
de construire un pipeline analytique complet.
Améliorations futures
Machine Learning
Détection temps réel
API fraude
Dashboard temps réel
Data Engineering pipeline
Auteur

Moulaye Idrisse Haïdara


---

