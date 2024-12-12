def calculate_total(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(r, c, letter):
        return 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] == letter

    def dfs(r, c, letter):
        stack = [(r, c)]
        visited[r][c] = True
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            area += 1
            # Check neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, letter):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != letter:
                    # Increment perimeter if edge touches an invalid cell
                    perimeter += 1

        return area, perimeter

    total = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Found a new region
                letter = grid[r][c]
                area, perimeter = dfs(r, c, letter)
                total += area * perimeter

    return total


with open("input.txt", "r") as inputfile:
    grid = [list(line.strip()) for line in inputfile]

for line in grid:
    print(line)

# Calculate total sum of area * perimeter for all regions
result = calculate_total(grid)
print(f"Total sum of area * perimeter: {result}")
