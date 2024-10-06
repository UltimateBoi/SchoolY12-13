while True:
    bags, sweets = int(input("Enter the number of paper bags: ")), int(input("Enter the number of sweets: "))
    if sweets <= bags: print("Error: The number of sweets must be greater than the number of bags.")
    else: print("Yes, it is possible to put an odd number of sweets in each bag." if (sweets - bags) % 2 == 0 else "No, it is not possible to put an odd number of sweets in each bag.")
    if input("Do you want to enter another set of values? (y/n): ").strip().lower()[0] != 'y': break