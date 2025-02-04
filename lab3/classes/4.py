class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew", amount, "Balance:", self.balance)
        else:
            print("Insufficient funds")



acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)