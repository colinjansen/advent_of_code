import re
from collections import defaultdict

def build_map():
    R = defaultdict(list)
    S = ''
    with(open("_input/day19.txt", "r") as file):
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = re.match(r"(.+) => (.+)", line)
            if m:
                R[m[1]].append(m[2])
            else:
                S = line
    return R, S

result = set()
r, s = build_map()

for match, replacements in r.items():
    for i in [m.start() for m in re.finditer(match, s)]:
        for replacement in replacements:
            result.add(s[:i] + replacement + s[i+len(match):])

print(len(result))