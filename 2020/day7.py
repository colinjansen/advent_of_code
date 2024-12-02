import re
from collections import deque

def parse():

    def parse_line(line):
        if line == 'no other bags.':
            return {}
        d = {}
        for l in line.split(','):
            m = re.match('(\d*) (.*) bag', l.strip())
            amount, type = m.groups()
            d[type] = int(amount)
        return d
    
    with open('day7.txt', 'r') as file:
        D = {}
        for line in file.readlines():
            m = re.match('(.*) bags contain (.*)', line)
            type, contains = m.groups()
            D[type] = parse_line(contains)
    return D

def get_containers(D, type):
    l = set()
    for k,v in D.items():
        if type in v.keys():
            l.add(k)
    return l

D = parse()

def part_1(D):
    S = set()
    Q = deque(['shiny gold'])
    while Q:
        type = Q.popleft()
        containers = get_containers(D, type)
        S.update(containers)
        Q.extend(containers)
    return len(S)

def part_2(D):
    C = 0

    Q = deque([(1, 'shiny gold', 1)])
    while Q:
        a, type, m = Q.popleft()
        for v in D[type]:
            C += D[type][v] * (m*a)
            #print(type, D[type][v], v)
            Q.append((D[type][v], v, a*m))
    return C
print('part 2: ', part_2(D))