balance = 1000

print("Welcome to the ATM")
print("Your balance is " , balance)
print("Below is the ATM actions  ")

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

while True:
    option=int(input("Enter your guess : "))
    if option ==4 :
        print("Goodbye")
        break
