import math
import re

with open("_input/day8.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

D = '' # directions
N = {} # nodes

# pull in the input data
for i, line in enumerate(lines):
    if i == 0:
        D = line
    if i >= 2:
        g = re.match('(\w+) = \((\w+), (\w+)\)', line).groups()
        N[g[0]] = (g[1], g[2])

def lcm(numbers):
    lcm = 1
    for n in numbers:
        lcm = lcm * n // math.gcd(lcm, n)
    return lcm

def find_cycles_to_end_point(node):
    cycles = 0
    while True:
        for d in D:
            node = N[node][0] if d == 'L' else N[node][1]
            cycles += 1
            if node[-1] == 'Z':
                return cycles
            
def part1():
    C = 'AAA'
    s = 0
    while C != 'ZZZ':
        for d in D:
            C = N[C][0] if d == 'L' else N[C][1]
            s += 1
    return s

def part2():
    numbers = []
    # gather starting nodes
    for n in N.keys():
        if n[-1] == 'A':
            numbers.append(find_cycles_to_end_point(n))
    
    return lcm(numbers)

print(f'part 1: {part1()}  part 2: {part2()}')
