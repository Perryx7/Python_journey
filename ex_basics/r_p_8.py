# Banka acoount simulator
# Ask the user for an initial balance.
#  Allow them to perform 3 simple operations: 
# deposit, withdraw, check balance.


def deposit(balance , amount) :
 #initialise the balance with the cureent balance + the current amount you want to make a deposit
 balance += amount 
 
 print ("you make a deposit off " + str(amount) + " " + "\n you new balance is " + str(balance))

#return the new balance
 return balance


def withdraw(balance , amount) :
 #initialise the balance with the current balance + the  amount you want to make a withdraw
 balance -= amount 
 print ("you make a withdraw off " + str(amount) + " " + "\n you new balance is " + str(balance))

#return the new balance
 return balance

#Actions
balance = int(input ("enter your initial balance "))

while True:
    action = input("  1 for deposit , 2 for withdraw, 3 for check, 4 for exist ").strip().lower()

    # deposit action
    if action == "1" :
     amount = int(input("enter the amount of your deposit   "))
     if amount < 0 :
      print("you must enter a ngative number")
     else:
      balance = deposit(balance, amount)

    #withdraw action
    elif action== "2":
    
        amount = int(input("how many do you want to withdraw "))
        if amount > balance :
         print("insuufficient  funds")
        else:
         balance  = withdraw(balance,amount)
    #check action
    elif action == "3" :
      print("your balance is " + str(balance))
      #exit action
    elif action == "4":
     break


 
 

