def binary_search(arr, target):
    # Initialize the left and right pointers for the binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Define the array and the target value
array = [3, 8, 15, 23, 42, 50]
target = 23

# Perform the binary search
result = binary_search(array, target)

# Print the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
