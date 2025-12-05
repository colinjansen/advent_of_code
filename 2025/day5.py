
def parse():
    ranges = []
    ids = []
    add_range = True
    with open('_input/day5.txt') as f:
        for line in f.readlines():
            if line.strip() == '':
                add_range = False
                continue
            if add_range:
                ranges.append([int(x) for x in line.strip().split('-')])
            else:
                ids.append(int(line.strip()))
    return ranges, ids

def is_fresh(id, ranges):
    for r in ranges:
        if r[0] <= id <= r[1]:
            return True
    return False

def part1(ranges, ids):
    fresh = 0
    for id in ids:
        if is_fresh(id, ranges):
            fresh += 1
    return fresh

def part2(ranges):
    condensed = []
    for r in sorted(ranges):
        if not condensed or r[0] > condensed[-1][1] + 1:
            condensed.append(r)
        else:
            condensed[-1][1] = max(condensed[-1][1], r[1])
    return sum([c[1] - c[0] + 1 for c in condensed])


ranges, ids = parse()

print('part 1: ', part1(ranges, ids))
print('part 2: ', part2(ranges))