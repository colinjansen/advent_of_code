from computer import Computer
from collections import defaultdict, deque

with open('2019/_input/day15.txt') as f:
    program = f.readline().strip()

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

FAIL = 0
OK = 1
DONE = 2

def go_left(d):
    if d == NORTH:
        return WEST
    if d == EAST:
        return NORTH
    if d == SOUTH:
        return EAST
    if d == WEST:
        return SOUTH
    
def go_right(d):
    if d == NORTH:
        return EAST
    if d == EAST:
        return SOUTH
    if d == SOUTH:
        return WEST
    if d == WEST:
        return NORTH
    
def get_map():
    D = NORTH
    P = (0, 0)
    on_wall = False
    walls = set()
    sensor = None

    def handle_input():
        if not on_wall:
            return NORTH
        return D
    
    def get_p(P, D):
        if D == NORTH:
            return (P[0], P[1] - 1)
        if D == SOUTH:
            return (P[0], P[1] + 1)
        if D == WEST:
            return (P[0] - 1, P[1])
        if D == EAST:
            return (P[0] + 1, P[1])
    
    def handle_output(v):
        nonlocal D, P, on_wall, sensor

        new_P = get_p(P,D)

        if new_P == (0, 0):
            c.halted = True
            return
        
        if v == FAIL:
            on_wall = True
            walls.add(new_P)
            D = go_right(D)
        if v == OK or v == DONE:
            if v == DONE:
                sensor = new_P
            P = new_P
            D = go_left(D) if on_wall else D
        
    c = Computer(program)
    c.go(input_function=handle_input, output_function=handle_output)

    return walls, sensor

def show_map(walls, path, sensor):
    min_x = min([x for x, y in walls])
    max_x = max([x for x, y in walls])
    min_y = min([y for x, y in walls])
    max_y = max([y for x, y in walls])

    s = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) == (0,0):
                s += 'S'
            elif (x,y) == sensor:
                s += 'O'
            elif (x,y) in walls:
                s += '.'
            elif (x,y) in path:
                s += 'x'
            else:
                s += ' '
        s += '\n'
    return s

def find_shortest_path(start, walls, target=None):
    def get_neighbours(p):
        return [(p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0] + 1, p[1])]
    
    def bfs(start, target, walls):
        Q = deque([(start, 0)])
        visited = defaultdict(int)
        while Q:
            position, steps = Q.popleft()
            if target and position == target:
                visited[position] = steps
                return visited
            if position in visited:
                visited[position] = min(visited[position], steps)
                continue
            visited[position] = steps
            for n in get_neighbours(position):
                if n not in walls:
                    Q.append((n, steps + 1))
        return visited

    return bfs(start, target, walls)

walls, sensor = get_map()
path = find_shortest_path((0,0), walls, sensor)
fill = find_shortest_path(sensor, walls)
print(show_map(walls, path, sensor))

print('part 1:', path[sensor])
print('part 2:', max(fill.values()))