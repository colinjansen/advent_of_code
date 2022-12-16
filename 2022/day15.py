import re
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union

with open("_input/day15.txt", encoding='utf8') as f:
    input = f.read().splitlines()


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_intersecting_segment(beacon: tuple, sensor: tuple, line: int) -> tuple | bool:
    d = manhattan_distance(sensor, beacon)
    d2 = d - abs(sensor[1] - line)
    return False if d2 < 0 else (sensor[0] - d2, sensor[0] + d2)


def get_intersecting_segments(beacons: list[tuple], sensors: list[tuple], line: int) -> list[tuple]:
    segments = []
    for i in range(0, len(sensors)):
        s = get_intersecting_segment(beacons[i], sensors[i], line)
        if s == False:
            continue
        segments.append(s)
    return segments


def combine_segments(segments: list[tuple]) -> list[tuple]:
    result = []
    for segment in sorted(segments):
        result = result or [segment]
        if segment[0] > result[-1][1]:
            result.append(segment)
        else:
            old = result[-1]
            result[-1] = (old[0], max(old[1], segment[1]))
    return result


def sum_segment_lengths(segments: list[tuple]) -> int:
    length = 0
    for segment in segments:
        length += abs(segment[1] - segment[0])
    return length


def part1(beacons, sensors, line=2000000):
    segments = get_intersecting_segments(beacons, sensors, line)
    segments = combine_segments(segments)
    return sum_segment_lengths(segments)


def get_poly(beacon, sensor):
    d = manhattan_distance(sensor, beacon)
    x = sensor[0]
    y = sensor[1]
    return Polygon([(x + d, y), (x, y-d), (x-d, y), (x, y+d), (x+d, y)])


def get_polygons(beacons, sensors):
    polys = []
    for i in range(0, len(sensors)):
        polys.append(get_poly(beacons[i], sensors[i]))
    return polys


def part2(beacons, sensors):
    polygons = get_polygons(beacons, sensors)
    u = unary_union(polygons)
    for u in u.interiors:
        point: Point = u.centroid
        return int((point.x * 4000000) + point.y)


beacons = []
sensors = []

for line in input:
    m = re.match(
        'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    g = m.groups()
    sensors.append((int(g[0]), int(g[1])))
    beacons.append((int(g[2]), int(g[3])))


p1 = part1(beacons, sensors)
p2 = part2(beacons, sensors)

print(p1, p2)
