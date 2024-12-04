inputFile = open("input.txt", "r")
lines = inputFile.readlines()

listA = []
listB = []

for line in lines:
    linesplit = line.split()
    listA.append(linesplit[0])
    listB.append(linesplit[1])

listA.sort()
listB.sort()

distance = 0
pos = 0
for a in listA:
    distance += abs(int(a) - int(listB[pos]))
#    if (a > listB[pos]):
#        notice = "A > B"
#    else:
#        notice = "OK"
#    print("A: " + a + " :: B: " + listB[pos] + " :: " + notice)
    pos += 1

print("Distance: " + str(distance) + " ?")

