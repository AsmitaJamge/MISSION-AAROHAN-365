Name = input("Enter your Name:")
Age=int(input("Enter your Age:"))
Account_Balance=int(input("Enter your Account Balance:"))
if Age>=18 and Account_Balance>=1000:
    print("Transaction Allowed")
else:
    print("Transaction Denied")