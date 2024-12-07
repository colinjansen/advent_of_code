import re
from collections import Counter, defaultdict

with open('2019/_input/day3.txt') as fp:
    w1 = fp.readline()
    w2 = fp.readline()

def get_direction(d):
    if d == 'U':
        return (-1, 0)
    if d == 'D':
        return (1, 0)
    if d == 'R':
        return (0, 1)
    if d == 'L':
        return (0, -1)
    
def run_wire(w1):
    visited = defaultdict(list)
    position = (0, 0)
    steps = 0
    for s in w1.split(','):
        d = get_direction(s[0])
        for _ in range(int(s[1:])):
            steps += 1
            position = (position[0] + d[0], position[1] + d[1])
            visited[position].append(steps)
    return visited

v1 = run_wire(w1)
v2 = run_wire(w2)

part1 = float('inf')
part2 = float('inf')
for x, y in set(v1.keys()).intersection(set(v2.keys())):
    part1 = min(part1, abs(x) + abs(y))
    part2 = min(part2, min(v1[(x, y)]) + min(v2[(x, y)]))
print(part1)
print(part2)