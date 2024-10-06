# Subroutine to display the menu and validate the user choice
def displayMenu():
    while True:
        print("\n1. Add name \n2. Display list \n3. Quit")
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice - please re-enter.")
        except ValueError:
            print("Invalid input - please enter a number between 1 and 3.")

# Subroutine to add a name at a specific position
def addName(names):
    if len(names) < 10:
        name = input("Enter the name to be added to the list: ")
        while True:
            try:
                position = int(input("Enter the position in the list to insert the name (1-10): "))
                if 1 <= position <= 10:
                    names[position - 1] = name  # Insert or overwrite the name
                    break
                else:
                    print("Invalid position - please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input - please enter a valid number.")
    else:
        print("The list is full. Unable to add more names.")

# Subroutine to display the list
def displayList(names):
    for i, name in enumerate(names):
        if name:
            print(f"{i + 1} {name}")
        else:
            print(f"{i + 1} [Empty]")

# Main program
def main():
    names = [None] * 10  # Initialize a list of 10 empty slots
    while True:
        choice = displayMenu()  # Call the subroutine to get the user's choice
        
        if choice == 1:
            addName(names)  # Call the subroutine to add a name
        elif choice == 2:
            displayList(names)  # Call the subroutine to display the list
        elif choice == 3:
            print("Program terminating")
            break

# Run the main program
main()