class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.03):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied to account {self.account_number}. New balance is {self.balance}.")


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
        else:
            print("Amount exceeds overdraft limit.")


savings = SavingsAccount("adf2332", "talha", 1000)
checking = CheckingAccount("CAsss456", "hamza", 500)

savings.deposit(200)
savings.apply_interest()
savings.withdraw(100)

checking.deposit(300)
checking.withdraw(700)  
print("Savings Account Balance:", savings.get_balance())
print("Checking Account Balance:", checking.get_balance())
