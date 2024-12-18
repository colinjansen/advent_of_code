from dataclasses import dataclass
import re

@dataclass
class Coordinate:
    x: int
    y: int

@dataclass
class Machine:
    a: Coordinate
    b: Coordinate
    position: Coordinate

machines = {}
with open('2024/_input/day13.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 4):
        ax, ay = re.match(r'Button A: X(.*), Y(.*)', lines[i]).groups()
        bx, by = re.match(r'Button B: X(.*), Y(.*)', lines[i+1]).groups()
        px, py = re.match(r'Prize: X=(.*), Y=(.*)', lines[i+2]).groups()
        machine = Machine(Coordinate(int(ax), int(ay)), Coordinate(int(bx), int(by)), Coordinate(int(px), int(py)))
        machines[i] = machine

def moves(machine, mod=0):
    machine.position.x += mod
    machine.position.y += mod
    a = machine.position.x // machine.a.x
    while a > 0:
        # move to some 'a' position
        b = 0
        while True:
            # move to some 'b' position
            _x = (machine.a.x * a) + (machine.b.x * b)
            _y = (machine.a.y * a) + (machine.b.y * b)
            if _x == machine.position.x and _y == machine.position.y:
                return a, b
            # overshot?
            if _x > machine.position.x or _y > machine.position.y:
                break
            b += 1
        a -= 1
    return None

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

m = machines[0]

def check(m):
    i = line_intersection(((0,0), (m.a.x, m.a.y)), ((m.position.x-m.b.x, m.position.y-m.b.y), (m.position.x, m.position.y)))
    if i and i[0] % m.a.x == 0 and (m.position.y - i[1]) % m.b.y == 0:
        _a = i[0] / m.a.x
        _b = (m.position.y - i[1]) / m.b.y
        return _a*3 + _b
    return None

part1 = 0
part2 = 0
for m in machines.values():
    v = check(m)
    if v:
        part1 += v
    m.position.x += 10000000000000
    m.position.y += 10000000000000
    v = check(m)
    if v:
        part2 += v
        
print(part1, part2)
