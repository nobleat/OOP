class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance+= amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name}, {self.account_balance}")
    def transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kitty = User("Kitty Prissyboots", "KitPriss@fluff.com")
cullen = User("Cullen Benjamin", "CBDB@howhigh.org")
sara = User("Sara Simon", "sasimon@hotmail.com")

kitty.make_deposit(400).make_deposit(600).make_deposit(190).make_withdrawl(160)
kitty.display_user_balance()
print(kitty.account_balance)

cullen.make_deposit(500).make_deposit(400).make_withdrawl(200).make_withdrawl(100)
cullen.display_user_balance
print(cullen.account_balance)

sara.make_deposit(1500).make_withdrawl(300).make_withdrawl(100).make_withdrawl(100)
sara.display_user_balance
print(sara.account_balance)
kitty.transfer(sara, 450)
