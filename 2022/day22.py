import re

with open('_input/day22.txt') as f:
    lines = f.read().splitlines()


def trans(c):
    if c == '-':
        return '#'
    if c == ' ':
        return '.'
    if c == '.':
        return ' '
    if c == '#':
        return '*'
    if c == 'M':
        return 'M'
    return c


def draw_grid(grid, trail, me):
    for key in trail:
        grid[key[0]][key[1]] = trail[key]
    grid[me[0]][me[1]] = 'M'
    for g in grid:
        print(''.join([trans(c) for c in g]))


def draw_grid2(grid, trail, me, warps):
    for key in trail:
        grid[key[0]][key[1]] = trail[key]
    for key in warps:
        w = warps[key]
        grid[key[0]][key[1]] = 'w'
        grid[w[0]][w[1]] = 'o'
    grid[me[0]][me[1]] = 'M'
    for g in grid:
        print(''.join([trans(c) for c in g]))


def get_grid(lines, me=None):
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
                me = (y + 1, x + 1, '>')  # starting position
            if c == ' ':
                continue
            grid[y + 1][x + 1] = lines[y][x]
    return grid, me


def get_moves(lines):
    input = lines[-1:][0]
    moves = []
    for t in re.findall('(\d+)(\w?)', input):
        moves.append(int(t[0]))
        moves.append(t[1])
    return moves


def turn(d, me):
    if d == 'R':
        if me[2] == '>':
            return (me[0], me[1], 'v')
        if me[2] == 'v':
            return (me[0], me[1], '<')
        if me[2] == '<':
            return (me[0], me[1], '^')
        if me[2] == '^':
            return (me[0], me[1], '>')
    if d == 'L':
        if me[2] == '<':
            return (me[0], me[1], 'v')
        if me[2] == '^':
            return (me[0], me[1], '<')
        if me[2] == '>':
            return (me[0], me[1], '^')
        if me[2] == 'v':
            return (me[0], me[1], '>')
    return me


def get_next_block(grid, me):
    y = me[0]
    x = me[1]
    d = me[2]
    if me[2] == '>':
        x += 1
    if me[2] == '<':
        x -= 1
    if me[2] == '^':
        y -= 1
    if me[2] == 'v':
        y += 1
    if (grid[y][x] == ' '):
        if me[2] == '^':  # up
            while grid[y][x] == ' ':
                y = (y - 1) % len(grid)
        if me[2] == 'v':  # down
            while grid[y][x] == ' ':
                y = (y + 1) % len(grid)
        if me[2] == '>':  # right
            while grid[y][x] == ' ':
                x = (x + 1) % len(grid[y])
        if me[2] == '<':  # left
            while grid[y][x] == ' ':
                x = (x - 1) % len(grid[y])
    return (y, x, d)


def get_next_block2(grid, me, warps):
    y = me[0]
    x = me[1]
    d = me[2]
    if d == '>':
        x += 1
    if d == '<':
        x -= 1
    if d == '^':
        y -= 1
    if d == 'v':
        y += 1
    if (grid[y][x] == ' '):
        y, x, d = warps[(y, x, d)]
    return (y, x, d)


def walk(steps, grid, me, trail):
    for _ in range(steps):
        y, x, d = get_next_block(grid, me)
        if grid[y][x] == '.':
            trail[(me[0], me[1])] = me[2]
            me = (y, x, d)
            continue
        if grid[y][x] == '#':
            break
    return me, trail


def walk2(steps, grid, me, trail, warps):
    for _ in range(steps):
        y, x, d = get_next_block2(grid, me, warps)
        if grid[y][x] == '.':
            trail[(me[0], me[1])] = me[2]
            me = (y, x, d)
            continue
        if grid[y][x] == '#':
            break
    return me, trail


def get_facing(me):
    if me[2] == '^':
        return 3
    if me[2] == '>':
        return 0
    if me[2] == 'v':
        return 1
    if me[2] == '<':
        return 2


def create_warps(s):
    warps = {}
    for i in range(s):
        # from F to L and L to F
        warps[((s*2)-i, s, '<')] = ((s*2)+1, s-i, 'v') # ok
        warps[((s*2), s-i, '^')] = ((s*2)-i, s+1, '>') # ok
        # from D to R and R to D
        warps[(s-i, (s*3)+1, '>')] = ((s*2)+i+1, (s*2), '<') # ok
        warps[((s*2)+i+1, (s*2)+1, '>')] = (s-i, s*3, '<') # ok
        # from F to R and R to F
        warps[(s+1, (s*2)+i+1, 'v')] = (s+i+1, (s*2), '<') # ok
        warps[(s+i+1, (s*2)+1, '>')] = (s, (s*2)+i+1, '^') # ok
        # from B to D and D to B
        warps[((s*3)+i+1, s+1, '>')] = ((s*3), s+i+1, '^') # ok
        warps[(s*3+1, (s)+i+1, 'v')] = ((s*3)+i+1, s, '<') # ok
        # from U to L and L to U
        warps[(s-i, s, '<')] = ((s*2)+i+1, 1, '>') # ok
        warps[((s*2)+i+1, 0, '<')] = (s-i, s+1, '>') # ok
        # from B to R and R to B
        warps[((s*4)+1, s-i, 'v')] = (1, (s*3)-i, 'v') # ok
        warps[(0, (s*3)-i, '^')] = ((s*4), s-i, '^') # ok
        # from U to B and B to U
        warps[(0, (s*2)-i, '^')] = ((s*4)-i, 1, '>') # ok
        warps[((s*4)-i, 0, '<')] = (1, (s*2)-i, 'v')
    
    return warps


def part1(lines):
    trail = {}
    grid, me = get_grid(lines)
    moves = get_moves(lines)
    for m in range(0, len(moves), 2):
        me, trail = walk(moves[m], grid, me, trail)
        me = turn(moves[m+1], me)
    print(f'1000 * {me[0]} + 4 * {me[1]} + {get_facing(me)}')
    return (me[0] * 1000) + (me[1] * 4) + get_facing(me)


def part2(lines):
    trail = {}
    warps = create_warps(50)
    grid, me = get_grid(lines)
    moves = get_moves(lines)
    for m in range(0, len(moves), 2):
        me, trail = walk2(moves[m], grid, me, trail, warps)
        me = turn(moves[m+1], me)
    draw_grid2(grid, trail, me, warps)
    print(f'1000 * {me[0]} + 4 * {me[1]} + {get_facing(me)}')
    return (me[0] * 1000) + (me[1] * 4) + get_facing(me)


print(part2(lines))
