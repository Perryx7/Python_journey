class Bank:
    def __init__(self,initial_amount, accname):
        self.balance = initial_amount
        self.Name = accname

        print(f"\nAccount : {self.Name} created.\n balance : {self.balance:.2f}")

    def getBalance(self):
        print(f"Account `{self.Name}` your balance is `{self.balance:.2f}`")

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            else :
                self.balance= self.balance + amount
        except ValueError as e:
            print(f"Error: {e}")

        else:
            print(f"you have deposited `{amount}` your new balance is :{self.balance: .2f}")

        finally:
            print("deposit_complete")


