# Define Class
class BankAccount:
    def __init__(self, username, owner, password, balance=0):
        # Initialized account with username, owner name, password, and optional starting balance
        self.username = username
        self.owner = owner
        self.password = password
        self.__balance = balance # Private attribute for balance
        self.transaction_history = [] # List to store history of transactions (not used yet)

    def check_password(self, input_password):
        # Check if the entered password matches the account password
        return self.password == input_password

    def deposit(self, amount):
        # Deposit money into account
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money from account
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        # Return current balance (for internal use)
        return self.__balance

    def display(self):
        # Display account details
        print(f"\nAccount owner: {self.owner}")
        print(f"Username: {self.__username}") 
        print(f"Current balance: ${self.__balance}\n")
        print(f"Transaction history: {self.transaction_history}") # Will populate in future update

# Dictionary to store all registered bank accounts
accounts = {}

# Function to handle user registraction
def register():
    username = input("Choose a username: ")
    if username in accounts:
        print("❌ Username already exists.")
        return
    name = input("Enter your full name: ")
    password = input("Choose a password: ")
    try:
        starting_balance = float(input("Enter starting balance: "))
    except ValueError:
        print("❌ Invalid balance amount.")
        return
    accounts[username] = BankAccount(username, name, password, starting_balance)
    print(f"✅ Account created for {name}!")

# Function to handle user login
def login():
    username = input("Enter username: ")
    if username in accounts:
        password = input("Enter password: ")
        account = accounts[username]
        if account.check_password(password):
            print(f"✅ Welcome back, {account.owner}!")
            return account
        else:
            print("❌ Incorrect password.")
    else:
        print("❌ Account not found.")
    return None

# Menu fot logged-in users to manage their accounts
def user_menu(account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "3":
            account.display()
        elif choice == "4":
            print("🔓 Logging out...")
            break
        else:
            print("❌ Invalid option.")
# Menu for logged-in users to manage their accounts
def main():
    while True:
        print("\n=== Welcome to SimpleBank ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_account = login()
            if user_account:
                user_menu(user_account)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

# Run the program
main()
