from shapely.geometry import Polygon, box

def parse():
    coords = []
    with open("_input/day9.txt") as f:
        for line in f.readlines():
            coords.append(tuple([int(x) for x in line.strip().split(",")]))
    return coords


def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

def inside(a, b, shape):
    minx = min(a[0], b[0])
    maxx = max(a[0], b[0])
    miny = min(a[1], b[1])
    maxy = max(a[1], b[1])

    rect = box(minx, miny, maxx, maxy)

    return shape.covers(rect)

def part1(coords, check=None):
    shape = Polygon(coords)
    max_area = 0
    max_points = None
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            if check and not check(coords[i], coords[j], shape):
                continue
            a = area(coords[i], coords[j])
            if a > max_area:
                max_points = [coords[i], coords[j]]
                max_area = a
    return max_area, max_points

coords = parse()
m1, p = part1(coords)
m2, p = part1(coords, inside)
print('part 1: ', m1)
print('part 2: ', m2)