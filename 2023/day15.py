import re

with open("_input/day15.txt", encoding="utf8") as f:
    steps = f.read().splitlines()[0].split(',')

def hash(s):
    t = 0
    for c in s:
        t += ord(c) 
        t *= 17
        t %= 256
    return t

def part_2():
    D = {}
    def replace(k, l, v):
        for i, _ in enumerate(D[k]):
            if D[k][i][0] == l:
                D[k][i] = (l, v)
                return True
        return False

    for step in steps:
        l, op, v = re.match(r'(\w*)([-=])(\d?)', step).groups()
        k = hash(l)
        if k not in D:
            D[k] = []
        if op == '=':
            if replace(k,l,v):
                continue
            D[k].append((l, v))
        if op == '-':
            D[k] = [i for i in D[k] if i[0] != l]
            
    return sum([(k+1) * (i+1) * int(d[1]) for k in D.keys() for i, d in enumerate(D[k])])

def part_1():
    return sum([hash(s) for s in steps])

print(f'part 1: {part_1()} part 2: {part_2()}')