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

    def 