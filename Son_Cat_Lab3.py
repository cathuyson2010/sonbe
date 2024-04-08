class BankAccount:
    def __init__(self, name, checking_balance, savings_balance):
        self.name = name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def deposit_checking(self, amount):
        self.checking_balance += amount

    def deposit_savings(self, amount):
        self.savings_balance += amount

    def withdraw_checking(self, amount):
        if amount <= self.checking_balance:
            self.checking_balance -= amount
        else:
            print("Insufficient funds in checking account.")

    def withdraw_savings(self, amount):
        if amount <= self.savings_balance:
            self.savings_balance -= amount
        else:
            print("Insufficient funds in savings account.")

    def transfer_to_savings(self, amount):
        if amount <= self.checking_balance:
            self.checking_balance -= amount
            self.savings_balance += amount
        else:
            print("Insufficient funds to transfer from checking to savings.")

# Demo code
account = BankAccount("Mickey",500.00, 1000.00)
account.checking_balance = 500
account.savings_balance = 500
account.withdraw_savings(100)
account.withdraw_checking(100)
account.transfer_to_savings(300)
print(account.name)
print(f'Checking Balance: ${account.checking_balance:.2f}')
print(f'Savings Balance: ${account.savings_balance:.2f}')
