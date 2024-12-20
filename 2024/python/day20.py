from collections import defaultdict, deque

def get_track():
    start = None
    end = None
    path = set()
    with open('2024/_input/day20.txt') as f:
        for r, line in enumerate(f.readlines()):
            for c, char in enumerate(line):
                if char == 'S':
                    start = (r, c)
                if char == 'E':
                    end = (r, c)
                if char in '.E':
                    path.add((r, c))
    return start, end, path

start, end, path_set = get_track()

path = []
Q = deque([start])
while Q:
    p = Q.popleft()
    path.append(p)
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        _p = (dr + p[0], dc + p[1])
        if _p in path_set:
            path_set.remove(_p)
            Q.append(_p)

C = defaultdict(int)
for p in path:
    for dr, dc in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
        _p = (dr + p[0], dc + p[1])
        if _p in path:
            delta = path.index(_p) - path.index(p) - 2
            if delta > 0:
                C[delta] += 1
part1 = 0
for k, v in C.items():
    if k >= 100:
        part1 += v
print(part1)