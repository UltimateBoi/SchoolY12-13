import numpy as np

# 1D Array Example
# Creating a 1D array with numpy
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Accessing elements in a 1D array
print("First element in 1D array:", array_1d[0])
print("Last element in 1D array:", array_1d[-1])

# 2D Array Example
# Creating a 2D array with numpy
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

# Accessing elements in a 2D array
print("Element at row 1, column 2 in 2D array:", array_2d[0, 1])
print("Element at row 3, column 3 in 2D array:", array_2d[2, 2])

# 3D Array Example
# Creating a 3D array with numpy
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], 
                     [[7, 8, 9], [10, 11, 12]]])
array3d = [[[1, 2, 3], [4, 5, 6]], 
           [[7, 8, 9], [10, 11, 12]]]
print("\n3D Array:")
print(array_3d)

# Accessing elements in a 3D array
print("Element at depth 1, row 2, column 3 in 3D array:", array_3d[0, 1, 2])
print("Element at depth 2, row 1, column 1 in 3D array:", array_3d[1, 0, 0])

print(array3d[0][1][2],end="\n\n")

print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)