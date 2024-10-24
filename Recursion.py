def sum_even_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_even_numbers(n - 2)

n = 1000 # Max recursive depth in python is 1000
result = sum_even_numbers(n)
print(f"The sum of all even numbers between 0 and {n} is: {result}")