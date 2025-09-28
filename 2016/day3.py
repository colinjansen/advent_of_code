def viable(t):
    return (t[0]+t[1])>t[2] and (t[1]+t[2])>t[0] and (t[2]+t[0])>t[1]

def part1(lines):
    return [list(map(int, line.split())) for line in lines]

def part2(lines):
    b = []
    for i in range(0, len(lines), 3):
        lines[i] = lines[i].split()
        lines[i+1] = lines[i+1].split()
        lines[i+2] = lines[i+2].split()
        b.append((int(lines[i][0]), int(lines[i+1][0]), int(lines[i+2][0])))
        b.append((int(lines[i][1]), int(lines[i+1][1]), int(lines[i+2][1])))
        b.append((int(lines[i][2]), int(lines[i+1][2]), int(lines[i+2][2])))
    return b
with(open('2016/_input/day3.txt') as fp):
    lines = fp.readlines()
    part1 = sum([1 for t in part1(lines) if viable(t)])
    part2 = sum([1 for t in part2(lines) if viable(t)])
    print(part1, part2)