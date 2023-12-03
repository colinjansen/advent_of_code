from functools import reduce

with open("_input/day3.txt", encoding='utf8') as f:
    lines = f.read().splitlines()
    
# convenient constants
max_x = len(lines[0]) - 1
max_y = len(lines) - 1


def spin(coord, callback):
    """
    spin the wheel
    """
    x, y = coord
    for r in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1 ,1)]:
        _x = x + r[0]
        _y = y + r[1]
        if (_x < 0 or _x > max_x) or (_y < 0 or _y > max_y):
            continue
        callback(_x, _y)


def find_all_numbers(coordinates_to_search):
    """
    Find all numbers in the map and return them with their coordinates
    """
    numbers = []
    visited = []
    for x, y in coordinates_to_search:
        c = lines[y][x]
        if c.isdigit() and (x, y) not in visited:
            coords = [(x, y)]
            visited.append((x, y))
            buffer = c
            offset = 1
            while x+offset <= max_x and lines[y][x+offset].isdigit():
                visited.append((x+offset, y))
                coords.append((x+offset, y))
                buffer += lines[y][x+offset]
                offset += 1
            offset = -1
            while x+offset >= 0 and lines[y][x+offset].isdigit():
                visited.append((x+offset, y))
                coords.append((x+offset, y))
                buffer = lines[y][x+offset] + buffer
                offset -= 1
            numbers.append((int(buffer), coords))
            continue
    return numbers


def find_adjacent_numbers(gears, numbers):
    """
    find numbers that are adjacent to the gears
    """
    result = []
    def add_adjacent_number(_x, _y):
        n = get_number(numbers, _x, _y)
        if n and n not in adjacent_numbers:
            adjacent_numbers.append(n)
    for x, y in gears:
        adjacent_numbers = []
        spin((x, y), lambda x, y: add_adjacent_number(x, y))
        result.append(adjacent_numbers)
    return result
    

def get_number(numbers, x, y):
    """
    find number with matching coordinates
    """
    for i, e in enumerate(numbers):
        k = e[0]
        v = e[1]
        if (x, y) in v:
            return (i, k)
    return None



queue = []
gears = []
# get all spaces adjacent to a symbol and mark where the 'gears' are
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if (ord(c) < 48 and ord(c) != 46) or ord(c) > 57:
            # found symbol
            queue.append((x, y))
            # take a special note for the gears
            if c == '*':
                gears.append((x, y))
            spin((x, y), lambda x, y: queue.append((x, y)))

# find all numbers
numbers = find_all_numbers(queue)

part1 = reduce(lambda x, y: x + y[0], numbers, 0)

# find the numbers adjacent to a gear
adjacent = find_adjacent_numbers(gears, numbers)

part2 = reduce(lambda x, y: x + (y[0][1] * y[1][1] if len(y) == 2 else 0), adjacent, 0)

print(part1, part2)