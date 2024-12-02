import re

codes = []
rules = {}

with open('_input/day19.txt') as fp:
    for line in fp.readlines():
        if ':' not in line:
            codes.append(line.strip())
            continue
        parts = line.split(':')
        rules[parts[0]] = parts[1].strip()

def expand(rule):
    if rule.startswith('"'):
        return rule.strip('"')
    return f"({''.join(['|' if p == '|' else expand(rules[p]) for p in rule.split()])})"

rx = re.compile(expand(rules['0']))

print(sum([1 for c in codes if rx.fullmatch(c)]))