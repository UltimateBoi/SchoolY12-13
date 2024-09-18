import re

def is_valid_email(email):
    # Check if the email matches the regular expression pattern for validating an email address
    # Regular expression pattern breakdown:
    # ^                     : Start of the string
    # [A-Za-z0-9._%+-]+     : One or more characters that can be uppercase letters, lowercase letters, digits, dots, underscores, percent signs, plus signs, or hyphens
    # @                     : The '@' symbol
    # [A-Za-z0-9.-]+        : One or more characters that can be uppercase letters, lowercase letters, digits, dots, or hyphens
    # \.                    : A literal dot
    # [A-Z|a-z]{2,}         : Two or more {2,} characters that can be uppercase or lowercase letters [A-Z|a-z]
    # $                     : End of the string

    if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$", email):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    email = input("Enter an email address to check its validity: ")
    if is_valid_email(email):
        print("Email is valid.")
    else:
        print("Email is invalid.")