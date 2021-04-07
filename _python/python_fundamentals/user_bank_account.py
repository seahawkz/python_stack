class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # deposit
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    # withdrawal
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    # display user balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
    # transfer money
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
	
    def deposit(self, amount):
        self.balance += amount
        return self
	
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee")
        return self
	
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
	
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

fred = User("Fred", "fred@email.com")
jen = User("Jen", "jen@email.com")
john = User("John", "john@email.com")

fred.make_deposit(400).make_withdrawal(300).display_user_balance()
