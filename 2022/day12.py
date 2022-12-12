with open("_input/day12.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

counter = 0

grid = []
for line in lines:
    grid.append(list(line))

memo = [ [0] * len(grid[0]) for _ in range(len(grid))]

def get_position(search: str, replace: str, lines: list[str]):
    for i in range(0, len(lines[0])):
        if search in lines[i]:
            p = lines[i].index(search)
            grid[i][p] = replace
            return (i, p)


def get_height(p):
    v = ord(grid[p[0]][p[1]])
    return v


def can_move(f, visited, t):
    if t in visited: return False
    vf = get_height(f)
    vt = get_height(t)
    d = vt - vf
    return True if d >= 0 and d <= 1 else False


def on_grid(p):
    return p[0] >= 0 and p[0] <= len(grid)-1 and p[1] >= 0 and p[1] <= len(grid[0])-1

def move(p, visited, moves=0):
    if len(visited) % 100 == 0: print(p)
    visited[p] = True

    if memo[p[0]][p[1]] == 0: memo[p[0]][p[1]] = moves
    if memo[p[0]][p[1]] > moves: memo[p[0]][p[1]] = moves
    if memo[p[0]][p[1]] < moves: return False


    if (p == end):
        paths.append(moves)
        return True
    u = (p[0] - 1, p[1])
    d = (p[0] + 1, p[1])
    l = (p[0], p[1] - 1)
    r = (p[0], p[1] + 1)
    if on_grid(l) and can_move(p, visited, l):
        move(l, {**visited}, moves + 1)
    if on_grid(r) and can_move(p, visited, r):
        move(r, {**visited}, moves + 1)
    if on_grid(u) and can_move(p, visited, u):
        move(u, {**visited}, moves + 1)
    if on_grid(d) and can_move(p, visited, d):
        move(d, {**visited}, moves + 1)
    return False

def print_memo():
    for m in memo:
        print(m)

paths = []
start = get_position('S', 'a', grid)
end = get_position('E', 'z', grid)

counter = 0
move(start, {})


print(f'part 1 is {min(paths)} part 2 is {0}')
