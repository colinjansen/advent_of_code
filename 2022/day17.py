with open('_input/day17.txt') as f:
    input = f.read()


wall = 7
input_length = len(input)
top = -1
input_p = 0
shape_p = 0
shapes = [
    [(0,0), (1,0), (2,0), (3,0)], # horizontal line
    [(0,1), (1,0), (1,1), (1,2), (2,1)], # plus shape
    [(0,0), (1,0), (2,0), (2,1), (2,2)], # L shape
    [(0,0), (0,1), (0,2), (0,3)], # vertical line
    [(0,0), (0,1), (1,1), (1,0)], # square
]

grid = {}

def draw_grid(s=None):
    g = [[' '] * wall for _ in range(get_highest_rock() + 6)]
    for p in grid:
        g[p[1]][p[0]] = '#'
    if s != None:
        for p in s.pos():
            g[p[1]][p[0]] = '-'
    for i in range(len(g)-1, -1, -1):
        line = ''.join(g[i])
        print(f'[{line}]')

def get_push():
    """
    get the direction to move the shape
    """
    global input_p
    c = input[input_p]
    input_p = (input_p + 1) % input_length
    return 1 if c == '>' else -1

def get_shape():
    """
    get the next shape to use
    """
    global shape_p
    s = [*shapes[shape_p]]
    shape_p = (shape_p + 1) % len(shapes)
    return Shape(s, 2, top + 4)

def check_collions(points: dict):
    for k in points.keys():
        if k[0] < 0 or k[0] >= wall or k in grid or k[1] < 0: return True
    return False

def add_shape_to_grid(points, t):
    global top 
    global grid
    top = max(top, t)
    grid.update(points)

class Shape:

    def __init__(self, points, x = 0, y = 0):
        self.points = points
        self.x = x
        self.y = y
        self.w = max(points, key=lambda x: x[0])[0] + 1
        self.h = max(points, key=lambda x: x[1])[1] + 1

    def __repr__(self) -> str:
        return f'{self.x} {self.y} {self.w} {self.h} {self.pos()}'

    def move(self, x_d, y_d):
        p_x = self.pos(x_d, 0)
        if check_collions(p_x) == False:
            self.x += x_d

        p_y = self.pos(0, y_d)
        if check_collions(p_y) == False:
            self.y += y_d
            return True
        
        p_f = self.pos(0, 0)
        add_shape_to_grid(p_f, self.y + self.h - 1)
        return False

    def pos(self, x=0, y=0):
        return {(p[0] + self.x + x, p[1] + self.y + y): 0 for p in self.points}

def get_top_at_iteration(i):                                                    
    for i in range(0, i):
        s = get_shape()
        if i % 100_000 == 0:
            print(f"\rcycle: {i}", end='')
        while s.move(get_push(), -1):
            pass
    print(f"\n{top + 1}")

#get_top_at_iteration(2022)
get_top_at_iteration(1_000_000_000_000)