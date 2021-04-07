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

ba1 = BankAccount(balance=300)
ba2 = BankAccount(.03, 600)

ba1.deposit(200).deposit(350).deposit(425).withdraw(205).yield_interest().display_account_info()
ba2.deposit(300).deposit(150).withdraw(250).withdraw(75).withdraw(200).withdraw(150).yield_interest().display_account_info()
