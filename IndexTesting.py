# Example string and array
example_string = "Hello, World!"
example_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Accessing the first element
first_char = example_string[0]  # 'H'
first_element = example_array[0]  # 1

# Accessing the last element
last_char = example_string[-1]  # '!'
last_element = example_array[-1]  # 10

# Slicing from the second element to the end
substring_from_second = example_string[1:]  # 'ello, World!'
subarray_from_second = example_array[1:]  # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing up to the fifth element (exclusive)
substring_to_fifth = example_string[:5]  # 'Hello'
subarray_to_fifth = example_array[:5]  # [1, 2, 3, 4, 5]

# Slicing with a step of 2
substring_step_two = example_string[::2]  # 'Hlo ol!'
subarray_step_two = example_array[::2]  # [1, 3, 5, 7, 9]

# Slicing with a negative step (reversing the string/array)
reversed_string = example_string[::-1]  # '!dlroW ,olleH'
reversed_array = example_array[::-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Slicing a specific range with a step
substring_range_step = example_string[1:10:2]  # 'el,W'
subarray_range_step = example_array[1:10:2]  # [2, 4, 6, 8, 10]

# Printing results
print(f"First character: {first_char}")
print(f"First element: {first_element}")
print(f"Last character: {last_char}")
print(f"Last element: {last_element}")
print(f"Substring from second: {substring_from_second}")
print(f"Subarray from second: {subarray_from_second}")
print(f"Substring to fifth: {substring_to_fifth}")
print(f"Subarray to fifth: {subarray_to_fifth}")
print(f"Substring with step two: {substring_step_two}")
print(f"Subarray with step two: {subarray_step_two}")
print(f"Reversed string: {reversed_string}")
print(f"Reversed array: {reversed_array}")
print(f"Substring range with step: {substring_range_step}")
print(f"Subarray range with step: {subarray_range_step}")