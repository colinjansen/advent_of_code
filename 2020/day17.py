active_cubes = set()

with open('_input/day17.txt') as fp:
    r = 0
    for line in fp.readlines():
        for c, a in enumerate(line.strip()):
            if a == '#':
                active_cubes.add((c, r, 0, 0))
        r += 1

def active_neighbours(cube):
    x, y, z, w = cube
    return [(_x+x, _y+y, _z+z, _w+w) for _w in [-1, 0, 1] for _z in [-1, 0, 1] for _y in [-1, 0, 1] for _x in [-1, 0, 1] if (_x+x, _y+y, _z+z, _w+w) != (x, y, z, w) and (_x+x, _y+y, _z+z, _w+w) in active_cubes]

def inactive_neighbours(cube):
    x, y, z, w = cube
    return [(_x+x, _y+y, _z+z, _w+w) for _w in [-1, 0, 1] for _z in [-1, 0, 1] for _y in [-1, 0, 1] for _x in [-1, 0, 1] if (_x+x, _y+y, _z+z, _w+w) != (x, y, z, w) and (_x+x, _y+y, _z+z, _w+w) not in active_cubes]

for cycle in range(6):
    # adjacent inactive cubes
    inactive_cubes = set([inactive_cube for active_cube in active_cubes for inactive_cube in inactive_neighbours(active_cube)])

    deactivate = set()
    activate = set()
    for cube in active_cubes:
        an = len(active_neighbours(cube))
        if an < 2 or an > 3:
            deactivate.add(cube)
    for cube in inactive_cubes:
        an = len(active_neighbours(cube))
        if an == 3:
            activate.add(cube)
    for cube in deactivate:
        active_cubes.remove(cube)
    for cube in activate:
        active_cubes.add(cube)

    print('deactivate: ', len(deactivate))
    print('activate: ', len(activate))
    print('cycle ', cycle+1, 'active cubes: ', len(active_cubes))

