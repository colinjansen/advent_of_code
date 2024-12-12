from functools import cache, lru_cache
from collections import Counter, defaultdict, deque
from itertools import permutations, pairwise
import re

map = []
with open('2024/_input/day12.txt') as f:
    for line in f.readlines():
        map.append(line.strip())

from functools import lru_cache

def find_islands():        
    islands = []
    visited = set()

    def count_corner_blocks(island):
        """
        ...
        ##.
        .#.
        
        """
        corners = 0
        for r, c in island:

            # outside corners

            # top left
            if (r, c-1) not in island and (r-1, c) not in island:
                corners += 1
            # top right
            if (r-1,c) not in island and  (r, c+1) not in island:
                corners += 1
            # bottom left
            if (r, c-1) not in island and (r+1, c) not in island:
                corners += 1
            # bottom right
            if (r+1, c) not in island and (r, c+1) not in island:
                corners += 1

            # inside corners

            # top left
            if (r-1, c) in island and (r, c-1) in island and (r-1, c-1) not in island:
                corners += 1
            # top right
            if (r-1, c) in island and (r, c+1) in island and (r-1, c+1) not in island:
                corners += 1
            # bottom left
            if (r+1, c) in island and (r, c-1) in island and (r+1, c-1) not in island:
                corners += 1
            # bottom right
            if (r+1, c) in island and (r, c+1) in island and (r+1, c+1) not in island:
                corners += 1

        return corners


    def calc_perimiter(island):
        perimiter = 0
        for r, c in island:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (r+dr, c+dc) not in island:
                    perimiter += 1
        return perimiter

    def explore(r, c):
        island = set()
        t = map[r][c]
        Q = deque([(r, c)])
        while Q:
            r, c = Q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            island.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                _r = r + dr
                _c = c + dc
                if 0 <= _r < len(map) and 0 <= _c < len(map[0]) and map[_r][_c] == t and (_r, _c) not in visited:
                    Q.append((_r, _c))
        return frozenset(island)

    for r in range(len(map)):
        for c in range(len(map[0])):
            if (r, c) not in visited:
                i = explore(r, c)
                islands.append({ 
                    'type': map[r][c], 
                    'island': i,
                    'area': len(i),
                    'sides': count_corner_blocks(i),
                    'perimiter': calc_perimiter(i)
                })
                print('island', map[r][c], len(i), count_corner_blocks(i))
    return islands

def part1(islands):
    return sum(i['area'] * i['perimiter'] for i in islands)

def part2(islands):
    return sum(i['area'] * i['sides'] for i in islands)

I = find_islands()

print(part1(I))
print(part2(I))