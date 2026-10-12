# Lab-7_B-2

# Create a BankAccount class with owner and balance. Add a deposit method that changes the balance.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        
account_holder1 = BankAccount("Buffet", 2500)
print(account_holder1.owner, account_holder1.balance)

account_holder2 = BankAccount("Gates", 1500)
print(account_holder2.owner, account_holder2.balance)

account_holder1.deposit(500)
print(account_holder1.owner, account_holder1.balance)


