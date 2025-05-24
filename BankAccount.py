# Define Class
class BankAccount:
    def __init__(self, username, owner, password, balance=0):
        self.username = username
        self.owner = owner
        self.password = password
        self.__balance = balance
        self.transaction_history = [] # List to store transactions

    def check_password(self, input_password):
        return self.password == input_password

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balane: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

    