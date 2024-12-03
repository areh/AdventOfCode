import re

inputfile = open("03_input.txt", "r")
inputdata = inputfile.read()
inputfile.close()

matches = re.findall("mul\((\d{1,3})\,(\d{1,3})\)", inputdata)

total = 0

for match in matches:
  calc = int(match[0])*int(match[1])
  print(str(match[0]) + " * " + str(match[1]) + " = " + str(calc))
  total += calc

print("The total is: " + str(total))

