import re

string = "AAA1234ZZZ"

try:
    found = re.search("AAA(.+?)ZZZ", string).group(1)
    print(f"Found: {found} at position {string.index(found)}")
except AttributeError:
    print("No match found.")
    
