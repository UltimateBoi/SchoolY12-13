def can_vote(age): # Define the function can_vote with one parameter, age
    return 18 <= age <= 120 # Return True if the age is between 18 and 120, and False otherwise

if __name__ == "__main__": # If the script is being run, not imported
    age = int(input("Enter your age: "))
    if can_vote(age): # Check if the person is eligible to vote
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")