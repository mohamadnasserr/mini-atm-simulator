balance = 1000.0

print("Welcome to the ATM")
print("Your balance is " , balance)
print("Below is the ATM options  ")

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

while True:
    option=int(input("Choose your option: "))
    if option == 1 :
        print("Available balance is :", balance)
        print("")
    elif option == 2:
        deposit_amount=float(input("Enter amount to deposit : "))
        balance = balance + deposit_amount
        print("Deposit successful. New balanace = ", balance)
        print("")
    elif option == 3 :
        withdraw_amount=float(input("Enter amount to withdraw : "))
        if withdraw_amount > balance:
            print("Insufficient funds!")
            print("")
        else : 
            balance = balance - withdraw_amount
            print("Withdrawal successful. New balance = ", balance)
            print("")

    elif option == 4 :
        print("Goodbye")
        break
