class BankAccount:

    def __init__(self, int_rate=.02, balance=0):
        self.int_rate=int_rate
        self.balance= balance

    def deposit(self, amount):
        self.balance= self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance+amount<amount:
            self.balance-=5
            print("Insufficent funds")
        else:
            self.balance-= amount
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance =self.balance+(self.balance*self.int_rate)
            return self

robert= BankAccount()
robert.deposit(500).deposit(500).deposit(1000).withdraw(700).yield_interest().display_account_info()

william = BankAccount()
william.deposit(5000).deposit(2000).withdraw(200).withdraw(400).withdraw(150).withdraw(200).yield_interest().display_account_info()