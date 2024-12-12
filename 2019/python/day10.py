from collections import defaultdict
import math

map = []
map2 = []
with open(f'2019/_input/day10.txt') as f:
    for line in f.readlines():
        map.append(line.strip())
        map2.append(list(line.strip()))

def get_points(map, f):
    return [(x, y) for x, r in enumerate(map) for y, c in enumerate(r) if f(c)]


def slope_to_degrees(rise, run, angle_offset_from_east=90):
    return (math.degrees(math.atan2(rise, run)) + angle_offset_from_east) % 360
    
    
def get_asteroid_info(asteroid, asteroids):
    info = []
    
    for a in asteroids:
        if a == asteroid:
            continue
        dx, dy = a[0] - asteroid[0], a[1] - asteroid[1]
        gcd = math.gcd(dx, dy)
        info.append({
            'position': a, 
            'slope': (dx / gcd, dy / gcd),
            'angle': slope_to_degrees(dx, dy),
            'distance': abs(dx + dy)
        })
    return info

def dict_from_list(list_of_items:list, key:str):
    d = defaultdict(list)
    for item in list_of_items:
        d[item[key]].append(item)
    return d

asteroids = get_points(map, lambda c: c == '#')

part1 = (0, None)
for asteroid in asteroids:
    info = get_asteroid_info(asteroid, asteroids)
    slopes = dict_from_list(info, 'slope')
    if len(slopes) > part1[0]:
        part1 = (len(slopes), asteroid, info)

print('part 1', part1[0], part1[1])

A = part1[2]
angles = dict_from_list(A, 'angle')
angles = dict(sorted(angles.items()))

# sort asteroids by distance
for angle, asteroids in angles.items():
    angles[angle] = sorted(asteroids, key=lambda a: a['distance'])

i = 0
t = 200
while i < 200:
    if 0 == sum(len(asteroids) for asteroids in angles.values()):
        print('all out of asteroids')
        break
    for angle, asteroids in angles.items():
        if asteroids:
            a = asteroids.pop(0)
            i += 1
            if i == t:
                print('part 2', a['position'][1]*100+a['position'][0], a)
                break