import re  # Import the regular expression module

def is_valid_url(string):
    # Check if the string matches the pattern for a valid URL starting with https://www. or http://www.
    if re.match(r"^https://www.[A-Za-z0-9]+.com$", string) or re.match(r"^http://www.[A-Za-z0-9]+.com$", string):
        print("Domain: " + string, "is valid.")  # Print that the domain is valid
    else:
        print("Domain: " + string, "is not valid.")  # Print that the domain is not valid

# Prompt user to enter a URL and check its validity
is_valid_url(input("Enter a url to check its validity: "))