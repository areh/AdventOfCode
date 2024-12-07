### Functions
def check_range(posX, posY, maxX, maxY, minX=0, minY=0):
    if minX <= posX <= maxX and minY <= posY <= maxY:
        return True
    else:
        return False

### Main

#with open("test_input.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    grid = [list(line.strip()) for line in inputfile]

total = 0

maxEW = len(grid[0])-1
maxNS = len(grid)-1

# Find initial position
for y, line in enumerate(grid):
    if "^" in line:
        posNS = y
        for x, char in enumerate(line):
            if char == "^":
                posEW = x

# Set direction "N"
dr = "N"

inside = True
while inside:
    grid[posNS][posEW] = "X"
    
    match dr:
        case "N":
            if check_range(posEW, posNS-1, maxEW, maxNS, 0, 0):
                if grid[posNS-1][posEW] == "#":
                    dr = "E"
                else:
                    posNS -= 1
            else:
                inside = False
        case "S":
            if check_range(posEW, posNS+1, maxEW, maxNS, 0, 0):
                if grid[posNS+1][posEW] == "#":
                    dr = "W"
                else:
                    posNS += 1
            else:
                inside = False
        case "W":
            if check_range(posEW-1, posNS, maxEW, maxNS, 0, 0):
                if grid[posNS][posEW-1] == "#":
                    dr = "N"
                else:
                    posEW -= 1
            else:
                inside = False
        case "E":
            if check_range(posEW+1, posNS, maxEW, maxNS, 0, 0):
                if grid[posNS][posEW+1] == "#":
                    dr = "S"
                else:
                    posEW += 1
            else:
                inside = False
    if grid[posNS][posEW] == "X":
        total += 1

print("The total is: " + str(total))

