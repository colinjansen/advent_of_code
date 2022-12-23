import re

with open('_input/day22.txt') as f:
    lines = f.read().splitlines()

me = None
trail = {}

def trans(c):
    if c == '-': return '#'
    if c == ' ': return '.'
    if c == '.': return ' '
    if c == '#': return '*'
    if c == 'M': return 'M'
    return c


def draw_grid(grid):
    for key in trail:
        grid[key[0]][key[1]] = trail[key]
    grid[me[0]][me[1]] = 'M'
    for g in grid:
        print(''.join([trans(c) for c in g]))


def get_grid(lines):
    global me
    # get max line length
    m = 0
    for i in range(len(lines) - 2):
        m = max(len(lines[i]), m)
    grid = [[' '] * (m+2) for _ in range(len(lines))]

    # copy our input into the grid
    for y in range(len(lines) - 2):
        for x in range(len(lines[y])):
            c = lines[y][x]
            if me == None and c == '.':
                me = (y + 1, x + 1, '>') # starting position
            if c == ' ':
                continue
            grid[y + 1][x + 1] = lines[y][x]
    return grid


def get_moves(lines):
    input = lines[-1:][0]
    moves = []
    for t in re.findall('(\d+)(\w?)', input):
        moves.append(int(t[0]))
        moves.append(t[1])
    return moves


def turn(d):
    global me
    if d == 'R':
        if me[2] == '>': return (me[0], me[1], 'v')
        if me[2] == 'v': return (me[0], me[1], '<')
        if me[2] == '<': return (me[0], me[1], '^')
        if me[2] == '^': return (me[0], me[1], '>')
    if d == 'L':
        if me[2] == '<': return (me[0], me[1], 'v')
        if me[2] == '^': return (me[0], me[1], '<')
        if me[2] == '>': return (me[0], me[1], '^')
        if me[2] == 'v': return (me[0], me[1], '>')
    return me


def get_next_block():
    global grid, me
    y = me[0]
    x = me[1]
    if me[2] == '>': x += 1
    if me[2] == '<': x -= 1 
    if me[2] == '^': y -= 1
    if me[2] == 'v': y += 1
    if (grid[y][x] == ' '):
        if me[2] == '^': # up
            while grid[y][x] == ' ': 
                y = (y - 1) % len(grid)
        if me[2] == 'v': # down
            while grid[y][x] == ' ': 
                y = (y + 1) % len(grid)
        if me[2] == '>': # right
            while grid[y][x] == ' ': 
                x = (x + 1) % len(grid[y])
        if me[2] == '<': # left
            while grid[y][x] == ' ':
                x = (x - 1) % len(grid[y])
    return (y, x)


def walk(steps):
    global me
    for _ in range(steps):
        y, x = get_next_block()
        if grid[y][x] == '.': 
            trail[(me[0], me[1])] = me[2]
            me = (y, x, me[2])
            continue
        if grid[y][x] == '#':
            return


grid = get_grid(lines)
moves = get_moves(lines)

for m in range(0, len(moves), 2):
    walk(moves[m])
    me = turn(moves[m+1])

def get_facing():
    global me
    if me[2] == '^': return 3
    if me[2] == '>': return 0
    if me[2] == 'v': return 1
    if me[2] == '<': return 2

#draw_grid(grid)
print(f'1000 * {me[0]} + 4 * {me[1]} + {get_facing()}')
print((me[0] * 1000) + (me[1] * 4) + get_facing())