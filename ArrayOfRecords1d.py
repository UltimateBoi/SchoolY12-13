from collections import namedtuple # Import namedtuple from collections module which allows us to create named tuples in Python

def main():
    # Define named tuple for user records
    User = namedtuple("User", ["FirstName", "LastName", "UserName", "Password"])
    
    # Create array of 5 user records
    users = [
        User("Jeff", "Bezos", "JeffB", "1pass"),
        User("Bob", "Smith", "BobS", "2pass"),
        User("David", "Scott", "DavidS", "3pass"),
        User("Dave", "Williams", "DaveW", "4pass"),
        User("William", "Smith", "WilliamS", "5pass")
    ]
    
    # Prompt for credentials
    print("Login")
    entered_username = input("Username: ")
    entered_password = input("Password: ")
    
    # Check validity of credentials
    access_granted = False
    for user in users:
        if user.UserName == entered_username and user.Password == entered_password: # Check if username and password match
            access_granted = True
            break
    
    if not access_granted:
        print("Access denied.")
        return
    else:
        print("Access granted. Welcome!")
        # Continue with rest of program here

if __name__ == "__main__": # Run the main function if the script is executed directly
    main()