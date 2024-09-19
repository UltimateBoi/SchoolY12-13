import heapq

# Heuristic function to estimate the cost from current node to the goal
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm implementation
def a_star_search(start, goal, grid, weights):
    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
    open_set = []  # Priority queue to store the nodes to be evaluated
    heapq.heappush(open_set, (0, start))  # Push the start node into the priority queue
    came_from = {}  # Dictionary to store the path
    g_score = {start: 0}  # Dictionary to store the cost from start to the current node
    f_score = {start: heuristic(start, goal)}  # Dictionary to store the estimated cost from start to goal

    while open_set:
        _, current = heapq.heappop(open_set)  # Get the node with the lowest f_score

        if current == goal:  # If the goal is reached, reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path in the correct order

        # Explore the neighbors of the current node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            # Check if the neighbor is within the grid and is not an obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                # Calculate the movement cost, considering the weights
                movement_cost = weights.get(neighbor, 1)
                tentative_g_score = g_score[current] + movement_cost  # Calculate the tentative g_score

                # If the neighbor is not in g_score or the tentative g_score is lower
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current  # Update the path
                    g_score[neighbor] = tentative_g_score  # Update the g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)  # Update the f_score
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))  # Push the neighbor into the priority queue

    return None  # Return None if no path is found

# Main function to test the A* search algorithm
def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]  # Define the grid with obstacles
    weights = {
        (2, 3): 5,  # Higher movement cost for cell (2, 3)
        (3, 1): 5   # Higher movement cost for cell (3, 1)
    }
    start = (0, 0)  # Define the start position
    goal = (4, 4)  # Define the goal position
    path = a_star_search(start, goal, grid, weights)  # Perform A* search
    if path:
        print("Path found:", path)  # Print the path if found
    else:
        print("No path found")  # Print a message if no path is found

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly