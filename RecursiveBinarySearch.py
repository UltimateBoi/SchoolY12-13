# Write a recursive function to implement binary search. Search for the number 7 in the array [1, 3, 5, 7, 9, 11, 13].

def binary_search(arr, target, low, high):
    # Base case: if low index exceeds high index, target is not found
    if low > high:
        return -1
    
    mid = (low + high) // 2  # Calculate the middle index using floor division (rounds down)

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If target is smaller than mid, search in the left half
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # If target is larger than mid, search in the right half
    else:
        return binary_search(arr, target, mid + 1, high)
    
# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(f"Target: {target}\nFound at index: {binary_search(arr, target, 0, len(arr) - 1)} of {arr}")  # Output: 3