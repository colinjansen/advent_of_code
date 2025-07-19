import re
from collections import defaultdict
from itertools import permutations

def build_map():
    map = defaultdict(lambda: defaultdict(int))
    with open("_input/day13.txt") as f:
        for line in f.read().splitlines():
            m = re.match(r"(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*).", line)
            map[m[1]][m[4]] = int(m[3]) if m[2] == "gain" else -int(m[3])
    return map

def add_me(M):
    M["Me"] = defaultdict(int)
    return M

def figure_it_out(M):
    ans = 0
    for p in permutations(M.keys()):
        happiness = 0
        for i in range(len(p)):
            A = p[i]
            B = p[(i + 1) % len(p)]
            happiness += M[A][B] + M[B][A]
        ans = max(ans, happiness)
    return ans

print(f'part 1: {figure_it_out(build_map())}')
print(f'part 2: {figure_it_out(add_me(build_map()))}')