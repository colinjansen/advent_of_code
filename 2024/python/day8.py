import re
from itertools import combinations, permutations
from collections import defaultdict, Counter

map = []
with open('2024/_input/day8.txt') as fp:
    part1 = part2 = 0
    for line in fp.readlines():
        map.append(list(line.strip()))

ant = defaultdict(list)
for i, r in enumerate(map):
    for j, c in enumerate(r):
        if c != '.':
            ant[c].append((i, j))

def on_map(n):
    return 0 <= n[0] < len(map) and 0 <= n[1] < len(map[0])

def get_anti_nodes_part1(l):
    anti_nodes = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            dx = l[i][0] - l[j][0]
            dy = l[i][1] - l[j][1]
            a1 = (l[j][0] - dx, l[j][1] - dy)
            a2 = (l[i][0] + dx, l[i][1] + dy)
            if on_map(a1):
                anti_nodes.append(a1)
            if on_map(a2):
                anti_nodes.append(a2)
    return set(anti_nodes)

def get_anti_nodes_part2(l):
    anti_nodes = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            anti_nodes.append((l[i][0], l[i][1]))
            anti_nodes.append((l[j][0], l[j][1]))
            dx = l[i][0] - l[j][0]
            dy = l[i][1] - l[j][1]
            
            a1 = (l[j][0] - dx, l[j][1] - dy)
            while on_map(a1):
                anti_nodes.append(a1)
                a1 = (a1[0] - dx, a1[1] - dy)

            a2 = (l[i][0] + dx, l[i][1] + dy)
            while on_map(a2):
                anti_nodes.append(a2)
                a2 = (a2[0] + dx, a2[1] + dy)
    return set(anti_nodes)

part1 = set()
part2 = set()
for k, v in ant.items():
    part1.update(get_anti_nodes_part1(v))
    part2.update(get_anti_nodes_part2(v))
print(len(part1), len(part2))