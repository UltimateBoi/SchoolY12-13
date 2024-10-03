def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    
    # Loop until the pointers cross
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return f"Number {target} found at index {mid}"
        
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # Return a message if the target is not found
    return f"Number {target} not found in the array"

# Sorted array to search in
arr = [10, 20, 30, 40, 50]

# Target number to find
target = 35

# Call the binary search function and print the result
print(binary_search(arr, target))