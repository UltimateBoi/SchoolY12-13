import json
import random

# Load user details from a JSON file
def load_user_details(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Check user ID
def check_user_id(user_id, stored_user_id):
    return user_id == stored_user_id

# Check PIN
def check_pin(pin, stored_pin):
    return pin == stored_pin

# Main login procedure
def login(user_details):
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        user_id = input("Enter your 10-character user ID: ")
        if check_user_id(user_id, user_details['user_id']):
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect ID - access denied. You have {max_attempts - attempts} attempts left.")
            else:
                print("Incorrect ID - access denied")
                return

    pin = input("Enter your 4-digit PIN: ")
    if not check_pin(pin, user_details['pin']):
        print("Incorrect PIN - access denied")
        return

    attempts = 0
    while attempts < max_attempts:
        # Ask periodically for three e.g. first, third, and fifth character of the user's password (each time different characters are requested)
        positions = random.sample(range(1, len(user_details['password']) + 1), 3)
        correct = True
        for pos in positions:
            password_char = input(f"Enter character {pos} of your password: ")
            if password_char != user_details['password'][pos - 1]:
                correct = False
                break
        if correct:
            print("Access granted")
            return
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect password - access denied. You have {max_attempts - attempts} attempts left.")
            else:
                print("Incorrect password - access denied")
                return

if __name__ == "__main__":
    user_details = load_user_details('user_details.json')
    login(user_details)