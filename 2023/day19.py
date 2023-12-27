import re
import copy

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

def sum_state(S):
    t = 1
    for c in 'xmas':
        t *= S[c][1] - S[c][0] + 1
    return t

def mod_state(S, n, s, v):
    if s == '>':
        S[n][0] = max(S[n][0], v + 1)
    if s == '<':
        S[n][1] = min(S[n][1], v - 1)
    if s == '>=':
        S[n][0] = max(S[n][0], v)
    if s == '<=':
        S[n][1] = min(S[n][1], v)
    return S

def invalid_state(S):
    for c in 'xmas':
        if S[c][0] > S[c][1]:
            return True
    return False

parse()
print(f'part 1: {part1()}')

Q = []
Q.append(('in', {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}))

part2 = 0
while Q:
    n, S = Q.pop()
    if n == 'R' or invalid_state(S):
        continue
    if n == 'A':
        part2 += sum_state(S)
        continue
    
    for r in RULES[n]:
        if isinstance(r, list): # fancy rules
            for _n, _s, _v, _d in r:
                Q.append((_d, mod_state(copy.deepcopy(S), _n, _s, _v)))
                S = mod_state(copy.deepcopy(S), _n, '<=' if _s == '>' else '>=', _v)
        else:
            Q.append((r, S))

print(f'part 2: {part2}')
