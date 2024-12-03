def is_safe(line):
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

    return safe


#inputFile = open("02_test_data.txt", "r")
inputFile = open("02_input.txt", "r")
lines = inputFile.readlines()

safelines = 0

for line in lines:
    print("Line '" + line.strip() + "'", end=" ")
    if is_safe(line):
        print("  is SAFE without exclusion", end=" ")
        safelines += 1
    else:
        linesplit = line.split()
#        print(linesplit)

        safecheck = 0
#        print("DEBUG length of line split: " + str(len(linesplit)))

        for i in range(len(linesplit)):
#            print("DEBUG i = " + str(i) + " :: " + linesplit[i])
            tempsplit = linesplit.copy()
            del tempsplit[i]
            templine = " ".join(tempsplit)
            if is_safe(templine):
                print("  Modified line '" + templine.strip() + "' is SAFE", end=" ")
                safecheck += 1
        if safecheck > 0:
            safelines += 1
    print(" ")


print("There are " + str(safelines) + " safe lines")


