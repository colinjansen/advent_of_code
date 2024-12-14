import os
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

def part1(program):
    c = Computer(program)
    output = []
    map = defaultdict(int)
    c.go(lambda v: output.append(v))
    i = 0
    while i < len(output):
        map[(output[i], output[i+1])] = output[i+2]
        i += 3

    return len([1 for x in map.values() if x == 2])

ball = None
paddle = None
score = 0

def part2(program):

    def handle_output(v):
        global ball, paddle, score
        output.append(v)
        if len(output) == 3:
            if output[0] == -1 and output[1] == 0:
                score = output[2]
            else:
                if output[2] == 3:
                    paddle = (output[0], output[1])
                if output[2] == 4:
                    ball = (output[0], output[1])
                map[(output[0], output[1])] = output[2]
            output.clear()

    def handle_input():
        global ball, paddle
        if paddle[1] <= ball[1]:
            return 0
        if paddle[0] > ball[0]:
            return -1
        if paddle[0] < ball[0]:
            return 1
        return 0
    
    c = Computer(program)
    c.set_memory(0, 2)
    output = []
    map = defaultdict(int)
    c.go(output_function=handle_output, input_function=handle_input)

    return score

print('part 1', part1(program))
print('part 2', part2(program))