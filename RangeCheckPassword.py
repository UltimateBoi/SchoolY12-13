import re

def is_strong_password(password):
    # Check if the length is between 8 and 20 characters
    if not (8 <= len(password) <= 20):
        print("Password must be between 8 and 20 characters long.")
        return False
    
    # Check if it contains at least one uppercase letter, one lowercase letter, and one digit
    if not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search(r'\d', password):
        print("Password must contain at least one digit.")
        return False
    
    return True

while True:
    password = input("Enter a password: ")
    if is_strong_password(password):
        print("Password is strong.")
        break
    else:
        print("Password is not strong enough. Please try again.")