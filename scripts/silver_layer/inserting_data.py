"""
=========================================================
🏦 BANKING SYSTEM DATABASE POPULATION SCRIPT
---------------------------------------------------------
⚠ WARNING:
- This script is for EDUCATIONAL & DEMONSTRATION purposes only.
- Do NOT use with real banking data.
- Ensure security protocols before running in a production environment.
=========================================================
"""

import mysql.connector
import random
import hashlib
from datetime import datetime, timedelta
import string

# 🎯 Generates a random alphanumeric string
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

# 🎯 Generates a random past date within the last 10 years
def random_date():
    return datetime.now() - timedelta(days=random.randint(0, 3650))

# 🎯 Establishes a connection to the MySQL database
def connect_db():
    try:
        conn = mysql.connector.connect(
            database="Banking_system",
            user="root",
            password="Robiya@12345",
            host="localhost",
            port=3306
        )
        print("✅ Database connection successful!")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database connection failed: {err}")
        exit(1)  # Stops execution if connection fails

# 🎯 Populates the Customers table
def populate_customers(cursor):
    print("📌 Populating Customers table...")
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO Customers (CustomerID, FullName, DOB, Email, PhoneNumber, Address, NationalID, TaxID, EmploymentStatus, AnnualIncome, CreatedAt, UpdatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
        """, (i, random_string(), random_date(), f"{random_string()}@example.com", '998' + str(random.randint(100000000, 999999999)), random_string(), random_string(), random_string(), 'Employed', random.randint(10000, 100000)))
    print("✅ Customers table populated!")

# 🎯 Populates the Branches table
def populate_branches(cursor):
    print("📌 Populating Branches table...")
    for i in range(1, 51):
        cursor.execute("""
            INSERT INTO Branches (BranchID, BranchName, Address, City, State, Country, ManagerID, ContactNumber)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (i, random_string(), random_string(), random_string(), random_string(), 'Uzbekistan', random.randint(1, 100), '998' + str(random.randint(100000000, 999999999))))
    print("✅ Branches table populated!")

# 🎯 Populates the Accounts table
def populate_accounts(cursor):
    print("📌 Populating Accounts table...")
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO Accounts (AccountID, CustomerID, AccountType, Balance, Currency, Status, BranchID, CreatedDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        """, (i, random.randint(10001, 20000), random.choice(['Savings', 'Checking', 'Business']), random.uniform(0, 10000), 'USD', 'Active', random.randint(1, 50)))
    print("✅ Accounts table populated!")

# 🎯 Populates the Transactions table
def populate_transactions(cursor):
    print("📌 Populating Transactions table...")
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO Transactions (TransactionID, AccountID, TransactionType, Amount, Currency, TransactionDate, Status, ReferenceNo)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s, %s)
        """, (i, random.randint(10001, 20000), random.choice(['Deposit', 'Withdrawal', 'Transfer', 'Payment']), random.uniform(0, 5000), 'USD', 'Completed', random_string()))
    print("✅ Transactions table populated!")

# 🎯 Populates the Employees table
def populate_employees(cursor):
    print("📌 Populating Employees table...")
    for i in range(1, 101):
        cursor.execute("""
            INSERT INTO Employees (EmployeeID, BranchID, FullName, Position, Department, Salary, HireDate, Status)
            VALUES (%s, %s, %s, %s, %s, %s, NOW(), %s)
        """, (i, random.randint(1, 50), random_string(), random.choice(['Manager', 'Teller', 'Clerk']), 'Finance', random.randint(30000, 80000), 'Active'))
    print("✅ Employees table populated!")

