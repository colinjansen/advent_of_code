
def get_map():
    map = set()
    keys = {}
    doors = {}
    with open('2019/_input/day18.txt') as f:
        for r, line in enumerate(f.read().splitlines()):
            for c, char in enumerate(line):
                # lowercase keys
                if ord(char) >= 97 and ord(char) <= 122:
                    keys[char] = (r, c)
                # uppercase doors
                if ord(char) >= 65 and ord(char) <= 90:
                    doors[char.lower()] = (r, c)
                # everything is part of the path
                if char not in '#':
                    map.add((r, c))

    return map, keys, doors

map, keys, doors = get_map()

