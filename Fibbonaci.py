# Generates Fibonacci numbers up to a specified limit.

def generate_fibonacci(limit):
    """
    Generates Fibonacci numbers up to the limit.
    
    Args:
    limit (int): The upper bound for the Fibonacci numbers.
    
    Returns:
    list: A list of Fibonacci numbers up to the limit.
    """
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def main():
    """
    Main function to execute the Fibonacci number generation.
    """
    limit = int(input("Enter the limit for Fibonacci numbers: "))
    fibonacci_numbers = generate_fibonacci(limit)
    print("Fibonacci numbers up to", limit, "are:", fibonacci_numbers)

if __name__ == "__main__":
    main()
