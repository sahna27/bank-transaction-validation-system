Bank Transaction Validator (main.py)

A Python script designed to evaluate bank account transaction requests based on account status, available balance, daily limits, and transaction counts.

📌 GitHub Repository Details

GitHub Summary

Python Bank Transaction Validator Script

GitHub Description (Under 350 characters)

A Python script (main.py) that evaluates bank transactions against security rules including account activity, available balance, daily expenditure limit, and transaction limits. Uses conditional statements (if-elif-else) to classify requests as approved, rejected, or requiring clarification.

📖 Overview

This program prompts users for key banking details and evaluates whether a financial transaction can proceed based on defined criteria:

Account Status must be "active".

Transaction Amount must be greater than $0$.

Account Balance must be greater than or equal to the transaction amount.

Transaction Amount must not exceed the daily limit.

Daily Transactions Count must not exceed $5$.

Decision Logic Matrix

Condition

Output

All security & balance conditions met

Transaction Approved.

Account_status is "inactive"

Transaction Rejected.

Any condition failed (e.g., limit exceeded, insufficient balance)

Clarification Required.

🚀 How to Run

Make sure Python 3 is installed on your system.

Clone or download this repository.

Open terminal/command prompt in the directory where main.py is saved.

Run the script:

python main.py



💻 Example Usage

Enter account status: active
Enter the transaction amount: 150
Enter the account balance: 500
Enter the daily limit: 1000
Enter the no. of transaction: 2

Transaction Approved.



✨ Key Features

Dynamic user inputs using appropriate numeric types (int and float).

Multi-variable boolean logic checks.

Flexible error pathing for non-active accounts vs. rule breaches.