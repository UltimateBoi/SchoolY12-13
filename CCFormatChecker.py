import re

def is_valid_credit_card(cardNumber): # function takes a card number as a parameter
    if re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$", cardNumber): # RegEx statement for card number in format "XXXX-XXXX-XXXX-XXXX" where X is a digit
        print("Credit card: " + cardNumber + " is valid") # if so, print valid
    else:
        print("Credit card: " + cardNumber + " is invalid") # else card must be invalid

def __main__():
    cardNumber = input("Enter a credit card number: ")
    is_valid_credit_card(cardNumber)

if __name__ == "__main__": # automatically run __main__ function
    __main__()