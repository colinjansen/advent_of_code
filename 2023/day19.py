import re

OBJ = []
RULES = {}

def parse():
    with open("_input/day19.txt", encoding='utf8') as f:
        for line in f.read().splitlines():
            if not line:
                continue
            if line[0] == '{':
                # {x=1020,m=854,a=3295,s=1367}
                o = {}
                for n, v in list(map(lambda x: x.split('='), line[1:-1].split(','))):
                    o[n] = int(v)
                OBJ.append(o)
                continue
            # dc{m<2846:ldt,x>2708:xf,s>1203:rb,zpn}
            n, v = re.match(r'(.*){(.*)}', line).groups()
            R = []
            D = None
            for v in v.split(','):
                if ':' in v:
                    p, s, v, c = re.match(r'(\w+)([><])(\d+):(\w+)', v).groups()
                    R.append((p, s, int(v), c))
                else:
                    D = v
            RULES[n] = (R, D)

def run_rules(o, rule):
    rules, de = rule
    for r in rules:
        a, b, c, d = r
        if b == '>' and o[a] > c: return d
        if b == '<' and o[a] < c: return d
    return de
    
def run(o, start='in'):
    r = start
    while r not in 'RA':
        r = run_rules(o, RULES[r])
    if r == 'A':
        return sum(o.values())
    return 0

def part1():
    t = 0
    for o in OBJ:
        t += run(o)
    return t

parse()

print(f'part 1: {part1()}')