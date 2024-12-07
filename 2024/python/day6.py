from datetime import datetime
import multiprocessing

MAP = []
with open('2024/_input/day6.txt') as fp:
    for line in fp.readlines():
        MAP.append(list(line))

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

def rotate(d):
    if d == DOWN:
        return LEFT
    if d == LEFT:
        return UP
    if d == UP:
        return RIGHT
    if d == RIGHT:
        return DOWN
    return (0, 0)

def find_guard():
    for i, r in enumerate(MAP):
        for j, c in enumerate(r):
            if c == '^':
                return (i, j)
    return (-1, -1)

def on_map(x, y):
    return x >= 0 and y >= 0 and x < len(MAP) and y < len(MAP[0])

def get_char(x, y, block=(-1,-1)):
    if x == block[0] and y == block[1]:
        return '#'
    if not on_map(x, y):
        return None
    return MAP[x][y]

def part1():
    # initial direction
    dr, dc = UP
    # initial position
    r, c = find_guard()

    V = set()
    while on_map(r, c):
        # turn if we need to
        ch = get_char(r + dr, c + dc)
        while ch == '#':
            dr, dc = rotate((dr, dc))
            ch = get_char(r + dr, c + dc)

        # move by the movement delta
        r = r + dr
        c = c + dc

        # remember this location, distinctly
        V.add((r, c))

    return V

def is_loop(block):
    # initial direction
    dr, dc = UP
    # initial position
    r, c = find_guard()

    V = set()
    while on_map(r, c):

        # turn if we need to
        ch = get_char(r + dr, c + dc, block)
        while ch == '#':
            dr, dc = rotate((dr, dc))
            ch = get_char(r + dr, c + dc)

        # move by the movement delta
        r = r + dr
        c = c + dc

        # have we been here before?
        DC = (r, c, dr, dc)
        if DC in V:
            return True

        V.add(DC)

    return False

if __name__ == '__main__':
    start = datetime.now()
    path = part1()
    print('part 1:', len(path), 'steps')
    with multiprocessing.Pool(16) as pool:
        print('part 2:', sum([1 if r else 0 for r in pool.map(is_loop, path)]), 'possibilities')
        pool.close()
    print('elapsed:', datetime.now() - start)
