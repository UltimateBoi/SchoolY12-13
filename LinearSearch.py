def linear_search(arr, target):
    # Iterate over each element in the array
    for index, value in enumerate(arr):
        # Check if the current element is the target
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Define the array and the target value
array = [5, 12, 18, 7, 3, 10] # Ex array
target = 18

# Perform the linear search
result = linear_search(array, target)

# Print the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

    # Define the array and the target value for the word search
    word_array = ['apple', 'banana', 'cherry', 'date']
    word_target = 'cherry'

    # Perform the linear search for the word
    word_result = linear_search(word_array, word_target)

    # Print the result for the word search
    if word_result != -1:
        print(f"Element '{word_target}' found at index {word_result}.")
    else:
        print(f"Element '{word_target}' not found in the array.")