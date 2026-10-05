# Lab-9_F-4

# Override __str__ in SavingsAccount so its output also includes the interest rate.


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

    def __str__(self):
        return f"{self.owner} - {self.balance} - {self.interest_rate}"
