# Fraud Detection Pipeline

## 📌 Objective
Identify high-risk users based on transaction behavior such as high transaction amount, frequency, and unusual timing.

---

## 🛠 Tools Used
- Python (Pandas)
- SQL
- Google Colab

---

## 📊 Dataset
- 1000 transaction records
- Columns: user_id, transaction_id, amount, device, location, transaction_time

---

## 🏗 Project Structure
- data/ → raw dataset
- notebooks/ → analysis using Pandas
- sql/ → fraud detection queries
- outputs/ → key insights

---

## ⚙️ Approach

### 1. Data Understanding
- Explored dataset using `.head()`, `.info()`, and `.describe()`
- Verified data quality and structure

### 2. Feature Engineering
- Extracted hour from transaction_time
- Created `is_night` feature for late-night transactions

### 3. Aggregation
- Calculated total transaction amount per user
- Counted number of transactions per user
- Counted night transactions per user

### 4. Fraud Detection Logic
Users are flagged as suspicious based on:
- High total transaction amount (> 200,000)
- High transaction frequency (> 15 transactions)
- High number of night transactions (≥ 4)

### 5. SQL Analysis
- Used GROUP BY for aggregation
- Applied CASE WHEN for conditional logic
- Used HAVING to filter aggregated results

---

## 🔍 Key Insights
- A small subset of users contributes to most suspicious transactions
- Night transactions are higher for certain users compared to others
- High-value transactions tend to occur during late-night hours
- Combining amount, frequency, and timing improves fraud detection

---

## 📊 Sample Output
- Identified a group of high-risk users based on defined fraud criteria
- Observed unusual patterns in transaction timing and value

---

## 🔄 Pipeline Extension
- Can be automated using scheduling tools like Airflow
- Can be connected to real-time transaction systems
- Thresholds can be refined using historical data

---

## 🚀 Conclusion
This project demonstrates how transaction data can be analyzed using Python and SQL to detect suspicious behavior. The approach can be extended into a real-time fraud detection system in production environments.
