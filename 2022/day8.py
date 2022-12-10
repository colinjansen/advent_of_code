import re

with open("_input/day8.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

g = [[0] * len(lines[0]) for _ in range(len(lines))]
for i in range(0, len(g[0])): 
    g[0][i] = 1
    g[-1][i] = 1
for i in range(0, len(g)): 
    g[i][0] = 1
    g[i][-1] = 1

def leftToRight(lines, y):
    t = int(lines[y][0])
    for i in range(1, len(lines[y])):
        c = int(lines[y][i])
        if (c > t):
            g[y][i] += 1
            t = c

def rightToLeft(lines, y):
    t = int(lines[y][-1])
    for i in range(len(lines[y]) - 2, -1, -1):
        c = int(lines[y][i])
        if (c > t):
            g[y][i] += 1
            t = c

def upToDown(lines, x):
    t = int(lines[0][x])
    for i in range(1, len(lines)):
        c = int(lines[i][x])
        if (c > t):
            g[i][x] += 1
            t = c
            
def downToUp(lines, x):
    t = int(lines[-1][x])
    for i in range(len(lines) - 2, -1, -1):
        c = int(lines[i][x])
        if (c > t):
            g[i][x] += 1
            t = c

def count_g():
    count = 0
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            if g[i][j] > 0: count += 1
    return count

def print_g():
    for l in g:
        print(l)

def score_right(y, x):
    s = 0
    tree_height = lines[y][x]
    t = x + 1
    while (t < len(lines[y])):
        if (lines[y][t] < tree_height): 
            s += 1
            t += 1
            continue
        if (lines[y][t] >= tree_height): 
            s += 1
            break
    return s

def score_left(y, x):
    s = 0
    tree_height = lines[y][x]
    t = x - 1
    while (t >= 0):
        if (lines[y][t] < tree_height): 
            s += 1
            t -= 1
            continue
        if (lines[y][t] >= tree_height): 
            s += 1
            break
    return s

def score_down(y, x):
    s = 0
    tree_height = lines[y][x]
    t = y + 1
    while (t < len(lines)):
        if (lines[t][x] < tree_height): 
            s += 1
            t += 1
            continue
        if (lines[t][x] >= tree_height): 
            s += 1
            break
    return s

def score_up(y, x):
    s = 0
    tree_height = lines[y][x]
    t = y - 1
    while (t >= 0):
        if (lines[t][x] < tree_height): 
            s += 1
            t -= 1
            continue
        if (lines[t][x] >= tree_height): 
            s += 1
            break
    return s

def score(y, x):
    r = score_right(y, x)
    l = score_left(y, x)
    d = score_down(y, x)
    u = score_up(y, x)
    return r * l * d * u

for x in range(0, len(lines)):
    leftToRight(lines, x)
    rightToLeft(lines, x)
for x in range(0, len(lines[0])):
    upToDown(lines, x)
    downToUp(lines, x)
part1 = count_g()

g = [[0] * len(lines[0]) for _ in range(len(lines))]

part2 = 0
for y in range(0, len(lines)):
    for x in range(0, len(lines[i])):
        s = score(y, x)
        if s > part2: part2 = s
        g[y][x] = s
print(part2)

#print(f'part 1 is {0}, part 2 is {0}')