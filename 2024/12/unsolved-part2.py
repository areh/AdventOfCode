'''
grid positions are in (r, c) format where r = row or up/down and c = column or left/right
Pseudo code:
    Traverse the grid and find a letter X at position (r, c)
        Find corners:
            Top_left_corner  = True if ((r+(-1),c+0) == [!X or is_out_of_bounds]) and ((r+0,c+(-1)) == [!X or is_out_of_bounds])
            Top_right_corner = True if ((r+0,c+0) != [X || is_out_of_bounds]) and ((0,-1) != [X || is_out_of_bounds])





'''



def calculate_total_with_new_corners(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] == target_letter

    def dfs(r, c, letter):
        stack = [(r, c)]
        visited[r][c] = True
        area = 0
        corners = 0

        while stack:
            x, y = stack.pop()
            area += 1
            # Traverse right and down to count the borders of the region
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                while is_valid(ny, nx) for nx, ny = x + dx, y + dy:
                    if grid[nx][ny] == letter and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                    elif grid[nx][ny] != letter or (nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid)):
                            corners += 1
        return area, corners

    total = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = grid[r][c]
                area, corners = dfs(r, c, letter)
                total += corners * area

    return total


# Input grid
grid = [
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F'],
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F'],
    ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
    ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F'],
    ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E'],
    ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E'],
    ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E'],
    ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']
]

# Calculate total sum of (corners * area) for all regions
result = calculate_total_with_new_corners(grid)
print(f"Total sum of corners * area: {result}")


'''


def calculate_total(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c, letter):
        stack = [(r, c)]
        visited[r][c] = True
        area = 0
        edges = set()

        while stack:
            x, y = stack.pop()
            area += 1

            # Check neighbors (up, down, left, right)
            for dx, dy, edge in [(-1, 0, ((x, y), (x - 1, y))),  # Up
                                 (1, 0, ((x, y), (x + 1, y))),    # Down
                                 (0, -1, ((x, y), (x, y - 1))),   # Left
                                 (0, 1, ((x, y), (x, y + 1)))]:   # Right
                nx, ny = x + dx, y + dy
                if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != letter:
                    # Increment corners when hitting an edge or a different region
                    edges.add(edge)
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        num_sides = len(edges)
        print(f"Letter: {letter} :: Sides: {num_sides} :: Area: {area}")
        print(f"Letter: {letter} :: Corners: {corners} :: Area: {area}")
        return area, num_sides

    total = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Found a new region
                letter = grid[r][c]
                area, sides = dfs(r, c, letter)
                total += sides * area

    return total


with open("test_input.txt", "r") as inputfile:
    grid = [list(line.strip()) for line in inputfile]

#for line in grid:
#    print(line)

# Calculate total sum of area * perimeter for all regions
result = calculate_total(grid)
print(f"Total: {result}")
'''
