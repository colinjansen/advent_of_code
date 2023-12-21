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
    rules, defaultDestination = rule
    for r in rules:
        node, operation, value, destination = r
        if operation == '>' and o[node] > value: return destination
        if operation == '<' and o[node] < value: return destination
    return defaultDestination
    
def run(o, node):
    while node not in 'RA':
        node = run_rules(o, RULES[node])
    return sum(o.values()) if node == 'A' else 0

def part1():
    return sum([run(o, 'in') for o in OBJ])

def part2():
    for r in RULES:
        print(r, RULES[r])
        

parse()

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')