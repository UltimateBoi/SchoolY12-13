names = [
    ["Altaf", 5],
    ["Mariam", 5],
    ["Eesa", 3],
    ["Hussain", 6],
    ["Sam", None],
    ["David", 2],
    ["Kaya", 1],
    ["Rezwan", 4]
]

# Create a linked list (not using classes)

head = 0
current = None

# Traverse linked list in physical order
def traverse_physical(arr):
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i][0], end=", ")
        else:
            print(arr[i][0], end="")
    print()

traverse_physical(names)

# Traverse linked list in logical order
def traverse_logical(arr):
    # Traverse based on the pointer of the second element in the sublist
    index = head
    while index is not None:
        current = arr[index]
        if current[1] is None:
            print(current[0], end="")
            break
        else:
            print(current[0], end=", ")
        index = current[1] # TODO: Fix this, prints infinite loop
    print()
    
traverse_logical(names)