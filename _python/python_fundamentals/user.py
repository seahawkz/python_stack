class User:
    def __init__(self, name):
        self.name = "Fred"
        self.account_balance = 0
    # deposit
    def make_deposit(self, amount):
        self.account_balance += amount
    # withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    # display user balance
    def display_user_balance(self):
        
    
