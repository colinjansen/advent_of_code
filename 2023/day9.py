from functools import reduce

def get_to_zero(source):
    entries = [source]
    while not all(i == 0 for i in source):
        source = [source[i] - source[i - 1] for i in range(1, len(source))]
        entries.append(source)
    return entries

def extrapolate(line):
    entries = get_to_zero([int(x) for x in line.split()])
    indexes = [i for i in range(len(entries) - 2, -1, -1)]
    accumulator_1 = reduce(lambda a, i: entries[i][-1] + a, indexes, 0)
    accumulator_2 = reduce(lambda a, i: entries[i][0] - a, indexes, 0)
    return accumulator_1, accumulator_2

with open("_input/day9.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

total_1 = sum([extrapolate(line)[0] for line in lines])
total_2 = sum([extrapolate(line)[1] for line in lines])
    
print(f'part 1: {total_1} part 2: {total_2}')