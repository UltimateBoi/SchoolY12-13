def get_user_input():
    return int(input("Enter a number: "))  # Get user input and convert to integer

def is_prime(number):
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for divisor in range(2, int(number**0.5) + 1):  # Check divisors up to the square root of the number
        if number % divisor == 0:  # If divisible, it's not a prime number
            return False
    return True  # If no divisors found, it's a prime number

def prime_check():
    num = get_user_input()  # Get the number from the user
    if is_prime(num):  # Check if the number is prime
        print(num, "is a prime number")  # Print if the number is prime
    else:
        print(num, "is not a prime number")  # Print if the number is not prime

# Run the prime check function
prime_check()  # Execute the prime check
