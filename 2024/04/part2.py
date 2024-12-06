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

print("The total is: " + str(total))
