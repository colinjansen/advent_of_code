from collections import deque
import math

with open('_input/day24.txt') as f:
    lines = f.read().splitlines()


def draw(storms: list[tuple], ME: tuple, h: int, w: int, t: int):

    grid = [['#'] * w for _ in range(h)]

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            grid[y][x] = ' '

    grid[0][1] = ' '
    grid[h-1][w-2] = ' '

    for storm in storms:
        grid[storm[0]][storm[1]] = '.'

    grid[ME[0]][ME[1]] = '*'

    print(' -- variation ', t, ' -- ')

    for g in grid:
        print(''.join(g))


def storm_permutations(lines: list[str]) -> dict:

    def parse_storm_information(lines):
        storms = []
        h = len(lines)
        w = len(lines[0])
        for y in range(h):
            for x in range(w):
                if lines[y][x] == 'v':
                    storms.append((y, x, 1, 0))
                    continue
                if lines[y][x] == '>':
                    storms.append((y, x, 0, 1))
                    continue
                if lines[y][x] == '<':
                    storms.append((y, x, 0, -1))
                    continue
                if lines[y][x] == '^':
                    storms.append((y, x, -1, 0))
                    continue
        return storms, h, w

    def move_storms(storms: list[tuple], h: int, w: int) -> list[tuple]:
        new_positions = []
        for storm in storms:
            y = storm[0] + storm[2]
            x = storm[1] + storm[3]
            if y == 0:
                y = h - 2
            if x == 0:
                x = w - 2
            if y == h - 1:
                y = 1
            if x == w - 1:
                x = 1
            new_positions.append((y, x, storm[2], storm[3]))
        return new_positions

    def get_all_storm_permutations(lines: list[str]) -> dict:
        permutations = {}
        storms, h, w = parse_storm_information(lines)
        lcm = math.lcm(h-2, w-2)
        count = 0
        while count < lcm:
            l = []
            for s in storms:
                l.append((s[0], s[1]))
            permutations[count] = l
            storms = move_storms(storms, h, w)
            count += 1

        return permutations, h, w

    return get_all_storm_permutations(lines)


def part1(lines):
    print('getting storm permutations')
    perms, h, w = storm_permutations(lines)
    print(f'found {len(perms)} variations')

    END = (h-1, w-2)
    START = (0, 1)

    # starting position
    Q = deque()
    Q.append((START, 469))
    DP = set()
    while Q:

        # pop the last know state
        ME, steps = Q.popleft()

        if ME == END:
            print(steps)
            break

        # if we've hit a border
        if ME[0] <= 0 or ME[1] <= 0 or ME[0] >= h-1 or ME[1] >= w-1:
            if ME != START:
                continue

        state = (ME, steps)
        if state in DP:
            continue
        DP.add(state)

        # the next permutation in the list
        next = (steps + 1) % len(perms)

        # where the storms are going to be
        storms = perms[next]

        #draw(storms, ME, h, w, steps+1)

        # possible positions to move to
        B = (ME[0]-1, ME[1])
        F = (ME[0]+1, ME[1])
        L = (ME[0], ME[1]-1)
        R = (ME[0], ME[1]+1)
        N = (ME[0], ME[1])

        # can we move back
        if B not in storms:
            Q.append((B, steps + 1))
        # can we move forward
        if F not in storms:
            Q.append((F, steps + 1))
        # can we move left
        if L not in storms:
            Q.append((L, steps + 1))
        # can we move right
        if R not in storms:
            Q.append((R, steps + 1))
        # can we stand where we are
        if N not in storms:
            Q.append((N, steps + 1))


part1(lines)
