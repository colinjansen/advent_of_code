from computer import Computer
from collections import defaultdict

with open('2019/_input/day11.txt') as f:
    program = f.read().strip()

map = defaultdict(int)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
position = (0, 0)
map[position] = 1
c = Computer(program)
c.add_input(map[position])

mode = 0
def handle_output(v):
    global mode, position, direction, directions
    if mode == 0: #paint
        map[position] = v
        
    if mode == 1: # move
        direction += -1 if v == 0 else 1
        direction %= 4
        d = directions[direction]
        position = (position[0] + d[0], position[1] + d[1])
        c.add_input(map[position])

    mode = (mode + 1) % 2

c.go(handle_output)
print(len(map))

def show(map):
    rows, cols = 0, 0
    for r, c in map:
        rows = max(rows, r)
        cols = max(cols, c)

    M = []
    for _ in range(rows + 1):
        M.append([' '] * (cols + 1))

    for r, c in map:
        M[r][c] = '#' if map[(r, c)] == 1 else ' '

    for r in M:
        print(''.join(r))

print(show(map))