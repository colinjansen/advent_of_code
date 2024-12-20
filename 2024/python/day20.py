from collections import defaultdict, deque
from datetime import datetime


def get_track():
    start = None
    end = None
    path_set = set()
    with open('2024/_input/day20.txt') as f:
        for r, line in enumerate(f.readlines()):
            for c, char in enumerate(line):
                if char == 'S':
                    start = (r, c)
                if char == 'E':
                    end = (r, c)
                if char in '.E':
                    path_set.add((r, c))

    ordered_path = []
    Q = deque([start])
    while Q:
        p = Q.popleft()
        ordered_path.append(p)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            _p = (dr + p[0], dc + p[1])
            if _p in path_set:
                path_set.remove(_p)
                Q.append(_p)

    path_index = {p: i for i, p in enumerate(ordered_path)}

    return start, end, path_index

def get_all_points_in_range(r):
    discard = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    points = []
    for dr in range(-r, r+1):
        for dc in range(-r, r+1):
            if abs(dr) + abs(dc) <= r and (dr, dc) not in discard:
                points.append((dr, dc, abs(dr) + abs(dc)))
    return points

def find_shortcuts(path, cheat_range=2):
    cheats = defaultdict(int)
    cheat_points = get_all_points_in_range(cheat_range)
    for p in path.keys():
        for dr, dc, d in cheat_points:
            _p = (dr + p[0], dc + p[1])
            if _p in path:
                delta = path[_p] - path[p] - d
                if delta > 0:
                    cheats[delta] += 1
    return cheats

start, end, path = get_track()

print('part 1', sum(v for k, v in find_shortcuts(path, 2).items() if k >= 100))

print('part 2', sum(v for k, v in find_shortcuts(path, 20).items() if k >= 100))
