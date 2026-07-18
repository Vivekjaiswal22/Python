print ("=============================== \n       Welcome To A.T.M.      \n===============================")
print(" ")
print ("       1. Check Balance \n       2. Deposit Money\n       3. Withdraw Money")

n = input("Enter your choice :\n ").title()
#old_balance = 50000
pins = [1234, 5678, 9876, 1111,7412,8523,9632,7896,9874]
balances = [50000,963210,74123,85210,963210,78964,74123658,74102,78963]

if n == "Check Balance":
    user_pin = int(input("Enter your PIN : "))
    
    
    if user_pin in pins :
        print("Login Successful")

        index = pins.index(user_pin)
        amount = balances[index]
        
        print("Your Current balance is :")
        print(amount)
    else:
        print("Invalid pin")

elif n == "Deposit Money":
    user_pin = int(input("Enter your PIN : "))
    
    
    if user_pin in pins :
        print("Login Successful")
       
        amt = int(input("Enter amount :"))

        index = pins.index(user_pin)
        amount = balances[index]

        New_Balance = amount + amt
        print("Your current balance is :")
        print(New_Balance)

    else:
        print("Invalid pin")

elif n == "Withdraw Money":
    user_pin = int(input("Enter your PIN : "))
    #print(pin)
    
    if user_pin in pins :
        print("Login Successful")
        
        withdraw = int(input("Enter amount :"))

        index = pins.index(user_pin)
        amount = balances[index]
        New_Balance = amount - withdraw

        if withdraw > amount :
            print("Insufficient balance.")
        else:
            print("Your current balance is :")
            print(New_Balance)
else:
    print("Thank You")