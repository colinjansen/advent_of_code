with open("_input/day14.txt", encoding='utf8') as f:
    input = f.read().splitlines()


class Line():
    def __init__(self):
        self.positions = []


class BoundingBox:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def __str__(self):
        return f'TRBL: {self.top} {self.right} {self.bottom} {self.left}'

    def width(self):
        return self.right - self.left + 1

    def height(self):
        return self.bottom - self.top + 1


def get_lines(lines: list[str]) -> list[Line]:
    """
    parse the lines into usable pairs grouped into lines
    """
    rock_lines = []
    for line in lines:
        l = Line()
        for pair in line.split(' -> '):
            p = pair.split(',')
            l.positions.append((int(p[0]), int(p[1])))
        rock_lines.append(l)
    return rock_lines


def get_bounding_box(cave: set) -> BoundingBox:
    """
    Get the maximum boundaries from all of the paris in all
    of the lines. we can use this to draw a grid
    """
    bbox = BoundingBox()
    for p in cave:
        if bbox.right == None or p[0] > bbox.right:
            bbox.right = p[0]
        if bbox.left == None or p[0] < bbox.left:
            bbox.left = p[0]
        if bbox.bottom == None or p[1] > bbox.bottom:
            bbox.bottom = p[1]
        if bbox.top == None or p[1] < bbox.top:
            bbox.top = p[1]
    return bbox


def expand_line(a: tuple, b: tuple) -> list[tuple]:
    """
    expand the line into its individual coordinate positions
    """
    x_i = b[0] - a[0]
    y_i = b[1] - a[1]
    if x_i != 0:
        x_i //= abs(x_i)
    if y_i != 0:
        y_i //= abs(y_i)
    c = a
    line = [c]
    while c != b:
        c = (c[0] + x_i, c[1] + y_i)
        line.append(c)
    return line


def get_starting_rocks(lines: list[Line]) -> set:
    """
    push all the lines into a set of coordinates
    """
    spaces: set = {}
    for line in lines:
        for i in range(1, len(line.positions)):
            for c in expand_line(line.positions[i-1], line.positions[i]):
                spaces[c] = '#'
    return spaces


def draw_cave(cave: set) -> None:
    """
    draw a representation of the cave
    """
    bbox = get_bounding_box(cave)
    grid = []
    for i in range(bbox.height()):
        grid.append([])
        for j in range(bbox.width()):
            grid[i].append([])
            grid[i][j] = '.'

    x_offset = 0 - bbox.left
    y_offset = 0 - bbox.top
    for p in cave:
        x = p[0] + x_offset
        y = p[1] + y_offset
        grid[y][x] = cave[p]
    for g in grid:
        print(''.join(g))


def can_move(cave: set, bbox: BoundingBox, s: tuple) -> tuple | bool:
    """
    can the sand move
    implementation for part 1 with the void
    return False for 'out of bounds'
    return None for 'can not move'
    otherwise return the new coordinate
    """
    # have we moved outside of the bbox?
    if s[0] < bbox.left or s[0] > bbox.right or s[1] > bbox.bottom:
        return False
    # fall straight down
    d = (s[0], s[1] + 1)
    if d not in cave:
        return d
    # down and left?
    dl = (s[0] - 1, s[1] + 1)
    if dl not in cave:
        return dl
    # down and right
    dr = (s[0] + 1, s[1] + 1)
    if dr not in cave:
        return dr
    # we can no longer move
    return True


def add_sand(cave: set, bbox: BoundingBox) -> bool:
    """
    add sand to the cave and see where it lands
    implementation for part 1 with a bounding box to check if the 
    sand falls into the void
    """
    s = (500, 0)
    move = can_move(cave, bbox, s)
    while (type(move) != bool):
        s = move
        move = can_move(cave, bbox, s)
    # no more sand can fit
    if move == False:
        return False
    # we can't move anymore
    if move == True:
        cave[s] = '*'
        return True


def can_move_v2(cave: set, floor: int, s: tuple) -> tuple | bool:
    """
    can the sand move
    implementation for part 2 with the infinite floor
    return False for 'out of bounds'
    return None for 'can not move'
    otherwise return the new coordinate
    """
    # we are blocked
    if s in cave:
        return False
    # we are on the floor
    if s[1] + 1 == floor:
        return True
    # fall straight down
    d = (s[0], s[1] + 1)
    if d not in cave:
        return d
    # down and left?
    dl = (s[0] - 1, s[1] + 1)
    if dl not in cave:
        return dl
    # down and right
    dr = (s[0] + 1, s[1] + 1)
    if dr not in cave:
        return dr
    # we can no longer move
    return True


def add_sand_v2(cave: set, floor: int) -> bool:
    """
    add sand to the cave and see where it lands
    implementation for part 2 with an infinite floor plane
    """
    s = (500, 0)
    move = can_move_v2(cave, floor, s)
    while (type(move) != bool):
        s = move
        move = can_move_v2(cave, floor, s)
    # no more sand can fit
    if move == False:
        return False
    # we can't move anymore
    if move == True:
        cave[s] = '*'
        return True


def part1() -> int:
    lines = get_lines(input)
    cave = get_starting_rocks(lines)
    bbox = get_bounding_box(cave)
    c = 0
    while add_sand(cave, bbox) == True:
        c += 1
    # draw_cave(cave)
    return c


def part2() -> int:
    lines = get_lines(input)
    cave = get_starting_rocks(lines)
    bbox = get_bounding_box(cave)
    c = 0
    while add_sand_v2(cave, bbox.bottom + 2) == True:
        c += 1
    # draw_cave(cave)
    return c


print(f'part 1 is {part1()} part 2 is {part2()}')
