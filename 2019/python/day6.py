from collections import defaultdict

map = defaultdict(str)

with open('2019/_input/day6.txt') as fp:
    for line in fp.readlines():
        a, b = line.strip().split(')')
        map[b] = a

def connections(t):
    c = 0
    a = map[t]
    v = defaultdict(int)
    v[a] = c
    while a in map:
        c += 1
        a = map[a]
        v[a] = c
    return v

def part1():
    t = 0
    for k in map.keys():
        v = connections(k)
        t += len(v)
    return t

def part2():
    t1 = connections('YOU')
    t2 = connections('SAN')
    for k in t2.keys():
        if k in t1:
            return t1[k] + t2[k]

print('part 1:', part1(), 'part 2:', part2())
