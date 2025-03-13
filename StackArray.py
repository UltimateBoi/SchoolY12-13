print("The input is " + ("a palindrome." if (w:=list(input("Please enter a word or phrase to be tested: ").lower()))==w[::-1] else "not a palindrome."))
"""
This module checks whether a user-provided word or phrase is a palindrome.

The script performs the following steps:
1. Prompts the user for a word or phrase.
2. Converts the input to lowercase.
3. Uses the walrus operator (:=) to assign the input (as a list of characters) to 'w'.
4. Compares the list with its reverse to determine if the input is a palindrome.

Note: The list() constructor is used to split the input string into a list of characters, which is a concise approach for this use case.
"""