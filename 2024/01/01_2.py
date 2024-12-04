inputFile = open("input.txt", "r")
lines = inputFile.readlines()

listA = []
listB = []

for line in lines:
    linesplit = line.split()
    listA.append(linesplit[0])
    listB.append(linesplit[1])

#listA.sort()
#listB.sort()

similarity = 0
#pos = 0
for a in listA:
    similarity += int(a) * listB.count(a)
#    distance += abs(int(a) - int(listB[pos]))
#    if (a > listB[pos]):
#        notice = "A > B"
#    else:
#        notice = "OK"
#    print("A: " + a + " :: B: " + listB[pos] + " :: " + notice)
#    pos += 1

#print("Distance: " + str(distance) + " ?")
print("Similarity: " + str(similarity) + " ?")

