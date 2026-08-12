"""wap for an ATM machine that check amount to be withdrawn 
checks amount:
- must be a multiple of 100,
- must not exceed the balance
- minimum balance after withdrawal must be 500
- else print message
"""
balance = 8000
amount = int(input("Enter amount to be withdrawn: "))

if amount % 100 == 0:
    if amount > balance:
        print("Cannot withdraw: insufficient balance")
    elif (balance - amount) < 500:
        print("Cannot withdraw: minimum balance must not be below 500")
    else:
        balance -= amount
        print(str(amount) + " withdrawn")
        print("Current balance: " + str(balance))
else:
    print("Only withdraw multiples of 100")