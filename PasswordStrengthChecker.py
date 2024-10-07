import re

def check_password_strength(password):
    # Define the criteria for a strong password
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[@$!%*?&#]', password)

    # Check the password against the criteria
    if len(password) < min_length:
        return "Password is too short. It should be at least 8 characters long."
    if not has_upper:
        return "Password should include at least one uppercase letter."
    if not has_lower:
        return "Password should include at least one lowercase letter."
    if not has_digit:
        return "Password should include at least one number."
    if not has_special:
        return "Password should include at least one special character (@$!%*?&#)."

    return "Password is strong."

def main():
    password = input("Create a password: ")
    feedback = check_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()