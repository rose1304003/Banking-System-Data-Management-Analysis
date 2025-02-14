/*
=========================================================
🏦 BANKING SYSTEM ANALYTICS - SQL QUERIES
---------------------------------------------------------
⚠ WARNING: 
- This script is for EDUCATIONAL & DEMONSTRATION purposes only.
- Ensure proper database indexing for optimal performance.
- Test queries on a safe environment before execution.
=========================================================
*/

-- 🔹 Top 3 Customers with the Highest Total Balance Across All Accounts
SELECT 
    CustomerId, 
    SUM(Balance) AS TotalBalance
FROM bronze.accounts
GROUP BY CustomerId
ORDER BY TotalBalance DESC
LIMIT 3;
PRINT '✅ Retrieved top 3 customers with the highest total balance!';
GO

-- 🔹 Customers Who Have More Than One Active Loan
SELECT 
    CustomerID,
    COUNT(LoanID) AS Active_Loan
FROM bronze.loans
GROUP BY CustomerId
HAVING COUNT(LoanID) > 1
ORDER BY Active_Loan DESC;
PRINT '✅ Retrieved customers with more than one active loan!';
GO

-- 🔹 Transactions That Were Flagged as Fraudulent
SELECT t.*
FROM bronze.transactions t
JOIN bronze.fraudDetection f 
ON t.TransactionID = f.TransactionID;
PRINT '✅ Retrieved all transactions flagged as fraudulent!';
GO

-- 🔹 Total Loan Amount Issued Per Branch
SELECT 
    b.BranchID, 
    b.BranchName,
    SUM(l.Amount) AS TotalLoanIssued
FROM bronze.loans AS l
JOIN bronze.accounts AS a ON l.CustomerId = a.CustomerID
JOIN bronze.branches AS b ON a.BranchId = b.BranchId
GROUP BY b.BranchID, b.BranchName
ORDER BY TotalLoanIssued DESC;
PRINT '✅ Retrieved total loan amount issued per branch!';
GO

-- 🔹 Customers who made multiple large transactions (above $10,000) within a short time frame (less than 1 hour apart)
SELECT 
    t1.TransactionID, 
    c.CustomerId, 
    COUNT(*) AS TransactionCount
FROM bronze.transactions t1
JOIN bronze.transactions t2 
ON t1.AccountID = t2.AccountID
AND t1.TransactionID <> t2.TransactionID -- Avoid self-matching
AND ABS(TIMESTAMPDIFF(MINUTE, t1.TransactionDate, t2.TransactionDate)) < 60
JOIN bronze.accounts AS a ON t1.AccountID = a.AccountID
JOIN bronze.customers AS c ON a.CustomerID = c.CustomerId
WHERE t1.Amount > 10000 AND t2.Amount > 10000  -- Ensure both transactions are large
GROUP BY t1.TransactionID, c.CustomerID
HAVING COUNT(*) > 1;
PRINT '✅ Retrieved customers making multiple large transactions in a short timeframe!';
GO

-- 🔹 Customers who have made transactions from different countries within 10 minutes (Potential Fraud)
SELECT 
    c.CustomerID, 
    t1.TransactionID, t1.TransactionDate, t1.Amount, t1.Currency, b1.Country AS Country1, 
    t2.TransactionID AS TransactionID2, t2.TransactionDate AS TransactionDate2, b2.Country AS Country2
FROM bronze.transactions t1
JOIN bronze.transactions t2 
ON t1.AccountID = t2.AccountID
AND t1.TransactionID <> t2.TransactionID -- Avoid self-matching
AND ABS(TIMESTAMPDIFF(MINUTE, t1.TransactionDate, t2.TransactionDate)) <= 10
JOIN bronze.accounts a1 ON t1.AccountID = a1.AccountID
JOIN bronze.accounts a2 ON t2.AccountID = a2.AccountID
JOIN bronze.customers c ON a1.CustomerId = c.CustomerId
JOIN bronze.branches b1 ON a1.BranchID = b1.BranchID
JOIN bronze.branches b2 ON a2.BranchID = b2.BranchID
WHERE b1.Country <> b2.Country;
PRINT '✅ Retrieved customers with transactions from different countries within 10 minutes!';
GO

/*
=========================================================
🎯 FINAL NOTE:
- Queries are optimized for analysis but may require additional indexing for better performance.
- Consider creating views for frequently executed queries.
- Fraud detection queries should be integrated into real-time monitoring.
=========================================================
*/
