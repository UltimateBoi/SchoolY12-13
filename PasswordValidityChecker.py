def is_valid_password(password): # Define the function is_valid_password with one parameter, password
    if 8 <= len(password) <= 20: # Check if the length of the password is between 8 and 20 characters
        return True
    else:
        return False