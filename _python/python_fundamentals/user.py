class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # deposit
    def make_deposit(self, amount):
        self.account_balance += amount
    # withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    # display user balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    # transfer money
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

fred = User("Fred", "fred@email.com")
jen = User("Jen", "jen@email.com")
john = User("John", "john@email.com")

fred.make_deposit(200)
fred.make_deposit(1450)
fred.make_deposit(500)
fred.make_withdrawal(325)
fred.display_user_balance()

jen.make_deposit(230)
jen.make_deposit(380)
jen.make_withdrawal(110)
jen.make_withdrawal(234)
jen.display_user_balance()

john.make_deposit(1050)
john.make_withdrawal(150)
john.make_withdrawal(230)
john.make_withdrawal(565)
john.display_user_balance()

fred.transfer_money(john, 300)
fred.display_user_balance()
john.display_user_balance()
    
