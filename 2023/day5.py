from functools import reduce
import re

def load():

    with open("_input/day5.txt", encoding='utf8') as f:
        lines = f.read().splitlines()

    seeds = list(map(lambda x: int(x), lines[0].split('seeds: ')[1].split(' ')))
    maps = {}
    load = ''
    for line in lines:
        if line == 'seed-to-soil map:':
            load = 0 #'seed-to-soil'
            maps[load] = []
            continue
        if line == 'soil-to-fertilizer map:':
            load = 1 #'soil-to-fertilizer'
            maps[load] = []
            continue
        if line == 'fertilizer-to-water map:':
            load = 2 #'fertilizer-to-water'
            maps[load] = []
            continue
        if line == 'water-to-light map:':
            load = 3 #'water-to-light'
            maps[load] = []
            continue
        if line == 'light-to-temperature map:':
            load = 4 #'light-to-temperature'
            maps[load] = []
            continue
        if line == 'temperature-to-humidity map:':
            load = 5 #'temperature-to-humidity'
            maps[load] = []
            continue
        if line == 'humidity-to-location map:':
            load = 6 #'humidity-to-location'
            maps[load] = []
            continue
        if load != '' and line != '':
            maps[load].append(list(map(lambda x: int(x), line.split(' '))))
    return seeds, maps

seeds, maps = load()

def map_value(seed, maps):
    for map in maps:
        if seed >= map[1] and seed <= map[1] + map[2]:
            return seed + (map[0] - map[1])
    return seed

def rev_map_value(seed, maps):
    for map in reversed(maps):
        if seed >= map[0] and seed <= map[0] + map[2]:
            return seed + (map[1] - map[0])
    return seed

def do_map(seed):
    m = seed
    for i in range(7):
        m = map_value(m, maps[i])
    return m

def in_seeds(seeds, n):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= n and n < seeds[i] + seeds[i+1]:
            return True
    return False

def part1(seeds):
    f = []
    for seed in seeds:
        f.append(do_map(seed))
    return min(f)
    

def rev_do_map(seeds, location):
    m = location
    for i in range(6, -1, -1):
        m = rev_map_value(m, maps[i])
    if in_seeds(seeds, m):
        return m
    return False

def part2(seeds, block=1000):
    n = 0
    while rev_do_map(seeds, n) == False:
        n += block
    low = n
    for i in range(n, n-block, -1):
        r = rev_do_map(seeds, i)
        if r != False and low > i:
            low = i
    return low

print(f'part1: {part1(seeds)} part2: {part2(seeds)}')
print('it wants part 2 to be one less')