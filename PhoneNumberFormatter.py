def phone_num_formatter(phone_num):
    if not phone_num.isdigit():  # Check if the input is a number
        return "Invalid input: phone number must be a number"
    
    if len(phone_num) == 10:  # Check if the phone number has 10 digits
        formatted_num = f"({phone_num[:3]}) {phone_num[3:6]}-{phone_num[6:]}" # Format the phone number using parentheses and dashes
        return f"Formatted phone number: {formatted_num}" # Return the formatted phone number
    else:
        return "Invalid phone number: enter a 10-digit number" # Return an error message if the phone number is not 10 digits

if __name__ == "__main__":
    print(phone_num_formatter(input("Enter your phone number (10 digits): "))) # Ask the user to enter their phone number and print the formatted number