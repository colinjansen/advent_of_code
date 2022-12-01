from collections import defaultdict
import sys
import re
import math

def day22(lines):

    def get_overlap(c1, c2):
        if any(r1[0] > r2[1] or r2[0] > r1[1] for r1, r2 in zip(c1, c2)):
            return None 
        return tuple([(max(r1[0], r2[0]), min(r1[1], r2[1])) for r1, r2 in zip(c1, c2)])

    cubes = defaultdict(int)
    for line in lines:
        status, coords = line.split()
        x0, x1, y0, y1, z0, z1 = list(map(int, re.findall('-?\d+', coords)))
        c_new = ((x0, x1), (y0, y1), (z0, z1))
        status = re.sub(r'\W+', '', status)
        new_cubes = defaultdict(int)
        for c in cubes:
            overlap = get_overlap(c_new, c)
            if overlap:
                new_cubes[overlap] -= cubes[c]

        if status == 'on':
            new_cubes[c_new] += 1

        for c in new_cubes:
            cubes[c] += new_cubes[c]

    total = 0
    for c in cubes:
        total += math.prod([r[1] - r[0] + 1 for r in c]) * cubes[c]

    print(f'part 2: {total}')

def day23(lines):
    print("hello")

with open(sys.argv[1], encoding='utf8') as f:
    lines = f.readlines()

day23(lines)
