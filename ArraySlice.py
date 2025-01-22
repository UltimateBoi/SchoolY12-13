numbers = [1,2,3,4,5,6]
numbers = numbers[::-1]
for i in range(len(numbers)):
    print(numbers[i],end="")
total = sum(numbers)
average = total / len(numbers)
print(f"\nTotal: {total}")
print(f"Average: {average:.2f}")

def search_name(names, target_name):
    for index in range(len(names)):
        if names[index] == target_name:
            return index + 1
    return -1  

print("\n")
# Example usage
names = ["Alice", "Bob", "Charlie", "David"]
target_name = input("Enter the name to search for: ")
record_number = search_name(names, target_name)
if record_number != -1:
    print(f"Record number for {target_name} is {record_number}.")
else:
    print(f"{target_name} was not found.")

def quarterSales(o1, o2, o3):
    total_sales = [0, 0, 0, 0]
    for i in range(4):
        total_sales[i] = o1[i] + o2[i] + o3[i]
    return total_sales

Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [5, 8, 3, 6]
Outlet3Sales = [10, 12, 15, 10]

totals = quarterSales(Outlet1Sales, Outlet2Sales, Outlet3Sales)

for i in range(4):
    print(f"Total for quarter {i+1} {totals[i]}")

# Write a program to read 6 numbers into an array numbers[0] to numbers[5], ouput them in reverse order and then output the total and average.

def reverseArr(arr):
    return arr[::-1] # Reversing the array using slicing