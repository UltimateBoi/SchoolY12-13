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