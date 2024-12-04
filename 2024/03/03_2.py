import re

inputfile = open("input.txt", "r")
inputdata = inputfile.read()
inputfile.close()


compilation = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)|do\(\)|don't\(\)")

total = 0
include = True

for outer in compilation.finditer(inputdata):
  if outer.group() == "do()":
    include = True
  elif outer.group() == "don't()":
    include = False
  elif include:
    total += int(outer.group(1)) * int(outer.group(2))

print("The total is: " + str(total))