# 🎯 Populates the Credit Cards table
def populate_credit_cards(cursor):
    print("📌 Populating CreditCards table...")
    for i in range(10001, 20001):
        expiry_date = (datetime.now() + timedelta(days=random.randint(730, 1825))).strftime('%Y-%m-%d')
        cursor.execute("""
            INSERT INTO CreditCards (CardID, CustomerID, CardNumber, CardType, CVV, ExpiryDate, Limit, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            i,
            random.randint(10001, 20000),
            str(random.randint(4000000000000000, 4999999999999999)),
            random.choice(['Visa', 'MasterCard', 'Amex', 'Other']),
            random.randint(100, 999),
            expiry_date,
            random.randint(1000, 5000),
            random.choice(['Active', 'Blocked', 'Expired'])
        ))
    print("✅ CreditCards table populated!")

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def populate_credit_card_transactions(cursor):
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO CreditCardTransactions (TransactionID, CardID, Merchant, Amount, Currency, TransactionDate, Status)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            i,  # TransactionID
            random.randint(10001, 20000),  # CardID
            random_string(),  # Merchant
            round(random.uniform(10, 1000), 2),  # Amount
            'USD',  # Currency
            random.choice(['Pending', 'Completed', 'Failed'])  # Status
        ))

def populate_online_banking_users(cursor):
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO OnlineBankingUsers (UserID, CustomerID, Username, PasswordHash, LastLogin)
            VALUES (%s, %s, %s, %s, NOW())
        """, (i, random.randint(10001, 20000), random_string(), hashlib.sha256(random_string().encode()).hexdigest()))

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))
def populate_bill_payments(cursor):
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO BillPayments (PaymentID, CustomerID, BillerName, Amount, PaymentDate, Status)
            VALUES (%s, %s, %s, %s, NOW(), %s)
        """, (
            i,  # PaymentID
            random.randint(10001, 20000),  # CustomerID
            random_string(),  # BillerName
            round(random.uniform(10, 500), 2),  # Amount
            random.choice(['Pending', 'Completed', 'Failed'])  # Status
        ))
def populate_mobile_banking_transactions(cursor):
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO MobileBankingTransactions (TransactionID, CustomerID, DeviceID, AppVersion, TransactionType, Amount, TransactionDate)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
        """, (
            i,  # TransactionID
            random.randint(10001, 20000),  # CustomerID
            random_string(),  # DeviceID
            '1.0',  # AppVersion
            random.choice(['Deposit', 'Withdrawal', 'Transfer', 'Payment']),  # TransactionType
            round(random.uniform(10, 500), 2)  # Amount
        ))
def populate_loans(cursor):
    for i in range(10001, 20001):
        cursor.execute("""
            INSERT INTO Loans (LoanID, CustomerID, LoanType, Amount, InterestRate, StartDate, EndDate, Status)
            VALUES (%s, %s, %s, %s, %s, NOW() - INTERVAL %s DAY, NOW() + INTERVAL %s DAY, %s)
        """, (
            i, 
            random.randint(10001, 20000), 
            random.choice(['Mortgage', 'Personal', 'Auto', 'Business']), 
            round(random.uniform(1000, 50000), 2),  # Loan amount
            round(random.uniform(1.5, 10.0), 2),  # Interest rate
            random.randint(30, 365 * 5),  # Start date in past
            random.randint(365, 365 * 10),  # End date in future
            random.choice(['Active', 'Closed', 'Defaulted'])
        ))
def populate_loan_payments(cursor):
    for i in range(10001, 20001):  # Generating PaymentID in range
        loan_id = random.randint(10001, 20000)  # Random existing LoanID
        amount_paid = round(random.uniform(100, 5000), 2)  # Random payment amount
        remaining_balance = round(random.uniform(0, 45000), 2)  # Random remaining balance

        cursor.execute("""
            INSERT INTO LoanPayments (PaymentID, LoanID, AmountPaid, PaymentDate, RemainingBalance)
            VALUES (%s, %s, %s, NOW(), %s)
        """, (i, loan_id, amount_paid, remaining_balance))


#def populate_credit_scores(cursor):
    for customer_id in range(10001, 20001):  # Assuming CustomerIDs exist in this range
        credit_score = random.randint(300, 850)  # Random credit score within valid range

        cursor.execute("""
            INSERT INTO CreditScores (CustomerID, CreditScore, UpdatedAt)
            VALUES (%s, %s, NOW())
        """, (customer_id, credit_score))

