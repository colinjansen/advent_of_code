import re
from collections import deque

with open("_input/day16.txt", encoding='utf8') as f:
    lines = f.read().splitlines()


valves = {}
tunnels = {}
dists = {}
cache = {}
nonempty = []

for line in lines:
    g = re.match(
        'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)', line).groups()
    valves[g[0]] = int(g[1])
    tunnels[g[0]] = g[2].split(', ')

#
# get distances to neighbouring valves
#
for valve in valves:
    if valve != 'AA' and not valves[valve]:
        continue
    if valve != 'AA':
        nonempty.append(valve)
    dists[valve] = {valve: 0, 'AA': 0}
    visited = {valve}
    queue = deque([(0, valve)])
    while queue:
        distance, position = queue.popleft()
        for neighbour in tunnels[position]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if valves[neighbour]:
                dists[valve][neighbour] = distance + 1
            queue.append((distance + 1, neighbour))
    del dists[valve][valve]
    if valve != 'AA':
        del dists[valve]['AA']

indices = {}
for i, el in enumerate(nonempty):
    indices[el] = i


def search(time, valve, mask):
    if (time, valve, mask) in cache:
        return cache[(time, valve, mask)]
    max_flow = 0
    for neighbour in dists[valve]:
        bit = 1 << indices[neighbour]
        if mask & bit:
            continue
        remaining_time = time - dists[valve][neighbour] - 1
        if remaining_time <= 0:
            continue
        max_flow = max(max_flow, search(remaining_time, neighbour, mask | bit) + (valves[neighbour] * remaining_time))
    cache[(time, valve, mask)] = max_flow
    return max_flow

part1 = search(30, 'AA', 0)

b = (1 << len(nonempty)) - 1

m = 0
for i in range((b + 1) // 2):
    m = max(m, search(26, 'AA', i) + search(26, 'AA', b ^ i))

print(part1, m)
