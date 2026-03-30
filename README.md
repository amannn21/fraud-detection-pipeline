# 🚨 Fraud Detection using Transaction Data

## 📌 Overview

This project analyzes transaction data to identify **potentially suspicious users** based on behavioral patterns such as transaction amount, frequency, and night-time activity.

A simple rule-based approach is used to flag users showing abnormal transaction behavior.

---

## 📊 Dataset

* File: `transactions.csv`
* Key columns:

  * `user_id` – Unique user identifier
  * `transaction_id` – Unique transaction ID
  * `amount` – Transaction value
  * `transaction_time` – Timestamp of transaction

---

## ⚙️ Methodology

### 1. Data Preparation

* Loaded dataset using Pandas
* Converted `transaction_time` to datetime
* Extracted transaction hour

---

### 2. Feature Engineering

* `hour` → Extracted from timestamp
* `is_night` → Flag for transactions before 6 AM

---

### 3. Aggregation

Grouped data by `user_id`:

* Total transaction amount
* Transaction count
* Night transaction count

---

### 4. Fraud Detection Logic

Users flagged as suspicious if:

* `total_amount > 200000`
* `txn_count > 15`
* `night_txn_count ≥ 4`

---

## 📈 Output

### Suspicious Users

Identifies users with:

* High spending
* High activity
* Unusual timing

---

### Distribution of Transactions

A histogram is used to analyze the distribution of total transaction amounts and identify outliers.

---

## 🔍 Key Observations

* High-frequency users with large total spend stand out clearly
* Night transactions contribute significantly to suspicious patterns
* Only a small subset of users meet all fraud conditions

---

## 💡 Limitations

* Rule-based detection (no ML model)
* Fixed thresholds
* No labeled fraud data

---

## 🚀 Future Improvements

* Build **Power BI dashboard** for visualization
* Add ML model for better prediction
* Use dynamic thresholds

---

## 🛠️ Tech Stack

* Python (Pandas)
* Matplotlib
* Google Colab

---

## ▶️ Run on Google Colab

1. Open the notebook in Colab
2. Upload the dataset:

```python
from google.colab import files
files.upload()
```

3. Run all cells

---

## 📊 Visualization

<img width="575" height="453" alt="visuals" src="https://github.com/user-attachments/assets/dde9a437-2150-49d6-8897-e5b7fcc37c74" />

---

## 📬 Contact

Aman Baikar
GitHub: https://github.com/amannn21
