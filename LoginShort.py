import json, random
def load_user_details(file_path): return json.load(open(file_path, 'r'))
def check_user_id(user_id, stored_user_id): return user_id == stored_user_id
def check_pin(pin, stored_pin): return pin == stored_pin
def login(user_details):
    attempts, max_attempts = 0, 3
    while attempts < max_attempts:
        if check_user_id(input("Enter your 10-character user ID: "), user_details['user_id']): break
        else: attempts += 1; print(f"Incorrect ID - access denied. You have {max_attempts - attempts} attempts left.") if attempts < max_attempts else print("Incorrect ID - access denied"); return
    if not check_pin(input("Enter your 4-digit PIN: "), user_details['pin']): print("Incorrect PIN - access denied"); return
    attempts = 0
    while attempts < max_attempts:
        positions = random.sample(range(1, len(user_details['password']) + 1), 3)
        if all(input(f"Enter character {pos} of your password: ") == user_details['password'][pos - 1] for pos in positions): print("Access granted"); return
        else: attempts += 1; print(f"Incorrect password - access denied. You have {max_attempts - attempts} attempts left.") if attempts < max_attempts else print("Incorrect password - access denied"); return

if __name__ == "__main__": login(load_user_details('user_details.json'))