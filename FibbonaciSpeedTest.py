from datetime import datetime as t

# Recursive approach
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Iterative approach
def fibonacci2(n):
    fibNumbers = [0, 1]  # list of first two Fibonacci numbers
    # now append the sum of the two previous numbers to the list    
    for i in range(2, n + 1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

# Test the functions and benchmark the time taken
n = 50

# Benchmark recursive approach
startTime = t.now()
fib(n)
endTime = t.now()
totalTimeRecursive = endTime - startTime

# Benchmark iterative approach
startTime = t.now()
fibonacci2(n)
endTime = t.now()
totalTimeIterative = endTime - startTime

print(f"Time taken for recursive approach: {totalTimeRecursive.total_seconds():.06f} seconds")
print(f"Time taken for iterative approach: {totalTimeIterative.total_seconds():.06f} seconds")