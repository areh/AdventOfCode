import re

with open("input.txt", "r") as inputfile:
  inputdata = inputfile.read()

def extract_xy(line):
  xys = re.search(".*X.(\d+).*Y.(\d+)", line)
  return xys.groups()

prizeadd = 10000000000000

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
        prize["Px"], prize["Py"] = int(x)+prizeadd, int(y)+prizeadd
  prizes.append(prize)


total = 0
for idx, prize in enumerate(prizes):
  print(f"Prize {idx} :: {prize}")
  a = int(int(prize['Px']*prize['By'] - prize['Py']*prize['Bx']) / int(prize['Ax']*prize['By'] - prize['Ay']*prize['Bx']))
  b = int(int(prize['Ax']*prize['Py'] - prize['Ay']*prize['Px']) / int(prize['Ax']*prize['By'] - prize['Ay']*prize['Bx']))
  if a*prize['Ax']+b*prize['Bx'] == prize['Px'] and a*prize['Ay']+b*prize['By'] == prize['Py']:
    print(f"  Found solution A: {a}  B: {b}")
    total += a*3+b
  else:
    print("  No solution!")

print(f"Total tokens: {total}")
