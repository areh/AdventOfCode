patterns = []
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if "," in line:
            towels = line.split(", ")
        elif len(line) > 1:
            patterns.append(line.strip())

def count_pattern(pattern, towels):
    towelset = set(towels)
    dp = [0]*(len(pattern) + 1)
    dp[0] = 1

    for i in range(1, len(pattern) + 1):
        for j in range(i):
            if dp[j] and pattern[j:i] in towelset:
                dp[i] += dp[j]

    return dp[len(pattern)]

total = 0
for pattern in patterns:
    total += count_pattern(pattern, towels)

print(f"Total pattern combinations: {total}")

