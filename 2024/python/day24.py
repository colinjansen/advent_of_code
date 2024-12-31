from collections import Counter
import re

C = {}
I = {}
with open('2024/_input/day24.txt') as f:
    a, b = f.read().split("\n\n")

for i in a.split("\n"):
    n, v = i.split(':')
    C[n.strip()] = int(v)

for inst in b.split("\n"):
    a, op, b, to = re.match(r'(.+) (AND|OR|XOR) (.+) -> (.+)', inst.strip()).groups()
    I[to] = (a, op, b)

def get_value(wire):
    if wire in C:
        return C[wire]
    if wire in I:
        a, op, b = I[wire]
        if op == 'AND':
            return get_value(a) & get_value(b)
        if op == 'OR':
            return get_value(a) | get_value(b)
        if op == 'XOR':
            return get_value(a) ^ get_value(b)

def part1():
    part1 = 0
    for i, key in enumerate(sorted([z for z in I.keys() if z[0] == 'z' ])):
        part1 += get_value(key) << i
    return part1

def part2():
    swapped = []

    def find(a, b, o):
        for k, v in I.items():
            if v == (a, o, b) or v == (b, o, a):
                return k
        return None

    def eq(e, a, b, o):
        return e == (a, o, b) or e == (b, o, a)

    def swap(a, b):
        t = I[a]
        I[a] = I[b]
        I[b] = t

    def find_unmatched(keys):
        return [k for k, v in Counter(keys).items() if v == 1]

    def find_problem():

        a = find('x00', 'y00', 'AND')
        for i in range(1, 44):
            X = f'x{i:02}'
            Y = f'y{i:02}'
            Z = f'z{i:02}'

            b = find(X, Y, 'XOR')
            assert b and b[0] not in 'xyz', f'{Z} Could not find B for {X} XOR {Y}'

            z = find(a, b, 'XOR')
            if z == None:
                _a, _o, _b = I[Z]
                return find_unmatched([a, b, _a, _b])
            if z != Z:
                _a, _o, _b = I[Z]
                err = find(_a, _b, _o)
                if err == Z:
                    return z, err

            c = find(b, a, 'AND')
            assert c and c[0] not in 'xyz', f'{Z} Could not find C for {b} AND {a}'

            d = find(X, Y, 'AND')
            assert d and d[0] not in 'zxy', f'{Z} Could not find D for {X} AND {Y}'

            a = find(c, d, 'OR')
            assert a and a[0] not in 'xyz', f'{Z} Could not find A for {c} OR {d}'

        return None

    while find_problem():
        a, b = find_problem()
        swap(a, b)
        #print('swapping', a, b)
        swapped.extend([a, b])

    return ','.join(sorted(swapped))

print('part 1:', part1())

print('part 2:', part2())