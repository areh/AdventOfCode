from collections import deque

Gx, Gy = 71, 71
maxbytes = 1024
with open("input.txt", "r") as inputfile:
  inputdata = inputfile.read()

def shortest_path(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        row, col, dist = queue.popleft()
        
        if row == rows - 1 and col == cols - 1:
            return dist
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))
    return -1

grid = [[0 for i in range(Gx)] for j in range(Gy)]
for memspace in inputdata.split("\n"):
    if len(memspace) > 1:
        memsplit = memspace.split(",")
        memX, memY = int(memsplit[0]), int(memsplit[1])
        grid[memY][memX] = 1
        if shortest_path(grid) == -1:
            print(f"Last memory corrupted: {memspace}")
            break

