from collections import deque
from typing import Dict, List, Set, Tuple


all_paths = set()
start, end = None, None
with open('2024/_input/day16.txt') as f:
    width = 0
    height = 0
    for r, line in enumerate(f.readlines()):
        height = r
        for c, char in enumerate(line):
            width = len(line.strip())
            if char in '.ES':
                all_paths.add((r, c))
            if char == 'S':
                start = (r, c)
            if char == 'E':
                end = (r, c)

def find_min_cost(path, start, end):
    r, c = start
    Q = deque([(r, c, (0, 1), 0)])
    visited = {}
    while Q:
        r, c, d, cost = Q.popleft()
        if (r, c) in visited and visited[(r, c)] < cost:
            continue
        visited[(r, c)] = cost
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c, new_d = r + dr, c + dc, (dr, dc)
            if (new_r, new_c) in path:
                Q.append((new_r, new_c, new_d, cost + 1 if new_d == d else cost + 1001))
    return visited[end]

def get_best_paths(all_path, start, target, max_cost):
    r, c = start
    good_paths = {}
    Q = deque([(r, c, (0, 1), 0, [start])])
    while Q:
        r, c, direction, cost, current_path = Q.popleft()
        if cost > max_cost:
            continue
        if (r, c) == target:
            if cost not in good_paths:
                good_paths[cost] = []
            good_paths[cost].append(current_path)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c, new_d = r + dr, c + dc, (dr, dc)
            if (new_r, new_c) in all_path and (new_r, new_c) not in current_path:
                Q.append((new_r, new_c, new_d, cost + 1 if new_d == direction else cost + 1001, current_path + [(new_r, new_c)]))
    return good_paths

best = set()
def add_path(path):
    for p in path:
        best.add(p)
    print(f'adding path: {len(best)}')

min_cost = find_min_cost(all_paths, start, end)
best_paths = get_best_paths(all_paths, start, end, min_cost)

lowest_cost = min(best_paths.keys())
for path in best_paths[lowest_cost]:
    for p in path:
        best.add(p)

for r in range(height + 1):
    for c in range(width + 1):
        if (r, c) in all_paths:
            if (r, c) in best:
                print('O', end='')
            else:
                print('.', end='')
        else:
            print(' ', end='')
    print()

print('part 1:', min_cost)
print('part 2:', len(best))