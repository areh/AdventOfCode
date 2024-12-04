#inputFile = open("test_input.txt", "r")
inputFile = open("input.txt", "r")
lines = inputFile.readlines()

safelines = 0

for line in lines:
    safe = True
    dirok = True
    linesplit = line.split()
    if int(linesplit[1]) - int(linesplit[0]) > 0:
        ascending = True
    else:
        ascending = False
    pos = 0
    for l in linesplit:
        if pos > 0:
            splitdiff = int(l) - int(linesplit[pos-1])
            if abs(splitdiff) > 3:
                safe = False
            if safe:
                if splitdiff > 0:
                    if not ascending:
                        dirok = False
                elif splitdiff < 0:
                    if ascending:
                        dirok = False
                else:
                    dirok = False
        pos += 1
    if not dirok:
        safe = False
    if safe:
        print("Line '" + line.strip() + "' is SAFE")
        safelines += 1
    else:
        print("Line '" + line.strip() + "' is UNSAFE")

print("There are " + str(safelines) + " safe lines")

