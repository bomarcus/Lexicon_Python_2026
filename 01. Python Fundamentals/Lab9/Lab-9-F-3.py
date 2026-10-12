# Lab-9_F-3

# Create SavingsAccount(Account) with an additional interest_rate attribute. Use super() in __init__.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} - {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance,  interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
