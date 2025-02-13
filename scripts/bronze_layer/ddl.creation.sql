/*
🏦 Banking System Data Model & SQL Queries 💳
🚀 A powerful banking database model for financial data analysis, fraud detection, and SQL optimization!

⚠ Warning & Disclaimer ⚠
🚨 For educational & demonstration purposes only!
✔ Do NOT use real banking data.
✔ Ensure security protocols for sensitive data.
✔ Modify scripts before applying to production environments.

📌 Project Purpose
This repository provides a structured and scalable banking database to:
✔ Improve data integrity and query efficiency.
✔ Automate fraud detection & financial risk analysis.
✔ Enable advanced banking insights via SQL queries.
✔ Serve as a foundation for real-world banking applications.

🏦 Database Structure (30+ Tables)
📂 Core Banking – Customers, Accounts, Transactions
💳 Digital Payments – Credit Cards, Online Banking, Bill Payments
🏡 Loans & Credit – Loans, Repayments, Debt Collection
🔍 Fraud & Compliance – KYC, AML, Fraud Detection
📊 HR & Payroll – Employees, Salaries, Attendance
📈 Investments & Treasury – Stocks, Forex, Insurance

🎯 10,000+ Sample Data Rows for Realistic Testing & Analysis

⚡ Key SQL Features & Scripts
✅ Automated Database Setup – Structured CREATE TABLE & DROP TABLE scripts
✅ Data Population – Sample data generation for testing
✅ Fraud Detection Queries – Track suspicious transactions & financial crimes
✅ Financial KPIs – Identify high-value customers, active loans, and risk factors
✅ Security & Compliance Checks – Ensure banking regulations

🔥 Get Started!
📥 Clone the repository & explore structured database models.
⚡ Run SQL scripts to create, manage, and analyze banking data.
💡 Contribute & Collaborate – Suggestions & improvements welcome!

💬 Need Help? Open an issue & let's build a better banking system together! 🚀
*/

-- Drop and Create Customers Table
IF OBJECT_ID('bronze.customers', 'U') IS NOT NULL
    DROP TABLE bronze.customers;
CREATE TABLE bronze.customers (
    CustomerID INT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    DOB DATE,
    Email VARCHAR(255),
    PhoneNumber VARCHAR(50),
    Address TEXT,
    NationalID VARCHAR(50) UNIQUE,
    TaxID VARCHAR(50) UNIQUE,
    EmploymentStatus VARCHAR(50),
    AnnualIncome DECIMAL(15,2),
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);
GO

-- Drop and Create Accounts Table
IF OBJECT_ID('bronze.accounts', 'U') IS NOT NULL
    DROP TABLE bronze.accounts;
CREATE TABLE bronze.accounts (
    AccountID INT PRIMARY KEY,
    CustomerID INT,
    AccountType VARCHAR(50) CHECK (AccountType IN ('Savings', 'Checking', 'Business', 'Other')),
    Balance DECIMAL(15,2) DEFAULT 0.0,
    Currency VARCHAR(10),
    Status VARCHAR(50) CHECK (Status IN ('Active', 'Inactive', 'Closed')),
    BranchID INT,
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID),
    FOREIGN KEY (BranchID) REFERENCES bronze.branches(BranchID)
);
GO

-- Drop and Create Transactions Table
IF OBJECT_ID('bronze.transactions', 'U') IS NOT NULL
    DROP TABLE bronze.transactions;
CREATE TABLE bronze.transactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT,
    TransactionType VARCHAR(20) CHECK (TransactionType IN ('Deposit', 'Withdrawal', 'Transfer', 'Payment')),
    Amount DECIMAL(15,2),
    Currency VARCHAR(10),
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) CHECK (Status IN ('Pending', 'Completed', 'Failed')),
    ReferenceNo VARCHAR(255),
    FOREIGN KEY (AccountID) REFERENCES bronze.accounts(AccountID)
);
GO
-- Drop and Create Branches Table
IF OBJECT_ID('bronze.branches', 'U') IS NOT NULL
    DROP TABLE bronze.branches;
