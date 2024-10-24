class BankAccount:
    def __init__(self, account_holder_name, initial_balance=0):
        self.__account_holder_name = account_holder_name  # Initialize account holder name
        self.__balance = initial_balance  # Initialize balance

    def deposit(self, amount):
        if amount > 0:  # Check if deposit amount is positive
            self.__balance += amount  # Add amount to balance
            print(f"Deposited {amount}. New balance is {self.__balance}.")  # Print new balance
        else:
            print("Deposit amount must be positive.")  # Print error message for invalid deposit

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Check if withdrawal amount is valid
            self.__balance -= amount  # Subtract amount from balance
            print(f"Withdrew {amount}. New balance is {self.__balance}.")  # Print new balance
        else:
            print("Invalid withdrawal amount.")  # Print error message for invalid withdrawal

    def display_balance(self):
        print(f"Account holder: {self.__account_holder_name}, Balance: {self.__balance}")  # Display account holder and balance

# Testing the BankAccount class
account1 = BankAccount("Jeff", 1000)  # Create account1 with initial balance
account2 = BankAccount("Bob", 500)  # Create account2 with initial balance

account1.deposit(200)  # Deposit into account1
account1.withdraw(150)  # Withdraw from account1
account1.display_balance()  # Display balance of account1

account2.deposit(300)  # Deposit into account2
account2.withdraw(100)  # Withdraw from account2
account2.display_balance()  # Display balance of account2
