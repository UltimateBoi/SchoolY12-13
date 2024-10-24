import re

def is_valid_credit_card(cardNumber): # function takes a card number as a parameter
    if re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$", cardNumber): # RegEx statement for card number in format "XXXX-XXXX-XXXX-XXXX" where X is a digit
        return True # return True if valid
    else:
        return False # return False if invalid

def __main__():
    cardNumber = input("Enter a credit card number: ")
    if is_valid_credit_card(cardNumber):
        print("Credit card: " + cardNumber + " is valid")
    else:
        print("Credit card: " + cardNumber + " is invalid")

if __name__ == "__main__": # automatically run __main__ function
    __main__()