import re

with open("_input/day5.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

p1 = ''
p2 = 0

g = {}

def addToGraph(c, i):
    if i not in g: g[i] = []
    if c != ' ': g[i].append(c)

def moveSingleCrates(a, f, t):
    for i in range(0, a):
        lift = g[f][-1:]
        left = g[f][:len(g[f])-1]
        g[f] = left
        g[t].extend(lift)

def moveMultipleCrates(a, f, t):
    lift = g[f][-a:]
    left = g[f][:len(g[f])-a]
    g[f] = left
    g[t].extend(lift)

def printGraph():
    for i in g:
        print (i, g[i])

for e in reversed(lines[:8]):
    for x in range(1, len(e), 4):
        addToGraph(e[x], int(x / 4) + 1)

for i, move in enumerate(lines[10:]):
    match = re.match("move (\d+) from (\d+) to (\d+)", move)
    groups = match.groups()
    moveMultipleCrates(int(groups[0]), int(groups[1]), int(groups[2]))

for i in g:
    p1 += g[i][-1:][0]

print(f'part 1 is {p1}, part 2 is {p2}')