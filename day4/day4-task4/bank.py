class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
    def add_customer(self, customer):
        self.customers.append(customer)
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)            
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def check_balance(self):
        print(f"Balance in Account {self.account_number}: {self.balance}")
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to Account {self.account_number}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}")
        else:
            print("Insufficient funds")
    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to Account {target_account.account_number}")
        else:
            print("Insufficient funds")
            
my_bank = Bank(" Bank Masr")
alaa = Customer("Alaa")
mohammed = Customer("mohammed")
my_bank.add_customer(alaa)
my_bank.add_customer(mohammed)
account1 = Account("1", 1000)
account2 = Account("2", 500)
alaa.add_account(account1)
mohammed.add_account(account2)
account1.check_balance()
account2.check_balance()
account1.transfer(account2, 200)
account1.check_balance()
account2.check_balance()
