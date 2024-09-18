def get_valid_cost():
    # Loop until a valid cost is entered
    while True:
        try:
            # Prompt the user to enter a cost and convert it to a float
            cost = float(input("Enter a cost: "))
            return cost  # Return the valid cost
        except ValueError:
            # If the input is not a valid float, print an error message
            print("Invalid input. Please enter a valid number.")

def main():
    # Get a valid cost from the user
    cost = get_valid_cost()
    # Print the cost formatted to 2 decimal places with a pound sign
    print(f"£{cost:.2f}")

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()