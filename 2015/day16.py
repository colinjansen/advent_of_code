from collections import defaultdict
import re

def build_map():
    M = {}
    with open("_input/day16.txt") as f:
        for line in f.read().splitlines():
            m = re.match(r"Sue (\d*): (.*)", line)
            num = int(m[1])
            M[num] = {}
            for prop in m[2].split(", "):
                key, value = prop.split(": ")
                M[num][key] = int(value)
    return M

def filter_v1(sues, key, value):
    filtered = {}
    for num, props in sues.items():
        if key in props and props[key] != value:
            continue
        filtered[num] = props
    return filtered

def filter_v2(sues, key, value):
    def keep(props, key):
        if key not in props:
            return True
        if key in ["cats", "trees"]:
            return props[key] > value
        if key in ["pomeranians", "goldfish"]:
            return props[key] < value
        return props[key] == value

    filtered = {}
    for num, props in sues.items():
        if keep(props, key):
            filtered[num] = props
    return filtered

filter = filter_v2

sues = build_map()
sues = filter(sues, "children", 3)
sues = filter(sues, "cats", 7)
sues = filter(sues, "samoyeds", 2)
sues = filter(sues, "pomeranians", 3)
sues = filter(sues, "akitas", 0)
sues = filter(sues, "vizslas", 0)
sues = filter(sues, "goldfish", 5)
sues = filter(sues, "trees", 3)
sues = filter(sues, "cars", 2)
sues = filter(sues, "perfumes", 1)

print(sues)