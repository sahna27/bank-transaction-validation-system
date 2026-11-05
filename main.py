Account_status= input("Enter account status:")
Transaction_amount = int(input("Enter the transaction amount:"))
Account_balance = float(input("Enter the account balance:"))
Daily_limit = float(input("Enter the daily limit:"))
Transactions = int(input("Enter the no. of transaction:"))

if Account_status == "active" and Transaction_amount > 0 and Account_balance >=Transaction_amount and Transaction_amount<= Daily_limit and Transactions<=5:
    print("Transaction Approved.")
elif Account_status=="inactive":
    print("Transaction Rejected.")
else:
    print("Clarification Required.")