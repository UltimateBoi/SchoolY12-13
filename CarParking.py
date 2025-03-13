park = [["empty" for _ in range(6)] for _ in range(10)] # 10 rows, 6 columns using list comprehension

def display_grid():
    for r in range(10): # r is for row index
        print(f"Row {r+1}: {park[r]}") # Pretty print the grid using list comprehension

while True:
    reg = input("Enter car registration (or 'quit' to exit): ")
    if reg.lower() == "quit":
        break
    while True:
        try:
            row = int(input("Enter row (1-10): "))
            col = int(input("Enter column (1-6): "))
            if 1 <= row <= 10 and 1 <= col <= 6:
                if park[row-1][col-1] == "empty":
                    park[row-1][col-1] = reg
                    break
                else:
                    print("That space is taken.")
            else:
                print("Invalid. Try again.")
        except ValueError: # Handle invalid input
            print("Invalid. Try again.")
    display_grid()