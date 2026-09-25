# Lab-9_F-5

# Create and print both an Account and a SavingsAccount object

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


account = Account("bo", 200)

savings_account = SavingsAccount("gun", 200, 5)

print(account)

print(savings_account)
