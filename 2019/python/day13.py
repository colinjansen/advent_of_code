from computer import Computer
from collections import defaultdict


with open('2019/_input/day13.txt') as f:
    program = f.readline().strip()

def show(map):
    rows, cols = 0, 0
    for x, y in map:
        rows = max(rows, y)
        cols = max(cols, x)
                   
    M = []
    for _ in range(rows + 1):
        M.append([' '] * (cols + 1))

    for x, y in map:
        t = map[(x, y)]
        if t == 0:
            M[y][x] = ' '
        if t == 1:
            M[y][x] = '#'
        if t == 2:
            M[y][x] = '*'
        if t == 3:
            M[y][x] = '-'
        if t == 4:
            M[y][x] = 'o'

    for row in M:
        print(''.join(row))

c = Computer(program)

output = []
map = defaultdict(int)
c.go(lambda v: output.append(v))
i = 0
while i < len(output):
    map[(output[i], output[i+1])] = output[i+2]
    i += 3

show(map)