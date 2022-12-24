with open('_input/day23.txt') as f:
    lines = f.read().splitlines()


def draw(elves):
    t = 1_000_000
    b = -1_000_000
    l = 1_000_000
    r = -1_000_000
    for k in elves:
        t = min(t, k[0])
        b = max(b, k[0])
        l = min(l, k[1])
        r = max(r, k[1])
    h = b - t + 1
    w = r - l + 1
    wo = l
    ho = t
    grid = [['.'] * w for _ in range(h)]
    for k in elves:
        grid[k[0] - ho][k[1] - wo] = '#'
    for g in grid:
        print(''.join(g))
    return (w*h) - len(elves)


positions = {}

directions = ['N', 'S', 'W', 'E']

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '#':
            positions[(i, j)] = None


# ===============================================
# set up the elves
# ===============================================

def scan(positions, elf, direction):
    y = elf[0]
    x = elf[1]
    nw = (y-1, x-1) in positions
    n  = (y-1, x) in positions
    ne = (y-1, x+1) in positions
    e  = (y, x+1) in positions
    sw = (y+1, x-1) in positions
    s  = (y+1, x) in positions
    se = (y+1, x+1) in positions
    w  = (y, x-1) in positions
    if sum([nw, n, ne, e, se, s, sw, w]) == 0: return None
    if direction == 'N' and sum([nw, n, ne]) == 0: return (y-1, x)
    if direction == 'S' and sum([sw, s, se]) == 0: return (y+1, x)
    if direction == 'E' and sum([ne, e, se]) == 0: return (y, x+1)
    if direction == 'W' and sum([nw, w, sw]) == 0: return (y, x-1)
    return None

#draw(positions)
round = 1
while True:

    # propose
    for direction in directions:
        for elf in positions:
            if positions[elf] != None:
                continue
            positions[elf] = scan(positions, elf, direction)

    # move the elves
    ne = {}
    for elf in positions:
        c = sum(k == positions[elf] for k in positions.values())
        if c > 1 or positions[elf] == None:
            ne[elf] = None
            continue
        ne[positions[elf]] = None
    
    no_moves = len([elf for elf in positions if positions[elf] != None])
    if no_moves == 0:
        print('no moves on round ', round)
        break
    round += 1

    positions = ne

    # move first direction to last
    directions.append(directions.pop(0))

#print(draw(positions))