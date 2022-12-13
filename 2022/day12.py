with open("_input/day12.txt", encoding='utf8') as f:
    lines = f.read().splitlines()



class Node:
    def __init__(self):
        self.position = (0, 0)
        self.moves = 0
        self.parent = None
        self.elevation = None


visited = {}


grid = []
for line in lines:
    grid.append(list(line))


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
    return True if d >= -1 else False


def on_grid(p):
    lines = len(grid)
    chars = len(grid[0])
    return p[0] >= 0 and p[0] < lines and p[1] >= 0 and p[1] < chars


def try_add_to_queue(queue, p, n):
    if on_grid(p) == False: return
    if can_move(n.position, p) == False: return
    node = Node()
    node.position = p
    node.parent = n
    node.steps = n.steps + 1
    node.elevation = grid[node.position[0]][node.position[1]]
    queue.append(node)


def build_tree(start):
    tree = Node()
    tree.position = start
    tree.parent = None
    tree.steps = 0
    tree.elevation = grid[tree.position[0]][tree.position[1]]

    queue = [tree]

    while len(queue) > 0:
        node = queue.pop()

        # have we already been here?        
        if (node.position in visited):
            if (visited[node.position].steps <= node.steps):
                continue
            if (visited[node.position].steps > node.steps):
                visited[node.position].steps = node.steps
                visited[node.position].parent = node.parent

        visited[node.position] = node

        try_add_to_queue(queue, (node.position[0] - 1, node.position[1]), node)
        try_add_to_queue(queue, (node.position[0] + 1, node.position[1]), node)
        try_add_to_queue(queue, (node.position[0], node.position[1] - 1), node)
        try_add_to_queue(queue, (node.position[0], node.position[1] + 1), node)


    return tree


def get_path_steps(p: Node):
    steps = 0
    while p.parent != None:
        p = p.parent
        steps += 1
    return steps


start = get_position('S', 'a', grid)
end = get_position('E', 'z', grid)


tree = build_tree(end)

part1 = get_path_steps(visited[start])

part2 = 987654321

for v in visited:
    if (visited[v].elevation == 'a'):
        steps = get_path_steps(visited[v])
        if (steps < part2): part2 = steps

print(f'part 1 is: {part1} and part 2 is {part2}')
