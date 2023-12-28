import networkx as nx

def parse():
    M = []
    with open("_input/day23.txt", encoding='utf8') as f:
        for line in f.read().splitlines():
            M.append(list(line))
    return M

def show(M, N):
    for r, line in enumerate(M):
        for c, chr in enumerate(line):
            if (c, r) in N:
                print('*', end='')
            else:
                print(' ' if chr == '.' else chr, end='')
        print()
    
def part1():
    map = parse()
    start = (map[0].index('.'), 0)
    goal = (map[len(map)-1].index('.'), len(map)-1)
    return max([len(p) for p in get_paths(map, start, goal)])-1

def get_paths(M, S, G):


    def valid(fx, fy, dx, dy):
        if 0 > dx or dx >= len(M[0]) or 0 > dy or dy >= len(M):
            return False
        c = M[dy][dx]
        if c == '#':
            return False
        if dx - fx == 1 and c == '<':
            return False
        if dx - fx == -1 and c == '>':
            return False
        if dy - fy == 1 and c == '^':
            return False
        if dy - fy == -1 and c == 'v':
            return False
        return True
    
    Q = [(S[0], S[1], [])]
    P = []
    while Q:
        x, y, mem = Q.pop(0)
        mem.append((x, y))
        if (x, y) == G:
            P.append(mem)
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if valid(x, y, nx, ny) and (nx, ny) not in mem:
                Q.append((nx, ny, mem.copy()))
    return P
    
def map_to_graph(M, G):
    start = (M[0].index('.'), 0)
    goal = (M[len(M)-1].index('.'), len(M)-1)
    N = set()
    E = {}
    mem = set()


    def valid(dx, dy):
        if 0 > dx or dx >= len(M[0]) or 0 > dy or dy >= len(M):
            return False
        if M[dy][dx] == '#':
            return False
        return True
    

    def is_node(x, y):
        if x == start[0] and y == start[1]:
            return True
        if x == goal[0] and y == goal[1]:
            return True
        v = 0
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if valid(x + dx, y + dy):
                v += 1
        return v > 2


    Q = [(start[0], start[1], start[0], start[1], 0, [])]
    while Q:
        x, y, fx, fy, s, mem = Q.pop(0)
        mem.append((x, y))
        if is_node(x, y):
            if (fx, fy) in E and (x, y) in E[(fx, fy)]:
                continue
            if (x, y) not in N:
                N.add((x, y))
            if s > 0:
                if (fx, fy) not in E:
                    E[(fx, fy)] = {}
                if (x, y) not in E:
                    E[(x, y)] = {}

                E[(fx, fy)][(x, y)] = s
                E[(x, y)][(fx, fy)] = s
                G.add_edge((fx, fy), (x, y), length=s)
                G.add_edge((x, y), (fx, fy), length=s)
                fx = x
                fy = y
                s = 0
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and (nx, ny) not in mem:
                Q.append((nx, ny, fx, fy, s+1, mem.copy()))
    return G, E, start, goal


def get_paths_2(edges, s, goal):
    P = []
    Q = [(s, 0, [])]

    while Q:
        current_node, steps, path = Q.pop(0)
        path.append(current_node)
        if current_node == goal:
            P.append(steps)
            continue
        for node in edges[current_node].keys():
            if node not in path:
                Q.append((node, steps + edges[current_node][node], path.copy()))
    return P



M = parse()
G = nx.Graph()
G, e, s, g = map_to_graph(M, G)

best = 0
for path in nx.all_simple_paths(G, s, g):
    t = 0
    for i in range(1, len(path)):
        t += e[path[i-1]][path[i]]
    if t > best:
        best = t
print(best)
