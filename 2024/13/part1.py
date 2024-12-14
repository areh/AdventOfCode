import re

with open("input.txt", "r") as inputfile:
  inputdata = inputfile.read()

def extract_xy(line):
  xys = re.search(".*X.(\d+).*Y.(\d+)", line)
  return xys.groups()

prizes = []
for chunk in inputdata.split("\n\n"):
  prize = {}
  for line in chunk.split("\n"):
    if len(line) > 1:
      x, y = extract_xy(line)
      if "Button A" in line:
        prize["Ax"], prize["Ay"] = int(x), int(y)
      elif "Button B" in line:
        prize["Bx"], prize["By"] = int(x), int(y)
      elif "Prize" in line:
        prize["Px"], prize["Py"] = int(x), int(y)
  prizes.append(prize)

total = 0
for idx, prize in enumerate(prizes):
  for a in range(1, 101):
    for b in range(1, 101):
      if a*prize['Ax']+b*prize['Bx'] == prize['Px'] and a*prize['Ay']+b*prize['By'] == prize['Py']:
        total += a*3+b

print(f"Total tokens: {total}")
