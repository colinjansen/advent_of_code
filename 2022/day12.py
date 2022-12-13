with open("_input/day12.txt.test", encoding='utf8') as f:
    lines = f.read().splitlines()

counter = 0

class Node:
    def __init__(self):
        self.position = (0, 0)
        self.moves = 0
        self.parent = None
        self.children = []
    def __str__(self):
        buf = f'{self.x} {self.y} {self.moves}\n'
        for c in self.children:
            buf += str(c)
        return buf

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


def can_move(f, t):
    vf = get_height(f)
    vt = get_height(t)
    d = vt - vf
    return True if d >= 0 and d <= 1 else False


def on_grid(p):
    return p[0] >= 0 and p[0] <= len(grid)-1 and p[1] >= 0 and p[1] <= len(grid[0])-1


def build_tree(node: Node, visited, moves=0):

    if (node.position in visited):
        if (visited[l].moves > moves):
            visited[l].moves = moves
            visited[l].parent = node
        return

    if on_grid(node.position) == False: return
    if can_move(p, r) == False: return

    visited[node.position] = node

    u = (p[0] - 1, p[1])
    d = (p[0] + 1, p[1])
    l = (p[0], p[1] - 1)
    r = (p[0], p[1] + 1)

    if on_grid(l) and can_move(p, l):
        else:
            n = build_tree(l, visited, moves+1)
            n.parent = node
            node.children.append(n)

    if :
        if (r in visited):
            if (visited[r].moves > moves):
                visited[r].moves = moves
                visited[r].parent = node
        else:
            n = build_tree(r, visited, moves+1)
            n.parent = node
            node.children.append(n)

    if on_grid(u) and can_move(p, u):
        if (u in visited):
            if (visited[u].moves > moves):
                visited[u].moves = moves
                visited[u].parent = node
        else:
            n = build_tree(u, visited, moves+1)
            n.parent = node
            node.children.append(n)

    if on_grid(d) and can_move(p, d):
        if (d in visited):
            if (visited[d].moves > moves):
                visited[d].moves = moves
                visited[d].parent = node
        else:
            n = build_tree(d, visited, moves+1)
            n.parent = node
            node.children.append(n)

    return node


def move(p, visited, moves=0):
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


def get_path_steps(p:Node):
    steps = 0
    while p.parent != None:
        p = p.parent
        steps += 1
    return steps

paths = []
start = get_position('S', 'a', grid)
end = get_position('E', 'z', grid)

visited = {}
tree = Node()
tree.position = start
tree = build_tree(start, visited)
steps = get_path_steps(visited[end])
print(f'{steps}')

#print(f'part 1 is {min(paths)} part 2 is {0}')
