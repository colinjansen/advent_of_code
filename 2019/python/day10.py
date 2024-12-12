MAP = []
with open('2019/_input/day10.txt') as f:
    for line in f.readlines():
        MAP.append(line.strip())
def get_starts():
    return [(x, y) for x, r in enumerate(MAP) for y, c in enumerate(r )if c == '#']

print(get_starts())