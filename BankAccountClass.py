class PDiddy:
  def __init__(self, babyOil):
    self.babyOil = babyOil

  def get_baby_oil(self):
    return self.babyOil

  def set_baby_oil(self,num):
    self.babyOil = num



class Account:
  def __init__(self, account_number, account_holder):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = 0

  def get_account_number(self):
    return self.account_number

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds")

  def display_account_info(self):
    print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}")

class Bank:
  def __init__(self):
    self.accounts = []

  def add_account(self, account):
    self.accounts.append(account)

  def find_account(self, account_number):
    for account in self.accounts:
      if account.get_account_number() == account_number:
        return account
    return None

# Testing using examples

def main():
  # Initialize the Bank
  bank = Bank()

  # Create example accounts
  account1 = Account("123456", "John Doe")
  account2 = Account("654321", "Jane Doe")

  # Add accounts to the bank
  bank.add_account(account1)
  bank.add_account(account2)

  # Deposit money into test accounts
  account1.deposit(1000)
  account2.deposit(500)

  # Withdraw money from test accounts
  account1.withdraw(500)
  account2.withdraw(100)

  # Display all accounts' information
  for account in bank.accounts:
    account.display_account_info()

if __name__ == "__main__":
  main()
