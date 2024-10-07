def validate_age(age): #  This function checks if the provided age is within the valid range (10 to 18). And is a number.
    if not isinstance(age, (int, float)):  # Check if the input is a number
        return "Invalid input: age must be a number"
    
    if 10 <= age <= 18:  # Check if the age is within the valid range
        return "Valid pupil age"
    else:
        return "Invalid input: enter a value from 11 to 18"

if __name__ == "__main__": # If the script is being run, not imported
    print(validate_age(int(input("Enter the pupil's age: ")))) # Check if the age is within the valid range