import re
from collections import defaultdict

R = []
V = []
with open('2024/_input/day14.txt') as f:
    for line in f.readlines():
        px, py, vx, vy = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups()
        R.append((int(px), int(py)))
        V.append((int(vx), int(vy)))

width = 101
height = 103

def move(times = 1, width = 100, height = 103):
    collection1 = defaultdict(list)
    collection2 = defaultdict(list)
    for i in range(len(R)):
        R[i] = (R[i][0] + V[i][0] * times, R[i][1] + V[i][1] * times)
        R[i] = (R[i][0] % width, R[i][1] % height)
        collection1[R[i][1]].append(R[i][0])
        collection2[R[i][0]].append(R[i][1])
    return collection1, collection2


def get_quad_count():
    """
    Returns the number of points in each quadrant
    
    Returns:
        list: [Q1, Q2, Q3, Q4]
        top left, bottom left, top right, bottom right
    """
    Q = [0, 0, 0, 0]
    for r in R:
        if r[0] < width // 2: # left
            if r[1] < height // 2:
                Q[0] += 1
            if r[1] > height // 2:
                Q[1] += 1
        if r[0] > width // 2: # right
            if r[1] < height // 2:
                Q[2] += 1
            if r[1] > height // 2:
                Q[3] += 1
    return Q

def show():
    for y in range(height):
        for x in range(width):
            if (x, y) in R:
                print('#', end='')
            else:
                print('.', end='')
        print()

def part2():
    seconds = 0
    while True:
        c1, c2 = move(1, width, height)
        seconds += 1
        if 2 <= sum(1 for points in c1.values() if len(points) >= 30):
            if 2 <= sum(1 for points in c2.values() if len(points) >= 30):
                print(seconds)
                show()
                break

part2()