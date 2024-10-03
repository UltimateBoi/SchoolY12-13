def binary_search(arr, target):
    # Initialize the left and right pointers for the binary search
    left, right = 0, len(arr) - 1
    
    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is greater than the middle element, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is less than the middle element, ignore the right half
        else:
            right = mid - 1
    
    # If the target is not found, return -1
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
