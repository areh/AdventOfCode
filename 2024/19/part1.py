patterns = []
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if "," in line:
            towels = line.split(", ")
        elif len(line) > 1:
            patterns.append(line.strip())

def can_construct(pattern, towels):
    towelset = set(towels)
    dp = [False]*(len(pattern) + 1)
    dp[0] = True

    for i in range(1, len(pattern) + 1):
        for j in range(i):
            if dp[j] and pattern[j:i] in towelset:
                dp[i] = True
                break
    return dp[len(pattern)]

total = 0
for pattern in patterns:
    if can_construct(pattern, towels):
        total += 1

print(f"Total patterns constructable: {total}")

