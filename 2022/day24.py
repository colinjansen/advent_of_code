import math

with open('_input/day24.txt') as f:
    lines = f.read().splitlines()

def storm_permutations(lines: list[str]) -> dict:
        
    def parse_storm_information(lines):
        storms = []
        h = len(lines)
        w = len(lines[0])
        for y in range(h):
            for x in range(w):
                if lines[y][x] == 'v':
                    storms.append((y, x, 1, 0))
                if lines[y][x] == '>':
                    storms.append((y, x, 0, 1))
                if lines[y][x] == '<':
                    storms.append((y, x, 0, -1))
                if lines[y][x] == '^':
                    storms.append((y, x, -1, 0))
        return storms, h, w

    def move_storms(storms: list[tuple], h: int, w: int) -> list[tuple]:
        new_positions = []
        for storm in storms:
            y = storm[0] + storm[2]
            x =  storm[1] + storm[3]
            if y == 0: y = h - 2
            if x == 0: x = w - 2
            if y == h - 1: y = 1
            if x == w - 1: x = 1
            new_positions.append((y, x, storm[2], storm[3]))
        return new_positions

    def hash_storms(storms:list[tuple]) -> int:
        y = 0
        x = 0
        for storm in storms:
            y += storm[0] + (storm[0] + storm[2])
            x += storm[1] + (storm[1] + storm[3])
        return x*y

    def get_all_storm_permutations(lines: list[str]) -> dict:
        positions = {}
        storms, h, w = parse_storm_information(lines)
        hash = hash_storms(storms)
        while hash not in positions:
            positions[hash] = storms
            storms = move_storms(storms, h, w)
            hash = hash_storms(storms)
        return positions

    return get_all_storm_permutations(lines)

def part1(lines):
    print('getting storm permutations')
    perms = storm_permutations(lines)
    print(f'found {len(perms)} variations')
    for p in perms:
        print(f'{perms[p]}')

part1(lines)