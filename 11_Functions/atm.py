#ATM 

def check_balance(balance):
    print("Current balanace is :: ",balance)


def deposit(balance):
    amt=float(input("Enter AMount to be dposited :: "))
    balance=balance+amt
    print("Amount Deposited Successfully !!!! ")
    print("Current Balance is :: ",balance)
    return balance

def withdraw(balance):
    amt=float(input("Enter AMount to be withdraw :: "))
    if amt>balance:
        print("Insufficient Balance to withdraw !!!")
    else:
        balance=balance-amt
        print("Amount Withdrawn Successfully !!!! ")
        print("Current Balance is :: ",balance)
        return balance


balance=10000
while True:
    print("1. Check Balance \n2. Deposit Amount \n3. Withdraw \n4. Exit ")
    choice=int(input("Enter Choice :: "))

    if choice==1:
        check_balance(balance)
    elif choice==2:
        balance=deposit(balance)
    elif choice==3:
        balance=withdraw(balance)
    elif choice==4:
        print("Thank you for using our atm")
        break
    else:
        print("Invalid Choice ")