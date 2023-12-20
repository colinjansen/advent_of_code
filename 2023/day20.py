import math
import re

M = {}
BP = 0
MEM = {}

class Broadcaster(object):
    send = []
    on = False
    name = ''
    def __init__(self, name, vals):
        self.send = vals
        self.name = name
        self.on = False

    def pulse(self, f, p):
        for s in self.send:
            P.push(self.name, s, p)

    def __repr__(self) -> str:
        return f'BR {self.name} {self.send}'
    
class FlipFlop(object):
    send = []
    on = False
    name = ''
    def __init__(self, name, vals):
        self.send = vals
        self.name = name
        self.on = False

    def pulse(self, f, p):
        if p == 0:
            self.on = not self.on
            v = 1 if self.on else 0
            for s in self.send:
                P.push(self.name, s, v)

    def __repr__(self) -> str:
        return f'FF {self.name} {self.send}'
    
class Conjunction(object):
    send = []
    mem = {}
    name = ''

    def __init__(self, name, vals, cons):
        self.send = vals
        self.name = name
        self.on = False
        self.mem = {}
        for n, v, t in cons:
            if self.name in v:
                self.mem[n] = 0

    def pulse(self, f, p):
        self.mem[f] = p
        v = 0 if all(self.mem.values()) else 1
        for s in self.send:
            P.push(self.name, s, v)

    
    def __repr__(self) -> str:
        return f'CO {self.name} {self.send}'

class Q(object):
    queue = []
    highs = 0
    lows = 0

    def __init__(self):
        self.highs = 0
        self.lows = 0
        self.queue = []
        self.low_to_rx = False

    def clear(self):
        self.highs = 0
        self.lows = 0
        self.queue.clear()

    def push(self, name, target, value):
        global BP
        if value == 0:
            self.lows += 1
        if value == 1:
            self.highs += 1
        if target in ['gt', 'vr', 'nl', 'lr'] and value == 0:
            if target not in MEM:
                MEM[target] = []
            MEM[target].append(BP)
        self.queue.append((name, target, value))

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def empty(self):
        return not self.queue
    
    def __repr__(self) -> str:
        return f'{self.queue}'


with open("_input/day20.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

cons = []
for line in lines:
    n, v = re.match(r'(broadcaster|[&%]\w+) -> (.*)', line).groups()
    vals = v.split(', ')
    if n[0] == '%':
        cons.append((n[1:], vals, '%'))
    if n[0] == '&':
        cons.append((n[1:], vals, '&'))
    if n == 'broadcaster':
        cons.append((n, vals, 'broadcaster'))

for n, v, t in cons:
    if t == 'broadcaster':
        M[n] = Broadcaster(n, v)
        continue
    if t == '%':
        M[n] = FlipFlop(n, v)
        continue
    if t == '&':
        M[n] = Conjunction(n, v, cons)
        continue


P = Q()

def part1(times = 2):
    t = times
    h = 0
    l = 0
    while t:
        t -= 1
        P.clear()
        P.push('aptly', 'broadcaster', 0)
        while not P.empty():
            name, target, value = P.pop()
            if target in M:
                M[target].pulse(name, value)
        h += P.highs
        l += P.lows
    return h * l

def part2():
    global BP
    def lcm(numbers):
        lcm = 1
        for n in numbers:
            lcm = lcm * n // math.gcd(lcm, n)
        return lcm
    
    while BP < 20_000:
        BP += 1
        P.clear()
        P.push('aptly', 'broadcaster', 0)
        while not P.empty():
            name, target, value = P.pop()
            if target in M:
                M[target].pulse(name, value)
    repeats = []
    for m in MEM:
        print(m, MEM[m][1] - MEM[m][0])
        repeats.append(MEM[m][1] - MEM[m][0])
    return lcm(repeats)

p1 = part1(1000)
print(p1)

p2 = part2()
print(p2)
