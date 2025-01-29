import random

# A teacher uses a program that stores pupil names in an array. The array is indexed from 0, 
# so the first element in the array is name[0]. Occasionally the teacher needs to search for a name to find the student’s record number, which is index + 1. 

#Write an algorithm that will search an array name containing max elements, to find a name and output record number 
# if it exists. If the name does not exist the user should be told the term was not found.  Use appropriate prompts for input and output in your solution.

def search_name(name, array):
    for i in range(len(array)):
        if array[i] == name:
            return i + 1
    return "Name not found"

# Sales quantities of a certain item, calculated to the nearest thousand, for Jan-March, April-June, July-Sep and Oct-Dec are held in separate arrays for each of 3 outlets. The sales figures for each quarter are to be totalled and output in the format

        #Total for quarter 1 xxxx
        #Total for quarter 2 xxxx
        #Total for quarter 3 xxxx
        #Total for quarter 4 xxxx

        #Write a pseudocode algorithm for this program. Initialise the array with the following test data:
        #Outlet1Sales = [10, 12,15,10]
        #Outlet2Sales = [5,8,3,6]
        #Outlet3Sales = [10,12,15,10]

Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [5, 8, 3, 6]
Outlet3Sales = [10, 12, 15, 10]

total_sales = [0, 0, 0, 0]

for i in range(4):
    total_sales[i] = Outlet1Sales[i] + Outlet2Sales[i] + Outlet3Sales[i]
    print(f"Total for quarter {i + 1} {total_sales[i]}")

print("")

# Initialize the 2D array for 50 outlets and 4 quarters
outletSales = [[0 for _ in range(50)] for _ in range(4)] # Use of _ to indicate that the variable is not used when creating the array using list comprehension

# Populate the array with random sales data
for quarter in range(4):
    for outlet in range(50):
        outletSales[quarter][outlet] = random.randint(1, 20)

# Initialize total sales array
total_sales = [0, 0, 0, 0]

# Calculate total sales for each quarter
for quarter in range(4):
    for outlet in range(50):
        total_sales[quarter] += outletSales[quarter][outlet]
    print(f"Total for quarter {quarter + 1} {total_sales[quarter]}")