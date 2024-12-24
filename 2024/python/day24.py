from collections import defaultdict
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
        elif op == 'OR':
            return get_value(a) | get_value(b)
        elif op == 'XOR':
            return get_value(a) ^ get_value(b)



part1 = 0
for i, key in enumerate(sorted([ z for z in I.keys() if z[0] == 'z' ])):
    part1 += get_value(key) << i
print('part 1:', part1)