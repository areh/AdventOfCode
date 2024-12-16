import numpy as np

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

seconds = 100
grid = np.zeros((Gy, Gx), dtype=int)

for robot in robots:
  Posx = robot['Px']+seconds*robot['Vx']
  while not 0 <= Posx < Gx:
    if Posx < 0:
      Posx += Gx
    else:
      Posx -= Gx
  Posy = robot['Py']+seconds*robot['Vy']
  while not 0 <= Posy < Gy:
    if Posy < 0:
      Posy += Gy
    else:
      Posy -= Gy
  grid[Posy][Posx] += 1

safety = sum(sum([grid[i][:Gx // 2] for i in range(Gy // 2)])) * sum(sum([grid[i][(Gx // 2)+1:] for i in range(Gy // 2)])) * sum(sum([grid[i][:Gx // 2]     for i in range((Gy // 2)+1, Gy)])) * sum(sum([grid[i][(Gx // 2)+1:] for i in range((Gy // 2)+1, Gy)]))

print(f"Total safety factor: {safety}")
