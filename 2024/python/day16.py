from collections import deque


path = set()
start, end = None, None
with open('2024/_input/day16.txt') as f:
    width = 0
    height = 0
    for r, line in enumerate(f.readlines()):
        height = r
        for c, char in enumerate(line):
            width = len(line.strip())
            if char in '.ES':
                path.add((r, c))
            if char == 'S':
                start = (r, c)
            if char == 'E':
                end = (r, c)

def find_path(start, path):
    r, c = start
    Q = deque([(r, c, (0, 1), 0, 0)])
    visited = {}
    while Q:
        r, c, d, s1, s2 = Q.popleft()
        if (r, c) in visited and visited[(r, c)][1] < s2:
            continue
        visited[(r, c)] = [s1, s2]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c, new_d = r + dr, c + dc, (dr, dc)
            if (new_r, new_c) in path:
                Q.append((new_r, new_c, new_d, s1 + 1,  s2 + 1 if new_d == d else s2 + 1001))
    return visited


def get_best_paths(visited, end):
    r, c = end
    Q = deque([(r, c)])
    best = set()
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if (new_r, new_c) in visited:
                new = visited[(new_r, new_c)][1]
                cur = visited[(r, c)][1]
                if new < cur:
                    Q.append((new_r, new_c))
        best.add((r, c))
    return best

visited = find_path(start, path)
best = get_best_paths(visited, end)

for r in range(height + 1):
    for c in range(width + 1):
        if (r, c) in path:
            if (r, c) in best:
                print('O', end='')
            else:
                print('.', end='')
        else:
            print(' ', end='')
    print()

print(visited[end])