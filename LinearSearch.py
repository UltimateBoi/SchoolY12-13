def linear_search(arr, target):
    # Iterate over each element in the array
    for index, value in enumerate(arr):
        # Check if the current element is the target
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

def basic_linear_search(arr, target):
    # Iterate over each element in the array using a simple for loop
    for index in range(len(arr)):
        # Check if the current element is the target
        if arr[index] == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Define the array and the target value
array = [22, 34, 56, 78, 90] # Ex array
target = 56

# Perform the linear search
result = linear_search(array, target)

# Print the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

# Perform the basic linear search
basic_result = basic_linear_search(array, target)

# Print the result for the basic linear search
if basic_result != -1:
    print(f"Element {target} found at index {basic_result} using basic_linear_search.")
else:
    print(f"Element {target} not found in the array using basic_linear_search.")

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

# Perform the basic linear search for the word
basic_word_result = basic_linear_search(word_array, word_target)

# Print the result for the basic linear search for the word
if basic_word_result != -1:
    print(f"Element '{word_target}' found at index {basic_word_result} using basic_linear_search.")
else:
    print(f"Element '{word_target}' not found in the array using basic_linear_search.")