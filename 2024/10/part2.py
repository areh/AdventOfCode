def find_paths(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    unique_paths = []

    def dfs(x, y, path):
        # Add the current position to the path
        path.append((x, y))

        # If we reach a 9, save the path and return
        if grid[x][y] == 9:
            unique_paths.append(path[:])  # Store a copy of the path
            path.pop()  # Backtrack
            return

        # Mark the current cell as visited by storing None (temporarily)
        temp = grid[x][y]
        grid[x][y] = None

        # Explore all valid neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] is not None and grid[nx][ny] == temp + 1:
                dfs(nx, ny, path)

        # Backtrack: Restore the current cell
        grid[x][y] = temp
        path.pop()

    # Find all starting points (cells with 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dfs(i, j, [])

    return unique_paths


with open("input.txt", "r") as inputfile:
    grid = [[int(x) for x in line.strip()] for line in inputfile]

# Find all unique paths
paths = find_paths(grid)

print(f"Number of unique trailhead to summit combinations: {len(paths)}")
