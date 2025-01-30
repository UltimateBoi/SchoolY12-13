# Write a function that takes a list and an index as input and returns the element at that index. If the index is out of range, return None.

def getElementFromIndex(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None
    
# Example usage:
list1 = [10, 20, 30, 40, 50]
index = 2
result = getElementFromIndex(list1, index)

print(f"Index {index}: {result}")

# Write a function that takes a list and an element as input and removes the first occurrence of the element from the list.

def removeFirstOccurrence(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

# Example usage:
list2 = [10, 20, 30, 40, 50]
element_to_remove = 30
print(f"Original list: {list2}")
updated_list = removeFirstOccurrence(list2, element_to_remove)
print(f"Updated list after removing {element_to_remove}: {updated_list}")

# Write a function that takes two lists as input and returns a new list containing elements from both lists
def mergeLists(lst1, lst2):
    return lst1 + lst2

# Example usage:
list3 = [1, 2, 3]
list4 = [4, 5, 6]
merged_list = mergeLists(list3, list4)
print(f"Merged list: {merged_list}")

#  Write a function that takes a list as input and returns a new list with the elements sorted in ascending order.

def sortListAscending(lst):
    return sorted(lst)

# Example usage:
list5 = [50, 20, 40, 10, 30]
sorted_list = sortListAscending(list5)
print(f"Sorted list: {sorted_list}")

# Write a function that takes a list as input and returns a new list with the elements sorted in ascending order.

def sortListAscending(lst):
    return sorted(lst)

#  Write a function that takes a list as input and returns a new list with the elements reversed.

def reverseList(lst):
    return lst[::-1] # slicing

# Write a function that takes a list and an element as input and appends the element to the end of the list.

def appendElement(lst, element):
    lst.append(element) # append() method adds an element to the end of the list
    return lst

# Write a function that takes a list, an index, and a new value as input and updates the element at the specified index in the list.

def updateElementAtIndex(lst, index, new_value):
    if 0 <= index < len(lst): # Check if the index is within the range of the list
        lst[index] = new_value # Update the element at the specified index
    return lst

# Write a function that takes a list as input and returns the number of elements in the list.

def countElements(lst):
    return len(lst)

# Write a function that takes a list, an index, and an element as input and inserts the element at the specified index in the list.

def insertElementAtIndex(lst, index, element):
    if 0 <= index < len(lst): # Check if the index is within the range of the list
        lst.insert(index, element) # Insert the element at the specified
    return lst

# Write a function that takes a list and an element as input and returns True if the element is present in the list, otherwise False.

def isElementPresent(lst, element):
    return element in lst

# Write a function that takes a 2D array as input and returns a list containing the average of elements in each column.

def averageOfColumns(array_2d):
    num_columns = len(array_2d[0]) # Get the number of columns in the 2D array
    averages = [] # Initialize an empty list to store the averages
    for i in range(num_columns):
        column_sum = sum(row[i] for row in array_2d) # Calculate the sum of elements in the column
        column_average = column_sum / len(array_2d) # Calculate the average of elements in the column
        averages.append(column_average) # Append the average to the list
    return averages

# Write a function that takes a 2D array as input and returns the sum of all elements in the array.

def sumOfElements(array_2d):
    return sum(sum(row) for row in array_2d) # list comprehension to calculate the sum of all elements in the 2D array

# Write a function that takes two 2D arrays as input and returns their matrix multiplication

def matrixMultiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))] # Initialize the result matrix with zeros using list comprehension
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] # Perform matrix multiplication algorithm

# Write a function that takes a 2D array as input and returns a list containing the average of elements in each row.

def averageOfRows(array_2d):
    averages = [sum(row) / len(row) for row in array_2d] # Calculate the average of elements in each row using list comprehension
    return averages

# Write a function that takes a 2D array as input and returns the maximum element present in the array.

def maxElement(array_2d):
    return max(max(row) for row in array_2d) # Calculate the maximum element present in the 2D array

# Write a function that takes a 2D array as input and returns a list containing the sum of elements in each row.

def sumOfRows(array_2d):
    sums = [sum(row) for row in array_2d] # Calculate the sum of elements in each row using list comprehension
    return sums

# Write a function that takes a 2D array as input and returns the sum of elements on the main diagonal (top-left to bottom-right).

def sumOfMainDiagonal(array_2d):
    return sum(array_2d[i][i] for i in range(len(array_2d))) # Calculate the sum of elements on the

# Write a function that takes a 2D array and an element as input and returns True if the element is present in the array, otherwise False.

def isElementPresentIn2DArray(array_2d, element):
    return any(element in row for row in array_2d) # Check if the element is present in any row of the 2D array

# Write a function that takes a 2D array as input and returns a list containing the sum of elements in each column.

def sumOfColumns(array_2d):
    num_columns = len(array_2d[0]) # Get the number of columns in the 2D array
    sums = [sum(row[i] for row in array_2d) for i in range(num_columns)] # Calculate the sum of elements in each column using list comprehension
    return sums

# Write a function that takes a 2D array as input and returns its transpose (rows become columns and vice versa).

def transposeArray(array_2d):
    return [[array_2d[j][i] for j in range(len(array_2d))] for i in range(len(array_2d[0]))] # Transpose the 2D array using list comprehension