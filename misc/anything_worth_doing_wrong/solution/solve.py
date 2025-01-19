import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the maze image
maze_image_path = '../public/Misc200-3.png'
maze_image = Image.open(maze_image_path)

# Display the maze to understand its structure
#plt.imshow(maze_image)
#plt.axis('off')
#plt.show()

# Convert the image to a grayscale array for processing
maze_array = np.array(maze_image.convert('L'))

# Display the grayscale version of the maze
#plt.imshow(maze_array, cmap='gray')
#plt.axis('off')
#plt.show()

# Analyze the pixel values in the grayscale maze
#np.unique(maze_array)

# Binarize the maze: set threshold (e.g., anything above 128 becomes a path)
threshold = 128
binary_maze = (maze_array < threshold).astype(int)  # Paths are 1, walls are 0

# Display the binarized maze for confirmation
plt.imshow(binary_maze, cmap='gray')
plt.axis('off')
plt.show()

print(binary_maze.shape)

from collections import deque

def solve_maze(maze, start, end):
    """
    Solve the maze using BFS.
    :param maze: 2D binary numpy array (1: path, 0: wall)
    :param start: Tuple (x, y) for the starting position
    :param end: Tuple (x, y) for the ending position
    :return: List of (x, y) positions in the solution path, or empty if no solution
    """

    rows, cols = maze.shape
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct path from end to start
            path = []
            while current:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if neighbor not in visited and maze[neighbor] == 1:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current

    return []  # No solution found


# Define start (green) and end (red) positions
start_position = (6, 6)  # top-left corner (green dot)
end_position = (400, 795)  # Bottom-right corner (red dot)

# Solve the maze
solution_path = solve_maze(binary_maze, start_position, end_position)

# Visualize the solution
if solution_path:
    solved_maze = np.copy(binary_maze)
    for x, y in solution_path:
        solved_maze[x, y] = 0.5  # Mark solution path in gray

    plt.imshow(solved_maze, cmap='gray')
    plt.axis('off')
    plt.title("Solved Maze")
    plt.show()
else:
    print("No solution found for the maze.")