CREATE TABLE bronze.branches (
    BranchID INT PRIMARY KEY,
    BranchName VARCHAR(255),
    Address TEXT,
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    ManagerID INT,
    ContactNumber VARCHAR(50)
);
GO

-- Drop and Create Employees Table
IF OBJECT_ID('bronze.employees', 'U') IS NOT NULL
    DROP TABLE bronze.employees;
CREATE TABLE bronze.employees (
    EmployeeID INT PRIMARY KEY,
    BranchID INT,
    FullName VARCHAR(255),
    Position VARCHAR(100),
    Department VARCHAR(100),
    Salary DECIMAL(15,2),
    HireDate DATE,
    Status VARCHAR(50) CHECK (Status IN ('Active', 'Inactive', 'Terminated')),
    FOREIGN KEY (BranchID) REFERENCES bronze.branches(BranchID)
);
GO

-- Drop and Create CreditCards Table
IF OBJECT_ID('bronze.creditCards', 'U') IS NOT NULL
    DROP TABLE bronze.creditCards;
CREATE TABLE bronze.creditCards (
    CardID INT PRIMARY KEY,
    CustomerID INT,
    CardNumber VARCHAR(20) UNIQUE NOT NULL,
    CardType VARCHAR(50) CHECK (CardType IN ('Visa', 'MasterCard', 'Amex', 'Other')),
    CVV VARCHAR(10) NOT NULL,
    ExpiryDate DATE NOT NULL,
    Limit DECIMAL(15,2) NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('Active', 'Blocked', 'Expired')),
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create CreditCardTransactions Table
IF OBJECT_ID('bronze.creditCardTransactions', 'U') IS NOT NULL
    DROP TABLE bronze.creditCardTransactions;
CREATE TABLE bronze.creditCardTransactions (
    TransactionID INT PRIMARY KEY,
    CardID INT,
    Merchant VARCHAR(255) NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
    Currency VARCHAR(10) NOT NULL,
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) CHECK (Status IN ('Pending', 'Completed', 'Failed')),
    FOREIGN KEY (CardID) REFERENCES bronze.creditCards(CardID)
);
GO

-- Drop and Create OnlineBankingUsers Table
IF OBJECT_ID('bronze.onlineBankingUsers', 'U') IS NOT NULL
    DROP TABLE bronze.onlineBankingUsers;
