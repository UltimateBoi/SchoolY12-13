import json
import os

def is_username_available(username, existing_usernames):
    # Check if the username is already in the list
    if username in existing_usernames:
        return False
    
    # Check if the username length is greater than 0
    if len(username) == 0:
        return False
    
    # If the username is available, add it to the list
    existing_usernames.append(username)
    return True

def load_usernames(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_usernames(filename, usernames):
    with open(filename, 'w') as file:
        json.dump(usernames, file)

def main():
    filename = 'usernames.json'
    existing_usernames = load_usernames(filename)
    
    while True:
        username = input("Enter a username to check (or type 'exit' to quit): ")
        if username.lower() == 'exit':
            break
            
        if is_username_available(username, existing_usernames):
            print(f"Username '{username}' is available and has been added.")
        else:
            print(f"Username '{username}' is not available.")
    
    save_usernames(filename, existing_usernames)
    print("Final list of usernames:", existing_usernames)
    print("List has been saved to:", filename)

if __name__ == "__main__":
    main()