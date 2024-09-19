def is_valid_phone_number(phoneNumString):
    return phoneNumString.isdigit() and len(phoneNumString) == 10 # Check if the phone number is all digits (.isdigit() returns true bool if all values in the string are digits) and has a length of 10