CREATE TABLE bronze.onlineBankingUsers (
    UserID INT PRIMARY KEY,
    CustomerID INT,
    Username VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    LastLogin DATETIME,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create BillPayments Table
IF OBJECT_ID('bronze.billPayments', 'U') IS NOT NULL
    DROP TABLE bronze.billPayments;
CREATE TABLE bronze.billPayments (
    PaymentID INT PRIMARY KEY,
    CustomerID INT,
    BillerName VARCHAR(255) NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
    PaymentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50) CHECK (Status IN ('Pending', 'Completed', 'Failed')),
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create MobileBankingTransactions Table
IF OBJECT_ID('bronze.mobileBankingTransactions', 'U') IS NOT NULL
    DROP TABLE bronze.mobileBankingTransactions;
CREATE TABLE bronze.mobileBankingTransactions (
    TransactionID INT PRIMARY KEY,
    CustomerID INT,
    DeviceID VARCHAR(255) NOT NULL,
    AppVersion VARCHAR(50) NOT NULL,
    TransactionType VARCHAR(50) CHECK (TransactionType IN ('Deposit', 'Withdrawal', 'Transfer', 'Payment')),
    Amount DECIMAL(15,2) NOT NULL,
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create Loans Table
IF OBJECT_ID('bronze.loans', 'U') IS NOT NULL
    DROP TABLE bronze.loans;
CREATE TABLE bronze.loans (
    LoanID INT PRIMARY KEY,
    CustomerID INT,
    LoanType VARCHAR(50) CHECK (LoanType IN ('Mortgage', 'Personal', 'Auto', 'Business')),
    Amount DECIMAL(15,2) NOT NULL,
    InterestRate DECIMAL(5,2) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('Active', 'Closed', 'Defaulted')),
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create LoanPayments Table
IF OBJECT_ID('bronze.loanPayments', 'U') IS NOT NULL
    DROP TABLE bronze.loanPayments;
CREATE TABLE bronze.loanPayments (
    PaymentID INT PRIMARY KEY,
    LoanID INT,
    AmountPaid DECIMAL(15,2) NOT NULL,
    PaymentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    RemainingBalance DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (LoanID) REFERENCES bronze.loans(LoanID)
);
GO

-- Drop and Create CreditScores Table
IF OBJECT_ID('bronze.creditScores', 'U') IS NOT NULL
    DROP TABLE bronze.creditScores;
CREATE TABLE bronze.creditScores (
    CustomerID INT PRIMARY KEY,
    CreditScore INT CHECK (CreditScore BETWEEN 300 AND 850),
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create DebtCollection Table
IF OBJECT_ID('bronze.debtCollection', 'U') IS NOT NULL
    DROP TABLE bronze.debtCollection;
CREATE TABLE bronze.debtCollection (
    DebtID INT PRIMARY KEY,
    CustomerID INT,
    AmountDue DECIMAL(15,2) NOT NULL,
    DueDate DATE NOT NULL,
    CollectorAssigned VARCHAR(255),
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create KYC Table
IF OBJECT_ID('bronze.KYC', 'U') IS NOT NULL
    DROP TABLE bronze.KYC;
CREATE TABLE bronze.KYC (
    KYCID INT PRIMARY KEY,
    CustomerID INT,
    DocumentType VARCHAR(255) NOT NULL,
    DocumentNumber VARCHAR(255) UNIQUE NOT NULL,
    VerifiedBy VARCHAR(255) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create FraudDetection Table
IF OBJECT_ID('bronze.fraudDetection', 'U') IS NOT NULL
    DROP TABLE bronze.fraudDetection;
CREATE TABLE bronze.fraudDetection (
    FraudID INT PRIMARY KEY,
    CustomerID INT,
    TransactionID INT,
    RiskLevel VARCHAR(50) CHECK (RiskLevel IN ('Low', 'Medium', 'High')),
    ReportedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID),
    FOREIGN KEY (TransactionID) REFERENCES bronze.transactions(TransactionID)
);
GO

-- Drop and Create AML Cases Table
IF OBJECT_ID('bronze.amlCases', 'U') IS NOT NULL
    DROP TABLE bronze.amlCases;
CREATE TABLE bronze.amlCases (
    CaseID INT PRIMARY KEY,
    CustomerID INT,
    CaseType VARCHAR(255) NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('Open', 'Closed', 'Under Investigation')),
    InvestigatorID INT,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create RegulatoryReports Table
IF OBJECT_ID('bronze.regulatoryReports', 'U') IS NOT NULL
    DROP TABLE bronze.regulatoryReports;
CREATE TABLE bronze.regulatoryReports (
    ReportID INT PRIMARY KEY,
    ReportType VARCHAR(255) NOT NULL,
    SubmissionDate DATETIME DEFAULT CURRENT_TIMESTAMP
);
GO
-- Drop and Create Departments Table
IF OBJECT_ID('bronze.departments', 'U') IS NOT NULL
    DROP TABLE bronze.departments;
CREATE TABLE bronze.departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(255) NOT NULL,
    ManagerID INT
);
GO

-- Drop and Create Salaries Table
IF OBJECT_ID('bronze.salaries', 'U') IS NOT NULL
    DROP TABLE bronze.salaries;
CREATE TABLE bronze.salaries (
    SalaryID INT PRIMARY KEY,
    EmployeeID INT,
    BaseSalary DECIMAL(15,2) NOT NULL,
    Bonus DECIMAL(15,2),
    Deductions DECIMAL(15,2),
    PaymentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EmployeeID) REFERENCES bronze.employees(EmployeeID)
);
GO

-- Drop and Create EmployeeAttendance Table
IF OBJECT_ID('bronze.employeeAttendance', 'U') IS NOT NULL
    DROP TABLE bronze.employeeAttendance;
CREATE TABLE bronze.employeeAttendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeID INT,
    CheckInTime DATETIME NOT NULL,
    CheckOutTime DATETIME,
    TotalHours DECIMAL(5,2),
    FOREIGN KEY (EmployeeID) REFERENCES bronze.employees(EmployeeID)
);
GO

-- Drop and Create Investments Table
IF OBJECT_ID('bronze.investments', 'U') IS NOT NULL
    DROP TABLE bronze.investments;
CREATE TABLE bronze.investments (
    InvestmentID INT PRIMARY KEY,
    CustomerID INT,
    InvestmentType VARCHAR(255) NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
    ROI DECIMAL(5,2),
    MaturityDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create StockTradingAccounts Table
IF OBJECT_ID('bronze.stockTradingAccounts', 'U') IS NOT NULL
    DROP TABLE bronze.stockTradingAccounts;
CREATE TABLE bronze.stockTradingAccounts (
    AccountID INT PRIMARY KEY,
    CustomerID INT,
    BrokerageFirm VARCHAR(255) NOT NULL,
    TotalInvested DECIMAL(15,2) NOT NULL,
    CurrentValue DECIMAL(15,2),
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create ForeignExchange Table
IF OBJECT_ID('bronze.foreignExchange', 'U') IS NOT NULL
    DROP TABLE bronze.foreignExchange;
CREATE TABLE bronze.foreignExchange (
    FXID INT PRIMARY KEY,
    CustomerID INT,
    CurrencyPair VARCHAR(20) NOT NULL,
    ExchangeRate DECIMAL(10,6) NOT NULL,
    AmountExchanged DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create InsurancePolicies Table
IF OBJECT_ID('bronze.insurancePolicies', 'U') IS NOT NULL
    DROP TABLE bronze.insurancePolicies;
CREATE TABLE bronze.insurancePolicies (
    PolicyID INT PRIMARY KEY,
    CustomerID INT,
    InsuranceType VARCHAR(255) NOT NULL,
    PremiumAmount DECIMAL(15,2) NOT NULL,
    CoverageAmount DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create Claims Table
IF OBJECT_ID('bronze.claims', 'U') IS NOT NULL
    DROP TABLE bronze.claims;
CREATE TABLE bronze.claims (
    ClaimID INT PRIMARY KEY,
    PolicyID INT,
    ClaimAmount DECIMAL(15,2) NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('Pending', 'Approved', 'Rejected')),
    FiledDate DATE NOT NULL,
    FOREIGN KEY (PolicyID) REFERENCES bronze.insurancePolicies(PolicyID)
);
GO

-- Drop and Create UserAccessLogs Table
IF OBJECT_ID('bronze.userAccessLogs', 'U') IS NOT NULL
    DROP TABLE bronze.userAccessLogs;
CREATE TABLE bronze.userAccessLogs (
    LogID INT PRIMARY KEY,
    UserID INT,
    ActionType VARCHAR(255) NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES bronze.onlineBankingUsers(UserID)
);
GO

-- Drop and Create CyberSecurityIncidents Table
IF OBJECT_ID('bronze.cyberSecurityIncidents', 'U') IS NOT NULL
    DROP TABLE bronze.cyberSecurityIncidents;
CREATE TABLE bronze.cyberSecurityIncidents (
    IncidentID INT PRIMARY KEY,
    AffectedSystem VARCHAR(255) NOT NULL,
    ReportedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    ResolutionStatus VARCHAR(50) CHECK (ResolutionStatus IN ('Open', 'Resolved', 'Under Investigation'))
);
GO

-- Drop and Create Merchants Table
IF OBJECT_ID('bronze.merchants', 'U') IS NOT NULL
    DROP TABLE bronze.merchants;
CREATE TABLE bronze.merchants (
    MerchantID INT PRIMARY KEY,
    MerchantName VARCHAR(255) NOT NULL,
    Industry VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES bronze.customers(CustomerID)
);
GO

-- Drop and Create MerchantTransactions Table
IF OBJECT_ID('bronze.merchantTransactions', 'U') IS NOT NULL
    DROP TABLE bronze.merchantTransactions;
CREATE TABLE bronze.merchantTransactions (
    TransactionID INT PRIMARY KEY,
    MerchantID INT,
    Amount DECIMAL(15,2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (MerchantID) REFERENCES bronze.merchants(MerchantID)
);
GO

