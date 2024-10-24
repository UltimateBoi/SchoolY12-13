import re  # Import the regular expression module

def is_valid_url(string):
    """
    Regex pattern explanation:
    
    Check if the string matches the pattern for a valid URL starting with https://www. or http://www.
    The pattern ensures:
    - The URL starts with http://www. or https://www.
    - Followed by one or more alphanumeric characters (domain name)
    - Followed by a dot (.)
    - Followed by one or more alphabetic characters (top-level domain)
    - Ends with the top-level domain
    """
    pattern = r"^(https://www\.|http://www\.)[A-Za-z0-9]+\.[A-Za-z]+$"
    if re.match(pattern, string):
        return True  # Return True if the URL is valid
    else:
        return False  # Return False if the URL is not valid

# Prompt user to enter a URL and check its validity
url = input("Enter a URL to check its validity: ")
if is_valid_url(url):
    print("Domain: " + url + " is valid.")
else:
    print("Domain: " + url + " is not valid.")