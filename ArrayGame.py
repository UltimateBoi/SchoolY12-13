# A grid game draws a 6 by 4 grid with each square denoted by “x”. A character “O” can move by entering a row coordinate from 1 to 6 and column co-ordinate from 1 to 4. The character starts at array poistion [0,0] (Figure 1) and will move, for example, to row 0 column 1 (Figure 2) if the user enters 1, 2 for the row and column coordinates. Remember that the indices of the array both start at 0. 

# Create a 8x6 grid with each square denoted by “x” and the character “O” at position [0,0].

grid = [["x" for i in range(8)] for j in range(6)]

grid[0][0] = "O"

# Pretty print grid function
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

print_grid(grid)

print("")

# Ask the user to enter the row and column coordinates for the character to move to. Update the grid to show the character at the new position and print the updated grid.
row, column = int(input("Enter the row coordinate: ")), int(input("Enter the column coordinate: "))
grid[0][0] = "x"
grid[row-1][column-1] = "O"

print_grid(grid)