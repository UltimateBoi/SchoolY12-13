bags = int(input("Enter the number of paper bags: "))
sweets = int(input("Enter the number of sweets: "))

while True:
    if sweets <= bags:
        print("Error: The number of sweets must be greater than the number of bags.")
    else:
        if (sweets - bags) % 2 == 0:
            print("Yes, it is possible to put an odd number of sweets in each bag.")
        else:
            print("No, it is not possible to put an odd number of sweets in each bag.")
    
    continue_input = input("Do you want to enter another set of values? (y/n): ").strip().lower()
    if continue_input != 'y':
        break
    
    bags = int(input("Enter the number of paper bags: "))
    sweets = int(input("Enter the number of sweets: "))