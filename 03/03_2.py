import re

inputfile = open("03_input.txt", "r")
inputdata = inputfile.read()
inputfile.close()

total = 0

outerex = re.split(r"don't\(\)", inputdata)

first = True

for outer in outerex:
  if first:
    multext = outer
    first = False
  else:
    inner = re.search(r"do\(\)(.*)", outer)
    if inner:
      multext = inner.group()
    else:
      multext = None

  if multext:
    matches = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", multext)
    for match in matches:
      calc = int(match[0])*int(match[1])
#      print(str(match[0]) + " * " + str(match[1]) + " = " + str(calc))
      total += calc
    matches.clear()

print("The total is: " + str(total))

