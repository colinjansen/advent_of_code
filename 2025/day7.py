from collections import defaultdict


def parse():
    start = -1
    splitters = {}
    with open("_input/day7.txt") as f:
        for idx, line in enumerate(f.readlines()):
            if 'S' in line:
                start = line.index('S')
            splitters[idx] = []
            for i, c in enumerate(line):
                if c == '^':
                    splitters[idx].append(i)
    return start, splitters

def part1():
    start, splitters = parse()
    beams = set([start])
    count = 0

    for row in splitters.values():
        new_beams = set()

        for beam in beams:
            if beam in row:
                count += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)

        beams = new_beams

    return count

def part2():
    start, splitters = parse()
    beams = defaultdict(int)
    beams[start] = 1

    for row in splitters.values():
        for splitter in row:
            if beams[splitter] > 0:
                beams[splitter - 1] += beams[splitter]
                beams[splitter + 1] += beams[splitter]
                beams[splitter] = 0
    return sum(beams.values())

print(part1())
print(part2())