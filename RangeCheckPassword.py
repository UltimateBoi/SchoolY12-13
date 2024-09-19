import re

def is_strong_password(password):
    # Check if the length is between 8 and 20 characters
    if not (8 <= len(password) <= 20):
        return False
    
    # Check if it contains at least one uppercase letter, one lowercase letter, and one digit
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    
    return True