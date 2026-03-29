import pandas as pd

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("/content/transactions.csv")

# -------------------------------
# Basic Check
# -------------------------------
print(df.head())
print(df.info())

# -------------------------------
# Feature Engineering
# -------------------------------
df['transaction_time'] = pd.to_datetime(df['transaction_time'])
df['hour'] = df['transaction_time'].dt.hour
df['is_night'] = (df['hour'] < 6).astype(int)

# -------------------------------
# Aggregation
# -------------------------------
summary = df.groupby('user_id').agg(
    total_amount=('amount', 'sum'),
    txn_count=('transaction_id', 'count'),
    night_txn_count=('is_night', 'sum')
).reset_index()

print(summary.head())

# -------------------------------
# Fraud Detection
# -------------------------------
fraud_users = summary[
    (summary['total_amount'] > 200000) &
    (summary['txn_count'] > 15) &
    (summary['night_txn_count'] >= 4)
]

print("Suspicious Users:")
print(fraud_users)

import matplotlib.pyplot as plt

summary['total_amount'].hist()
plt.title("Distribution of Total Transaction Amount")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.show()
