def get_valid_integer():
    while True:
        try:
            # Prompt the user to enter an integer
            number = int(input("Enter an integer: "))
            return number  # Return the valid integer
        except ValueError:
            # If the input is not a valid integer, print an error message
            print("Invalid input. Please enter a valid integer.")

def main():
    # Get a valid integer from the user
    number = get_valid_integer()
    # Print the valid integer
    print(f"You entered the integer: {number}")

if __name__ == "__main__":
    main()