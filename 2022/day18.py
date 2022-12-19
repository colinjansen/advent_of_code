import time
from collections import deque 

with open('_input/day18.txt') as f:
    input = f.read().splitlines()

nodes = {}

minX = 10000
maxX = 0
minY = 10000
maxY = 0
minZ = 10000
maxZ = 0

for line in input:
    key = tuple([int(m) for m in line.split(',')])
    minX = min(key[0], minX)
    maxX = max(key[0], maxX)
    minY = min(key[1], minY)
    maxY = max(key[1], maxY)
    minZ = min(key[2], minZ)
    maxZ = max(key[2], maxZ)

for line in input:
    key = tuple([int(m) for m in line.split(',')])
    nodes[key] = 6

    for neighbour in [
        (key[0] + 1, key[1], key[2]),
        (key[0] - 1, key[1], key[2]),
        (key[0], key[1] + 1, key[2]),
        (key[0], key[1] - 1, key[2]),
        (key[0], key[1], key[2] + 1),
        (key[0], key[1], key[2] - 1)
    ]:
        if neighbour in nodes:
            nodes[key] = nodes[key] - 1
            nodes[neighbour] = nodes[neighbour] - 1

print(f'part 1 found: {sum([nodes[idx] for idx in nodes if nodes[idx] >= 0])} sides')

# fill everything with 0s
for key in [(x, y, z) for x in range(minX - 1, maxX + 2) for y in range(minY - 1, maxY + 2) for z in range(minZ - 1, maxZ + 2) if (x, y, z) not in nodes]:
    nodes[key] = -1

# find every empty adjoining node you can
Q = deque([(minX - 1, minY - 1, minZ - 1)])

dx = (maxX - minX) + 2
dy = (maxY - minY) + 2
dz = (maxZ - minZ) + 2
print(f'starting the backfill for {dx} * {dy} * {dz} = {dx * dy * dz} nodes')
counter = 0
while Q:
    e = Q.popleft()
    # have we already been here
    if nodes[e] == 0: continue
    # set this node as visited and up the counter
    nodes[e] = 0
    counter += 1
    if counter % 100 == 0: print(f"\rvisited: {counter} nodes", end='')
    for neighbour in [
        (e[0] + 1, e[1], e[2]),
        (e[0] - 1, e[1], e[2]),
        (e[0], e[1] + 1, e[2]),
        (e[0], e[1] - 1, e[2]),
        (e[0], e[1], e[2] + 1),
        (e[0], e[1], e[2] - 1)
    ]:
        if neighbour in nodes and nodes[neighbour] == -1:
            Q.append(neighbour)

print(f"\rvisited: {counter} nodes")

# find all the -1 nodes
for key in [n for n in nodes if nodes[n] < 0]:
    for neighbour in [
        (key[0] + 1, key[1], key[2]),
        (key[0] - 1, key[1], key[2]),
        (key[0], key[1] + 1, key[2]),
        (key[0], key[1] - 1, key[2]),
        (key[0], key[1], key[2] + 1),
        (key[0], key[1], key[2] - 1)
    ]:
        if nodes[neighbour] > 0:
            nodes[neighbour] -= 1

print(f'part 2 found: {sum([nodes[idx] for idx in nodes if nodes[idx] >= 0])} sides')