import re

lines = open('_input/day7.txt', 'r').readlines()
wires = {}


class node:
    def __init__(self, op):
        self.val = None
        self.op = op

    def read(self):
        if self.val == None:
            self.val = self.op() & 0xffff
        return self.val


def check(id: str):
    return id in wires and wires[id].read() != None


def value_node(v: str):
    return lambda: int(v)


def connect_node(id: str):
    return lambda: wires[id].read() if check(id) else None


def not_node(id: str):
    return lambda: ~(wires[id].read()) if check(id) else None


def lshift_node(id: str, shift: str):
    return lambda: wires[id].read() << int(shift) if check(id) else None


def rshift_node(id: str, shift: str):
    return lambda: wires[id].read() >> int(shift) if check(id) else None


def and_node(id1: str, id2: str):
    if id1.isnumeric():
        return lambda: int(id1) & wires[id2].read() if check(id2) else None
    if id2.isnumeric():
        return lambda: int(id2) & wires[id1].read() if check(id1) else None
    return lambda: wires[id1].read() & wires[id2].read() if check(id1) and check(id2) else None


def or_node(id1: str, id2: str):
    if id1.isnumeric():
        return lambda: int(id1) | wires[id2].read() if check(id2) else None
    if id2.isnumeric():
        return lambda: int(id2) | wires[id1].read() if check(id1) else None
    return lambda: wires[id1].read() | wires[id2].read() if check(id1) and check(id2) else None


def parse(lines):
    for line in lines:
        m = re.search('([a-z]+|[0-9]+) (AND|OR) ([a-z]+) -> ([a-z]+)', line)
        if m != None:
            if m[2] == 'AND':
                wires[m[4]] = node(and_node(m[1], m[3]))
                continue
            if m[2] == 'OR':
                wires[m[4]] = node(or_node(m[1], m[3]))
                continue

        m = re.search('([a-z]+) (LSHIFT|RSHIFT) ([0-9]+) -> ([a-z]+)', line)
        if m != None:
            wires[m[4]] = node(lshift_node(m[1], m[3]))
            if m[2] == 'LSHIFT':
                wires[m[4]] = node(lshift_node(m[1], m[3]))
                continue
            if m[2] == 'RSHIFT':
                wires[m[4]] = node(rshift_node(m[1], m[3]))
                continue

        m = re.search('NOT ([a-z]+) -> ([a-z]+)', line)
        if m != None:
            wires[m[2]] = node(not_node(m[1]))
            continue

        m = re.search('([a-z]+) -> ([a-z]+)', line)
        if m != None:
            wires[m[2]] = node(connect_node(m[1]))
            continue

        m = re.search('([0-9]+) -> ([a-z]+)', line)
        if m != None:
            wires[m[2]] = node(value_node(m[1]))
            continue

wires.clear()
parse(lines)
print(f"part A = wires[a] = {wires['a'].read()}")

# modify the lines with the value from part 'A'
lines = list(map(lambda a: f'{wires["a"].read()} -> b' if a.strip().endswith('-> b') else a, lines))

wires.clear()
parse(lines)
print(f"part B = wires[a] = {wires['a'].read()}")
