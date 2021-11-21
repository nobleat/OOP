from bankaccount import BankAccount



class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(.02,0)
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"{self.name}, {self.account}")
    # def transfer(self, other_user, amount):
    #     self.account-=amount
    #     other_user.account += amount



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kitty = User("Kitty Prissyboots", "KitPriss@fluff.com")
cullen = User("Cullen Benjamin", "CBDB@howhigh.org")
sara = User("Sara Simon", "sasimon@hotmail.com")

kitty.deposit(400).deposit(600).deposit(190).make_withdraw(160)
kitty.display_user_balance()
print(kitty.account)

cullen.deposit(500).deposit(400).make_withdraw(200).make_withdraw(100)
cullen.display_user_balance
print(cullen.account)

sara.deposit(1500).make_withdraw(300).make_withdraw(100).make_withdraw(100)
sara.display_user_balance
print(sara.account)
# kitty.transfer(sara, 450)
