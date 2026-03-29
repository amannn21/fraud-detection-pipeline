# Fraud Detection Pipeline

## Objective
Identify high-risk users based on transaction patterns such as high amount, frequency, and unusual timing.

## Tools Used
- Python (Pandas)
- SQL
- Google Colab

## Project Structure
- data/ → raw dataset
- notebooks/ → analysis using Pandas
- sql/ → fraud detection queries
- outputs/ → key insights

## Approach
- Cleaned and explored dataset
- Created features like hour and night transactions
- Aggregated data at user level
- Applied fraud detection logic

## Key Insights
- Small group of users shows abnormal behavior
- Night transactions correlate with higher risk
- High frequency + high amount indicates suspicious activity

## Real-World Thinking
- This can be extended into ETL pipeline
- Thresholds can be dynamic using historical data
- Can be connected to real-time dashboard
