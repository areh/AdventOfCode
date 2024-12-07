from itertools import product
from functools import reduce

def solve(solution, factors):
    for ops in product("*+", repeat=len(factors)-1):
        op = iter(ops)
        result = reduce(lambda x,y: x*y if next(op) == '*' else x+y, factors)
        if result == solution:
            return solution
    return 0

with open("input.txt", "r") as inputfile:
    problems = [line.strip().split() for line in inputfile]

total = 0

for problem in problems:
    solution = int(problem[0].rstrip(":"))
    factors = []
    for f in range(1, len(problem)):
        factors.append(int(problem[f]))
    total += solve(solution, factors)

print("The total is: " + str(total))

