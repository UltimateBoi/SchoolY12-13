def validate_temperature(temp): #  This function checks if the provided temperature is within the valid range (-50 to 50).
    if not isinstance(temp, (int, float)):  # Check if the input is a number
        return "Invalid input: temperature must be a number"
    
    if -50 <= temp <= 50:  # Check if the temperature is within the valid range
        return "Valid temperature"
    else:
        return "Temperature outside safe operating range"
    
if __name__ == "__main__": # If the script is being run, not imported
    temp = int(input("Enter the temperature in degrees Celsius: "))
    print(validate_temperature(temp)) # Check if the temperature is within the safe operating range