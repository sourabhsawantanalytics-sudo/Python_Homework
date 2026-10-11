class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name =holder_name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print("Deposited", amount)


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw", amount)
        else:
            print("Low Balance")


    def check_balance(self):
        print("Current Balance", self.balance)

BA = BankAccount(25347080, "Ajay Sharma", 10000)
print("Initial Balance:", BA.balance)
BA.deposite(14350)
BA.withdraw(3300)
BA.check_balance()        