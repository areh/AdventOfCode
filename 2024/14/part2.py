with open("input.txt", "r") as inputfile:
  inputdata = inputfile.read()

Gx, Gy = 101, 103

robots = []
for robotdata in inputdata.split("\n"):
  if len(robotdata) > 1:
    robot = {}
    for data in robotdata.split(" "):
      if len(data) > 1:
        pv = data.split("=")
        xy = pv[1].split(",")
        if pv[0] == 'p':
          robot["Px"], robot["Py"] = int(xy[0]), int(xy[1])
        elif pv[0] == 'v':
          robot["Vx"], robot["Vy"] = int(xy[0]), int(xy[1])
    robots.append(robot)

s=0
loopit = True
while loopit:
  grid = [[0 for i in range(Gx)] for j in range(Gy)]
  s+=1
  isbad = False
  for robot in robots:
    Posx = robot['Px']+s*robot['Vx']
    Posx = Posx % Gx
    Posy = robot['Py']+s*robot['Vy']
    Posy = Posy % Gy
    grid[Posy][Posx] += 1
    if grid[Posy][Posx] > 1:
      isbad = True
  if not isbad:
    for line in grid:
      for d in line:
        if d == 1:
          c = "#"
        else:
          c = "."
        print(c, end="")
      print("")
    print(f"Seconds to tree: {s}")
    loopit = False
  if s > Gx*Gy:
    print(f"Not seen in {Gx*Gy} seconds, aborting")
    loopit = False