#def populate_debt_collection(cursor):
    collectors = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Noah Brown", "Unassigned"]  # Possible collectors

    for debt_id in range(10001, 20001):  # Generating DebtID
        customer_id = random.randint(10001, 20000)  # Random existing CustomerID
        amount_due = round(random.uniform(100, 20000), 2)  # Random due amount
        due_date = (datetime.now() + timedelta(days=random.randint(-90, 90))).strftime('%Y-%m-%d')  # Past or future due dates
        collector_assigned = random.choice(collectors)  # Assign collector or leave unassigned

        cursor.execute("""
            INSERT INTO DebtCollection (DebtID, CustomerID, AmountDue, DueDate, CollectorAssigned)
            VALUES (%s, %s, %s, %s, %s)
        """, (debt_id, customer_id, amount_due, due_date, collector_assigned))


#def populate_kyc(cursor):
    document_types = ["Passport", "Driver's License", "National ID", "Residence Permit"]
    verifiers = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Anna Lee"]
    used_document_numbers = set()  # Store generated document numbers to ensure uniqueness

    for kyc_id in range(10001, 20001):  # Generating KYCID
        customer_id = random.randint(10001, 20000)  # Random existing CustomerID
        document_type = random.choice(document_types)  # Random document type

        # Generate a unique document number
        while True:
            document_number = f"{document_type[:2].upper()}{random.randint(100000, 999999)}"
            if document_number not in used_document_numbers:
                used_document_numbers.add(document_number)
                break  # Exit loop if unique

        verified_by = random.choice(verifiers)  # Random verifier

        cursor.execute("""
            INSERT INTO KYC (KYCID, CustomerID, DocumentType, DocumentNumber, VerifiedBy)
            VALUES (%s, %s, %s, %s, %s)
        """, (kyc_id, customer_id, document_type, document_number, verified_by))

#def populate_fraud_detection(cursor):
    risk_levels = ['Low', 'Medium', 'High']

    for fraud_id in range(10001, 11001):  # Generate 1000 fraud cases
        customer_id = random.randint(10001, 20000)  # Existing CustomerID
        transaction_id = random.randint(10001, 20000)  # FIXED: Ensure TransactionID exists
        risk_level = random.choice(risk_levels)  # Random risk level

        # Generate a random reported date within the last 2 years
        days_offset = random.randint(1, 730)  # Up to 2 years back
        reported_date = datetime.now() - timedelta(days=days_offset)

        cursor.execute("""
            INSERT INTO FraudDetection (FraudID, CustomerID, TransactionID, RiskLevel, ReportedDate)
            VALUES (%s, %s, %s, %s, %s)
        """, (fraud_id, customer_id, transaction_id, risk_level, reported_date))

#def populate_aml_cases(cursor):
    case_types = ["Money Laundering", "Terrorist Financing", "Fraud", "Suspicious Transaction"]
    statuses = ["Open", "Closed", "Under Investigation"]

    for case_id in range(30001, 31001):  # Generate 1000 AML cases
        customer_id = random.randint(10001, 20000)  # Ensure CustomerID exists
        investigator_id = random.randint(5001, 6000)  # Assuming InvestigatorID range
        case_type = random.choice(case_types)  # Random case type
        status = random.choice(statuses)  # Random case status

        # Generate a random reported date within the last 2 years
        days_offset = random.randint(1, 730)  # Up to 2 years back
        reported_date = datetime.now() - timedelta(days=days_offset)

        cursor.execute("""
            INSERT INTO AmlCases (CaseID, CustomerID, CaseType, Status, InvestigatorID)
            VALUES (%s, %s, %s, %s, %s)
        """, (case_id, customer_id, case_type, status, investigator_id))



