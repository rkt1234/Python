class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount) -> float:
        self.balance += amount
        print(f"Deposited ₹{amount}. Updated balance: ₹{self.balance}")
        return self.balance

    def withdraw(self, amount) -> float:
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Updated balance: ₹{self.balance}")
        return self.balance

    def display(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")
