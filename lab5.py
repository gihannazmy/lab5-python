class Animal:
    def _init_(self, name, type, gender):
        self.name = name
        self.type = type
        self.gender = gender

    def make_sound(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is a {self.type}."

class Cat(Animal):
    def _init_(self, name, gender):
        super()._init_(name, type="Cat", gender=gender)

    def meow(self):
        return f"{self.name} says Meow!"

    def eat(self):
        return f"{self.name} eats cat food."

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount can not be negative")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")


    def transfer(self, target_account, amount):
        if isinstance(target_account, Account) and 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            print("Transfer failed due to insufficient funds or invalid amount.")

    def check_balance(self):
        return self.balance

    def generate_statement(self):
        return f"Account {self.account_number} balance: ${self.balance:.2f}"

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_total_balance(self):
        total_balance = sum(account.check_balance() for account in self.accounts)
        return total_balance

    def generate_customer_statement(self):
        statement = f"Customer: {self.name}\n"
        for account in self.accounts:
            statement += account.generate_statement() + "\n"
        statement += f"Total balance: ${self.get_total_balance():.2f}"
        return statement


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)

    def get_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
        return None

    def transfer_money(self, source_account, target_account, amount):
        if isinstance(source_account, Account) and isinstance(target_account, Account):
            source_account.transfer(target_account, amount)
        else:
            print("Transfer failed due to invalid accounts.")



