SELECT 
    user_id,
    SUM(amount) AS total_amount,
    COUNT(transaction_id) AS txn_count,
    SUM(CASE WHEN EXTRACT(HOUR FROM transaction_time) < 6 THEN 1 ELSE 0 END) AS night_txn_count
FROM transactions
GROUP BY user_id
HAVING 
    SUM(amount) > 200000
    AND COUNT(transaction_id) > 15
    AND SUM(CASE WHEN EXTRACT(HOUR FROM transaction_time) < 6 THEN 1 ELSE 0 END) >= 4;
