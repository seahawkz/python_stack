class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # deposit
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    # withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    # display user balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    # transfer money
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

fred = User("Fred", "fred@email.com")
jen = User("Jen", "jen@email.com")
john = User("John", "john@email.com")

fred.make_deposit(200).make_deposit(1450).make_deposit(500).make_withdrawal(325).display_user_balance()

jen.make_deposit(230).make_deposit(380).make_withdrawal(110).make_withdrawal(234).display_user_balance()

john.make_deposit(1050).make_withdrawal(150).make_withdrawal(230).make_withdrawal(565).display_user_balance()

fred.transfer_money(john, 300).display_user_balance()
john.display_user_balance()
    
