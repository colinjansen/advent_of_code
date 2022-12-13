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

memo = [[0] * len(grid[0]) for _ in range(len(grid))]


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
    lines = len(grid)
    chars = len(grid[0])
    return p[0] >= 0 and p[0] < lines and p[1] >= 0 and p[1] < chars


visited = {}


def build_tree(start):
    tree = Node()
    tree.position = start
    tree.parent = None
    tree.steps = 0

    queue = [tree]

    while len(queue) > 0:
        n = queue.pop()

        # have we already been here?        
        if (memo[n.position[0]][n.position[1]] > 0):
            if (visited[n.position].steps > n.steps):
                visited[n.position].steps = n.steps
                visited[n.position].parent = n.parent
            continue

        u = (n.position[0] - 1, n.position[1])
        d = (n.position[0] + 1, n.position[1])
        l = (n.position[0], n.position[1] - 1)
        r = (n.position[0], n.position[1] + 1)

        if on_grid(l) and can_move(n.position, l):
            new = Node()
            new.position = l
            new.parent = n
            new.steps = n.steps + 1
            queue.append(new)
        if on_grid(r) and can_move(n.position, r):
            new = Node()
            new.position = r
            new.parent = n
            new.steps = n.steps + 1
            queue.append(new)
        if on_grid(u) and can_move(n.position, u):
            new = Node()
            new.position = u
            new.parent = n
            new.steps = n.steps + 1
            queue.append(new)
        if on_grid(d) and can_move(n.position, d):
            new = Node()
            new.position = d
            new.parent = n
            new.steps = n.steps + 1
            queue.append(new)

        visited[n.position] = n
        memo[n.position[0]][n.position[1]] = 2

    return tree


def get_path_steps(p: Node):
    steps = 0
    while p.parent != None:
        p = p.parent
        steps += 1
    return steps


start = get_position('S', 'a', grid)
end = get_position('E', 'z', grid)

tree = build_tree(start)
steps = get_path_steps(visited[end])

for m in memo:
    print(m)

print(steps)

#print(f'part 1 is {min(paths)} part 2 is {0}')
