inputfile = open("input.txt", "r")
#inputfile = open("test_input.txt", "r")
lines = inputfile.readlines()
inputfile.close()

total = 0

for y in range(1,  len(lines)-1):
  for x in range(1, len(lines[y])-1):
    if lines[y][x] == "A":
      str_tl_br = lines[y-1][x-1]+lines[y][x]+lines[y+1][x+1]
      if str_tl_br == "MAS" or str_tl_br == "SAM":
        str_tr_bl = lines[y-1][x+1]+lines[y][x]+lines[y+1][x-1]
        if str_tr_bl == "MAS" or str_tr_bl == "SAM":
          total+=1


#for lnum, line in enumerate(lines):
##  print("\nlnum: " + str(lnum) + " ::", end=" ")
#  for c in range(len(line)):
##    print(str(c), end=" ")
#    if line[c] == "X":
#      if c+3 <= len(line):              # Right
#        if line[c+1] == "M":
#          if line[c+2] == "A":
#            if line[c+3] == "S":
#              total += 1
#      if c-3 >= 0:                      # Left
#        if line[c-1] == "M":
#          if line[c-2] == "A":
#            if line[c-3] == "S":
#              total += 1
#      if lnum+3 < len(lines):           # Down
#        if lines[lnum+1][c] == "M":
#          if lines[lnum+2][c] == "A":
#            if lines[lnum+3][c] == "S":
#              total += 1
#        if c+3 <= len(line):              # - Right
#          if lines[lnum+1][c+1] == "M":
#            if lines[lnum+2][c+2] == "A":
#              if lines[lnum+3][c+3] == "S":
#                total += 1
#        if c-3 >= 0:                      # - Left
#          if lines[lnum+1][c-1] == "M":
#            if lines[lnum+2][c-2] == "A":
#              if lines[lnum+3][c-3] == "S":
#                total += 1
#      if lnum >= 3:                     # Up
#        if lines[lnum-1][c] == "M":
#          if lines[lnum-2][c] == "A":
#            if lines[lnum-3][c] == "S":
#              total += 1
#        if c+3 <= len(line):              # - Right
#          if lines[lnum-1][c+1] == "M":
#            if lines[lnum-2][c+2] == "A":
#              if lines[lnum-3][c+3] == "S":
#                total += 1
#        if c-3 >= 0:                      # - Left
#          if lines[lnum-1][c-1] == "M":
#            if lines[lnum-2][c-2] == "A":
#              if lines[lnum-3][c-3] == "S":
#                total += 1

print("The total is: " + str(total))