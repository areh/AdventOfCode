def findmid(listin):
    m = float(len(listin))/2
    if m % 2 != 0:
        return listin[int(m - .5)]
    else:
        return 0

inputfile = open("input.txt", "r")
#inputfile = open("test_input.txt", "r")
lines = inputfile.readlines()
inputfile.close()

total = 0

rules = []
pagesets = []

for line in lines:
  if "|" in line:
    rules.append([int(x) for x in line.strip().split("|")])
  if "," in line:
    pagesets.append([int(x) for x in line.strip().split(",")])


for pageset in pagesets:
  setok = True
  for rule in rules:
    if rule[0] in pageset and rule[1] in pageset:
      if pageset.index(rule[0]) > pageset.index(rule[1]):
        setok = False
  if setok:
    total += findmid(pageset)

print("The total is: " + str(total))
