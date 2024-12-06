def findmid(listin):
    m = float(len(listin))/2
    if m % 2 != 0:
        return listin[int(m - .5)]
    else:
        return 0

def is_ordered(pageset):
  setok = True
  for rule in rules:
    if rule[0] in pageset and rule[1] in pageset:
      if pageset.index(rule[0]) > pageset.index(rule[1]):
        setok = False
  return setok


### Main

inputfile = open("input.txt", "r")
#inputfile = open("test_input.txt", "r")
lines = inputfile.readlines()
inputfile.close()

total = 0

#Split lines into two new arrays, one with rules and one with pages
rules = []
pagesets = []

for line in lines:
  if "|" in line:
    rules.append([int(x) for x in line.strip().split("|")])
  if "," in line:
    pagesets.append([int(x) for x in line.strip().split(",")])

fixpagesets = []
for pageset in pagesets:
  if not is_ordered(pageset):
    fixpagesets.append(pageset)

#Kinda bubble sort / brute force change of the pagestes to fix
for pageset in fixpagesets:
  while not is_ordered(pageset):
    for a in range(len(pageset)):
      for b in range(a+1, len(pageset)):
        if [pageset[b], pageset[a]] in rules:
          pageset[b], pageset[a] = pageset[a], pageset[b]
  total += findmid(pageset)

print("The total is: " + str(total))
