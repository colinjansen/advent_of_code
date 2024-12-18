import multiprocessing

P = []
with open('2024/_input/day18.txt') as f:
    for line in f.readlines():
        x, y = line.strip().split(',')
        P.append((int(x), int(y)))

start = (0, 0)
end = (70, 70)

def bfs(start, end, blocks):
    x, y = start
    queue = [(x, y, 0)]
    visited = {}
    while queue:
        x, y, c = queue.pop(0)
        if (x, y) == end:
            return c
        if (x, y) in visited and visited[(x, y)] <= c:
            continue
        visited[(x, y)] = c
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n = (x + dx, y + dy)
            if n in blocks:
                continue
            if 0 <= n[0] <= 70 and 0 <= n[1] <= 70:
                queue.append((n[0], n[1], c+1))
    return False

b = 2915
print(P[b-1], bfs(start, end, P[:b]))