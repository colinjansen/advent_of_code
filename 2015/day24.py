from itertools import combinations
from math import prod

WEIGHTS = sorted([1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113], reverse=True)


target = sum(WEIGHTS) / 4

def smallest():
    found = False
    perms = set()
    for n in range(len(WEIGHTS)):
        if found:
            return perms
        for p in combinations(WEIGHTS, n):
            if sum(p) == target:
                found = True
                perms.add(tuple(sorted(p)))

def qest(perms):
    best = float('inf')
    for s in perms:
        best = min(best, prod(s))
    return best

perms = smallest()
print(f"found {len(perms)} permutations")
print(qest(perms))