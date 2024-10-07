def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))  # Get user input
    result = factorial(number)  # Calculate factorial
    print(f"The factorial of {number} is {result}")  # Print the result