def palidrome_checker(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    user_input = input("Enter a word to check if it's a palindrome: ")
    # Convert the string to an array of characters
    char_array = list(user_input)
    if palidrome_checker(char_array):
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")

if __name__ == "__main__":
    main()