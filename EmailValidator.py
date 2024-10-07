def validate_email(email):
    if not email: # Check if the email address is empty
        return "Email address cannot be empty."
    if "@" not in email or "." not in email.split("@")[-1]: # Check if the email address contains '@' and a domain
        return "Invalid email format. Please include '@' and a domain." 
    return "Email address is valid."

def main():
    email = input("Please enter your email address: ")
    validation_message = validate_email(email) # Validate the entered email address
    print(validation_message) # Print the validation result

if __name__ == "__main__":
    main()