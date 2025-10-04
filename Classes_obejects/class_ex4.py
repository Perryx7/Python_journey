"""Bank Account

Create a class BankAccount with attributes: owner and balance.

Add methods:

deposit(amount)

withdraw(amount) (only if balance is enough)

get_balance()

Create two accounts and simulate transactions.

"""

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    """def authentification(self, name):
        if name == self.owner:
            return True
        else :
            return False"""



    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount} from {self.owner} ")
        print(f'new Balance: {self.balance}')



    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdraw {amount} from {self.owner} ")
        print(f'new Balance: {self.balance}')

    def get_balance(self):
        print(self.balance)


Acc1 = BankAccount("Dia", 500)
Acc2 = BankAccount("Ango", 500)



for acc in Acc1, Acc2 :
    acc.deposit(100)
    acc.withdraw(100)




