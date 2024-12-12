from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
import re

map = []
with open("2024/_input/day10.txt") as f:
    for line in f.readlines():
        map.append(line.strip())

def find_trailheads(map):
    trailheads = []
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "0":
                trailheads.append((r, c))
    return trailheads

def find_trailends(map):
    trailheads = []
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "9":
                trailheads.append((r, c))
    return trailheads

def traverse(map, head):
    visited = set()
    q = deque([head])
    ends = []
    while q:
        r, c, height = q.popleft()

        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        if height == 9:
            ends.append((r, c))
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(map) and 0 <= new_c < len(map[0]) and int(map[new_r][new_c]) == height + 1:
                q.append((new_r, new_c, height + 1))
    return len(ends)

def find_all_paths(map, head):
    visited = {}
    q = deque([head])
    ends = []

    while q:
        r, c, max_paths = q.popleft()

        if (r, c) in visited:
            max_paths = max(max_paths, visited[(r, c)])
        visited[(r, c)] = max_paths + 1
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(map) and 0 <= new_c < len(map[0]) and map[new_r][new_c] != '.' and int(map[new_r][new_c]) == int(map[r][c]) + 1:
                q.append((new_r, new_c, max_paths))
    return visited

part1 = sum([ traverse(map, (r, c, 0)) for r, c in find_trailheads(map) ])
part2 = sum(sum(res[end] for end in find_trailends(map) if end in res) for r, c in find_trailheads(map) for res in [find_all_paths(map, (r, c, 0))])


print('part1:', part1)
print('part2:', part2)