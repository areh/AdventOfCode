from collections import Counter

with open("input.txt", "r") as inputfile:
  pebbles = inputfile.read().strip().split()

stones = Counter(pebbles)

for i in range(75):
  if i == 25:
    print(f"Part 1: {sum(stones.values())}")
  new_stones = Counter()
  for stone, num in stones.items():
    if stone == '0':
      new_stones['1'] += num
    elif len(stone) % 2 == 0:
      new_stones[stone[0:len(stone)//2]] += num
      new_stones[str(int(stone[len(stone)//2:]))] += num
    else:
      new_stones[str(int(stone)*2024)] += num
  stones = new_stones
  
print(f"Part 2: {sum(stones.values())}")
