with open("input.txt", "r") as inputfile:
    flist = list(inputfile.read().strip())

fid = 0
dmap = []

for id, fdata in enumerate(flist):
    f = int(fdata)
    if id % 2 == 0:
        for x in range(f):
            dmap.append(fid)
        fid += 1
    else:
        for x in range(f):
            dmap.append(-1)

preved = len(dmap)
for id in range(len(dmap)):
    if dmap[id] < 0:
        for ed in reversed(range(id, preved)):
            if dmap[ed] >= 0:
                if ed > id:
                    dmap[id], dmap[ed] = dmap[ed], dmap[id]
                    preved = ed
                    break

checksum = 0
for i, d in enumerate(dmap):
    if d > 0:
        checksum += i*d

print("The checksum is: " + str(checksum))

