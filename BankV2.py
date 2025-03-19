"""
Create a Python class for a Bank. Implement a constructor that initializes an 
empty list to store bank accounts. Create methods to add a new account to the 
bank, find an account by account number, deposit money into an account, withdraw 
money from an account, and display all accounts' information. Instantiate more 
than one object from the class, and show suitable testing.  
"""

class Bank:
    # private
    __accounts = None

    # constructor
    def __init__(self):
        elf.__accounts = []
s
    def add_account(self, account, account_holder, balance):
        new_account = Account(account, account_holder, balance) # instance of Account class that is created and stored in the list of accounts
        self.__accounts.append(new_account) # append the new account to the list of accounts
        return new_account # return the new account
    
    # find account by account number from the list of accounts accessing the Account class
    def find_account(self, account_number):
        for account in self.__accounts: # iterate through the list of accounts
            if account.get_account_number() == account_number: # if the account number matches the account number in the list of accounts, return that account
                return account
        return None

    def deposit(self, account_number, amount): # deposit money into an account by account number with the account number and amount as parameters
        account = self.find_account(account_number) # find the account by account number
        if account != None: # if the account is found
            account.deposit(amount) # deposit the amount into the account that is found through the account number
            return True
        return False # if the account is not found, return False

    def withdraw(self, account_number, amount): # withdraw money from an account by account number with the account number and amount as parameters
        account = self.find_account(account_number) # find the account by account number
        if account != None: # if the account is found
            if account.withdraw(amount): # withdraw the amount from the account that is found through the account number
                return True
        return False
    
    def display_accounts(self):
        for account in self.__accounts: # iterate through the list of accounts and for each account, print the account number, account holder, and balance
            print(f"Account Number: {account.get_account_number()}")
            print(f"Account Holder: {account.get_account_holder()}")
            print(f"Balance: {account.get_balance()}")
            print() # new line
    
class Account:
    def __init__(self, account_number, account_holder, balance): # constructor with account number, account holder, and balance as parameters
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_number(self): # get account number and return the account number
        return self.__account_number

    def get_account_holder(self): # get account holder and return the account holder
        return self.__account_holder

    def get_balance(self): # get balance and return the balance
        return self.__balance

    def deposit(self, amount): # deposit money into the account with the amount as a parameter
        self.__balance += amount

    def withdraw(self, amount): # withdraw money from the account with the amount as a parameter
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def __init__(self, account_number, account_holder, balance): # constructor with account number, account holder, and balance as parameters
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

# test all mehtods within the Bank class

bank = Bank() # instance of Bank class

account1 = bank.add_account(1, "John Doe", 1000) # create two test accounts
account2 = bank.add_account(2, "Jane Doe", 2000)

bank.display_accounts()

print("Adding 500 to account 1 (John Doe) and withdrawing 2 from account 1002 (Jane Doe)\n")

bank.deposit(1, 500)
bank.withdraw(2, 1000)

bank.display_accounts()

print(f"Finding account 1: {bank.find_account(1).get_account_holder()}")
print(f"Finding account 2: {bank.find_account(2).get_account_holder()}")