#def populate_regulatory_reports(cursor):
    report_types = ["Suspicious Activity Report", "Currency Transaction Report", "Compliance Audit", "Financial Statement"]

    for report_id in range(40001, 41001):  # Generate 1000 reports
        report_type = random.choice(report_types)  # Random report type

        # Generate a random submission date within the last 5 years
        days_offset = random.randint(1, 1825)  # Up to 5 years back
        submission_date = datetime.now() - timedelta(days=days_offset)

        cursor.execute("""
            INSERT INTO RegulatoryReports (ReportID, ReportType, SubmissionDate)
            VALUES (%s, %s, %s)
        """, (report_id, report_type, submission_date))

#def populate_departments(cursor):
    department_names = [
        "Finance", "Human Resources", "IT", "Risk Management",
        "Compliance", "Legal", "Operations", "Customer Service"
    ]

    for dept_id in range(1, len(department_names) + 1):  # Assuming 8 departments
        department_name = department_names[dept_id - 1]
        manager_id = random.randint(10001, 20000)  # Assuming ManagerID exists in Employees table

        cursor.execute("""
            INSERT INTO Departments (DepartmentID, DepartmentName, ManagerID)
            VALUES (%s, %s, %s)
        """, (dept_id, department_name, manager_id))

#def populate_salaries(cursor):
    cursor.execute("SELECT EmployeeID FROM Employees")  # Fetch existing EmployeeIDs
    employee_ids = [row[0] for row in cursor.fetchall()]  # Extract EmployeeIDs from result

    if not employee_ids:  # If no employees exist, avoid inserting salaries
        print("No Employee records found. Skipping Salaries population.")
        return  

    for salary_id in range(10001, 11001):  # Generate 1000 salary records
        employee_id = random.choice(employee_ids)  # Ensure EmployeeID exists
        base_salary = round(random.uniform(30000, 150000), 2)  # Base salary range
        bonus = round(random.uniform(1000, 10000), 2) if random.random() < 0.7 else 0  # 70% chance of bonus
        deductions = round(random.uniform(500, 5000), 2) if random.random() < 0.5 else 0  # 50% chance of deductions
        payment_date = datetime.now() - timedelta(days=random.randint(0, 365))  # Random date in the past year

        cursor.execute("""
            INSERT INTO Salaries (SalaryID, EmployeeID, BaseSalary, Bonus, Deductions, PaymentDate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (salary_id, employee_id, base_salary, bonus, deductions, payment_date))




#def populate_employee_attendance(cursor):
    cursor.execute("SELECT EmployeeID FROM Employees")  # Fetch existing EmployeeIDs
    employee_ids = [row[0] for row in cursor.fetchall()]  # Extract EmployeeIDs

    if not employee_ids:  # If no employees exist, avoid inserting attendance records
        print("No Employee records found. Skipping EmployeeAttendance population.")
        return  

    for attendance_id in range(10001, 11001):  # Generate 1000 attendance records
        employee_id = random.choice(employee_ids)  # Ensure EmployeeID exists
        check_in_time = datetime.now() - timedelta(days=random.randint(1, 30), hours=random.randint(8, 10))  # Random check-in within last 30 days
        check_out_time = check_in_time + timedelta(hours=random.randint(4, 10))  # Random check-out (4 to 10 hours later)
        total_hours = round((check_out_time - check_in_time).total_seconds() / 3600, 2)  # Calculate total hours worked

        cursor.execute("""
            INSERT INTO EmployeeAttendance (AttendanceID, EmployeeID, CheckInTime, CheckOutTime, TotalHours)
            VALUES (%s, %s, %s, %s, %s)
        """, (attendance_id, employee_id, check_in_time, check_out_time, total_hours))

#def populate_investments(cursor):
    cursor.execute("SELECT CustomerID FROM Customers")  # Fetch existing CustomerIDs
    customer_ids = [row[0] for row in cursor.fetchall()]  # Extract valid CustomerIDs

    if not customer_ids:  # If no customers exist, skip the process
        print("No Customer records found. Skipping Investments population.")
        return  

    investment_types = ['Stocks', 'Bonds', 'Mutual Funds', 'Real Estate', 'Cryptocurrency']

    for investment_id in range(10001, 11001):  # Generate 1000 investment records
        customer_id = random.choice(customer_ids)  # Ensure valid CustomerID
        investment_type = random.choice(investment_types)  # Select random investment type
        amount = round(random.uniform(500, 50000), 2)  # Investment amount between $500 - $50,000
        roi = round(random.uniform(1.5, 15.0), 2)  # ROI between 1.5% and 15%
        maturity_date = datetime.now() + timedelta(days=random.randint(30, 1825))  # Random maturity date (30 days - 5 years)

        cursor.execute("""
            INSERT INTO Investments (InvestmentID, CustomerID, InvestmentType, Amount, ROI, MaturityDate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (investment_id, customer_id, investment_type, amount, roi, maturity_date))



#def populate_stock_trading_accounts(cursor):
    # Fetch existing CustomerIDs to maintain referential integrity
    cursor.execute("SELECT CustomerID FROM Customers")  
    customer_ids = [row[0] for row in cursor.fetchall()]  

    if not customer_ids:  
        print("No Customer records found. Skipping Stock Trading Accounts population.")
        return  

    brokerage_firms = ['E-Trade', 'Robinhood', 'Charles Schwab', 'Fidelity', 'Vanguard']

    records = []  # Collect data before bulk insert
    for account_id in range(20001, 21001):  # Generate 1000 stock trading accounts
        customer_id = random.choice(customer_ids)  
        brokerage_firm = random.choice(brokerage_firms)  
        total_invested = round(random.uniform(1000, 100000), 2)  
        current_value = total_invested * round(random.uniform(0.8, 1.5), 2)  # Simulate gains/losses

        records.append((account_id, customer_id, brokerage_firm, total_invested, current_value))

    # Execute batch insert for better performance
    cursor.executemany("""
        INSERT INTO StockTradingAccounts (AccountID, CustomerID, BrokerageFirm, TotalInvested, CurrentValue)
        VALUES (%s, %s, %s, %s, %s)
    """, records)

#def populate_foreign_exchange(cursor):
    # Fetch existing CustomerIDs to maintain referential integrity
    cursor.execute("SELECT CustomerID FROM Customers")  
    customer_ids = [row[0] for row in cursor.fetchall()]  

    if not customer_ids:  
        print("No Customer records found. Skipping Foreign Exchange population.")
        return  

    currency_pairs = ['USD/EUR', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CHF', 'EUR/GBP', 'EUR/JPY']
    
    records = []  # Collect data before bulk insert
    for fx_id in range(30001, 31001):  # Generate 1000 FX transactions
        customer_id = random.choice(customer_ids)  
        currency_pair = random.choice(currency_pairs)  
        exchange_rate = round(random.uniform(0.5, 1.5), 6)  # Random exchange rate
        amount_exchanged = round(random.uniform(100, 50000), 2)  

        records.append((fx_id, customer_id, currency_pair, exchange_rate, amount_exchanged))

    # Execute batch insert for better performance
    cursor.executemany("""
        INSERT INTO ForeignExchange (FXID, CustomerID, CurrencyPair, ExchangeRate, AmountExchanged)
        VALUES (%s, %s, %s, %s, %s)
    """, records)

#def populate_insurance_policies(cursor):
    # Fetch existing CustomerIDs to ensure valid references
    cursor.execute("SELECT CustomerID FROM Customers")  
    customer_ids = [row[0] for row in cursor.fetchall()]  

    if not customer_ids:  
        print("No Customer records found. Skipping Insurance Policies population.")
        return  

    insurance_types = ['Health', 'Life', 'Auto', 'Home', 'Travel', 'Business']
    
    records = []  # Collect data before bulk insert
    for policy_id in range(40001, 41001):  # Generate 1000 insurance policies
        customer_id = random.choice(customer_ids)  
        insurance_type = random.choice(insurance_types)  
        premium_amount = round(random.uniform(50, 2000), 2)  # Monthly premium: $50 - $2000
        coverage_amount = round(premium_amount * random.uniform(50, 200), 2)  # Coverage: 50x - 200x of premium

        records.append((policy_id, customer_id, insurance_type, premium_amount, coverage_amount))

    # Execute batch insert for better performance
    cursor.executemany("""
        INSERT INTO InsurancePolicies (PolicyID, CustomerID, InsuranceType, PremiumAmount, CoverageAmount)
        VALUES (%s, %s, %s, %s, %s)
    """, records)

#def populate_claims(cursor):
    # Fetch existing PolicyIDs to ensure valid references
    cursor.execute("SELECT PolicyID FROM InsurancePolicies")  
    policy_ids = [row[0] for row in cursor.fetchall()]  

    if not policy_ids:  
        print("No Insurance Policy records found. Skipping Claims population.")
        return  

    statuses = ['Pending', 'Approved', 'Rejected']
    
    records = []  # Collect data before bulk insert
    for claim_id in range(50001, 51001):  # Generate 1000 claims
        policy_id = random.choice(policy_ids)  
        claim_amount = round(random.uniform(100, 50000), 2)  # Claim between $100 - $50,000
        status = random.choice(statuses)  
        filed_date = datetime.now() - timedelta(days=random.randint(1, 365))  # Filed within the last year

        records.append((claim_id, policy_id, claim_amount, status, filed_date))

    # Execute batch insert for better performance
    cursor.executemany("""
        INSERT INTO Claims (ClaimID, PolicyID, ClaimAmount, Status, FiledDate)
        VALUES (%s, %s, %s, %s, %s)
    """, records)


#def populate_user_access_logs(cursor):
    # Fetch existing UserIDs from OnlineBankingUsers table
    cursor.execute("SELECT UserID FROM OnlineBankingUsers")
    user_ids = [row[0] for row in cursor.fetchall()]

    if not user_ids:
        print("No Online Banking User records found. Skipping UserAccessLogs population.")
        return  

    action_types = ['Login', 'Logout', 'Password Change', 'Fund Transfer', 'Bill Payment', 'Profile Update']
    
    records = []  # Collect data before bulk insert
    for log_id in range(20001, 21001):  # Generate 1000 log entries
        user_id = random.choice(user_ids)
        action_type = random.choice(action_types)
        timestamp = datetime.now() - timedelta(days=random.randint(1, 365))  # Random past date within the last year

        records.append((log_id, user_id, action_type, timestamp))

    # Batch insert for efficiency
    cursor.executemany("""
        INSERT INTO UserAccessLogs (LogID, UserID, ActionType, Timestamp)
        VALUES (%s, %s, %s, %s)
    """, records)


#def populate_cyber_security_incidents(cursor):
    # Possible affected systems
    affected_systems = ['Firewall', 'Database Server', 'Payment Gateway', 'User Authentication', 'Email System']
    
    resolution_statuses = ['Open', 'Resolved', 'Under Investigation']
    
    records = []  # Collect data before batch insert
    for incident_id in range(30001, 30101):  # Generate 100 incident records
        affected_system = random.choice(affected_systems)
        reported_date = datetime.now() - timedelta(days=random.randint(1, 365))  # Random past date within a year
        resolution_status = random.choice(resolution_statuses)

        records.append((incident_id, affected_system, reported_date, resolution_status))

    # Batch insert for efficiency
    cursor.executemany("""
        INSERT INTO CyberSecurityIncidents (IncidentID, AffectedSystem, ReportedDate, ResolutionStatus)
        VALUES (%s, %s, %s, %s)
    """, records)


#def populate_merchants(cursor):
    merchant_names = ["Amazon", "Walmart", "Apple Store", "Tesla", "Google Store", "Starbucks", "McDonald's", "Nike", "Adidas", "IKEA"]
    industries = ["Retail", "E-commerce", "Technology", "Automotive", "Finance", "Food & Beverage", "Fashion"]
    locations = ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston", "Seattle", "Miami", "Boston", "Dallas", "Atlanta"]

    cursor.execute("SELECT CustomerID FROM Customers")  # Fetch existing CustomerIDs
    customer_ids = [row[0] for row in cursor.fetchall()]  # Extract valid CustomerIDs

    records = []  # Collect data before batch insert
    for merchant_id in range(40001, 40101):  # Generate 100 merchant records
        merchant_name = random.choice(merchant_names)
        industry = random.choice(industries)
        location = random.choice(locations)
        customer_id = random.choice(customer_ids) if customer_ids else None  # Assign customer if available

        records.append((merchant_id, merchant_name, industry, location, customer_id))

    # Batch insert for efficiency
    cursor.executemany("""
        INSERT INTO Merchants (MerchantID, MerchantName, Industry, Location, CustomerID)
        VALUES (%s, %s, %s, %s, %s)
    """, records)


def populate_merchant_transactions(cursor):
    cursor.execute("SELECT MerchantID FROM Merchants")  # Fetch existing MerchantIDs
    merchant_ids = [row[0] for row in cursor.fetchall()]  # Extract valid MerchantIDs

    if not merchant_ids:  # If no merchants exist, skip the process
        print("No Merchant records found. Skipping Merchant Transactions population.")
        return  

    payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash', 'Cryptocurrency']
    
    records = []  # Collect data before batch insert
    for transaction_id in range(50001, 50201):  # Generate 200 transactions
        merchant_id = random.choice(merchant_ids)  # Ensure valid MerchantID
        amount = round(random.uniform(5, 5000), 2)  # Transaction amount between $5 - $5000
        payment_method = random.choice(payment_methods)  # Random payment method
        transaction_date = datetime.now() - timedelta(days=random.randint(1, 365))  # Random date within the last year

        records.append((transaction_id, merchant_id, amount, payment_method, transaction_date))

    # Batch insert for efficiency
    cursor.executemany("""
        INSERT INTO MerchantTransactions (TransactionID, MerchantID, Amount, PaymentMethod, TransactionDate)
        VALUES (%s, %s, %s, %s, %s)
    """, records)


# 🎯 Runs all population functions in order
def main():
    conn = connect_db()
    cursor = conn.cursor()

    # Run population scripts
    populate_customers(cursor)
    populate_branches(cursor)
    populate_accounts(cursor)
    populate_transactions(cursor)
    populate_employees(cursor)
    populate_credit_cards(cursor)
    populate_customers(cursor)
    populate_branches(cursor)
    populate_accounts(cursor)
    populate_transactions(cursor)
    populate_employees(cursor)
    populate_credit_cards(cursor)
    populate_credit_card_transactions(cursor)
    populate_online_banking_users(cursor)
    populate_bill_payments(cursor)
    populate_mobile_banking_transactions(cursor)
    populate_loans(cursor)
    populate_loan_payments(cursor)
    populate_credit_scores(cursor)
    populate_debt_collection(cursor)
    populate_kyc(cursor)
    populate_fraud_detection(cursor)
    populate_aml_cases(cursor)
    populate_regulatory_reports(cursor)
    populate_departments(cursor)
    populate_salaries(cursor)
    populate_employee_attendance(cursor)
    populate_investments(cursor)
    populate_stock_trading_accounts(cursor)
    populate_foreign_exchange(cursor)
    populate_insurance_policies(cursor)
    populate_claims(cursor)
    populate_user_access_logs(cursor)
    populate_cyber_security_incidents(cursor)
    populate_merchants(cursor)
    populate_merchant_transactions(cursor)

    conn.commit()  # Commit changes
    cursor.close()
    conn.close()

    print("✅ All tables populated successfully!")

if __name__ == "__main__":
    main()

"""
=========================================================
🎯 FINAL NOTE:
- Ensure MySQL service is running before executing.
- Modify connection details if needed.
- Use `LIMIT` and `BATCH INSERTS` for large-scale data generation.
- Consider indexing for faster performance.
=========================================================
"""
