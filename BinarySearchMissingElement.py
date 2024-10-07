def binary_search(arr, target):
    # Perform a binary search to find the target in a sorted array.
    
    # Check if the array is empty
    if not arr:
        return "The array is empty"  # Return message if array is empty
    
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1  # Set initial pointers
    
    # Loop until the pointers cross
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        
        if arr[mid] == target:
            return f"Number {target} found at index {mid}"  # Target found
        
        elif arr[mid] < target:
            left = mid + 1  # Ignore the left half
        
        else:
            right = mid - 1  # Ignore the right half
    
    return f"Number {target} not found in the array"  # Target not found

# Sorted array to search in
arr = [10, 20, 30, 40, 50]

# Target number to find
target = 35

# Call the binary search function and print the result
print(binary_search(arr, target))
