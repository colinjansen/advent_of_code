import re

P = ''
N = []

def pattern_match(pattern, perm):
    if len(pattern) != len(perm):
        return -3
    for i, _ in enumerate(pattern):
        if perm[i] == '.' and pattern[i] not in ['.', '?']:
            return -2
        if perm[i] == '#' and pattern[i] not in ['#', '?']:
            return -1
    return True

with open("day12.output.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        
        if line.startswith("--------"):
            continue
            
        match = re.match(r'(.*) \[([^\]]+)\]', line)
        if match:
            groups = match.groups()
            P = groups[0]
            N = list(map(lambda x: int(x), groups[1].split(',')))
            continue
        
        r = pattern_match(P, line)
        if r != True:
            print(r, P, N, line)