import re
from functools import reduce

with open("_input/day2.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

def part_1(game_string):
    m = { 'red': 12, 'green': 13, 'blue': 14 } # max counts
    for g in game_string.split(';'):
        for e in g.split(','):
            g = re.match('(\d+) (red|blue|green)$', e.strip()).groups()
            c = g[1] # colour
            q = int(g[0]) # quantity
            if q > m[c]:
                return False
    return True

def part_2(game_string):
    m = {} # max counts
    for g in game_string.split(';'):
        for e in g.split(','):
            g = re.match('(\d+) (red|blue|green)$', e.strip()).groups()
            c = g[1] # colour
            q = int(g[0]) # quantity
            if c not in m:
                m[c] = q
                continue
            if q > m[c]:
                m[c] = q
    return reduce(lambda x, y: x * y, m.values())
    
p_1 = 0
p_2 = 0
for line in lines:
    match = re.match('Game (\d+): (.*)$', line)
    game = int(match.groups()[0])
    p_1 += game if part_1(match.groups()[1]) else 0
    p_2 += part_2(match.groups()[1])

print(f'Part 1: {p_1} Part 2: {p_2}')