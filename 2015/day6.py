import re

rows = 1000
cols = 1000

def make_grid(rows, cols):
    return [[0 for _ in range(rows)] for _ in range(cols)]

def visit1(l, x1, y1, x2, y2, action):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == 'toggle':
                l[x][y] = int(not l[x][y])
            if action == 'turn off':
                l[x][y] = 0
            if action == 'turn on':
                l[x][y] = 1

def visit2(l, x1, y1, x2, y2, action):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == 'toggle':
                l[x][y] += 2
            if action == 'turn off':
                l[x][y] = max(l[x][y] - 1, 0)
            if action == 'turn on':
                l[x][y] += 1

def count(l):
    c = 0
    for x in range(rows):
        for y in range(cols):
            c += l[x][y]
    return c

l1 = make_grid(rows, cols)
l2 = make_grid(rows, cols)

for line in open('./_input/day6.txt', 'r').readlines():
    m = re.match('(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
    (action, x1, y1, x2, y2) = m.groups()
    visit1(l1, int(x1), int(y1), int(x2), int(y2), action)
    visit2(l2, int(x1), int(y1), int(x2), int(y2), action)
    
print(count(l1))
print(count(l2))