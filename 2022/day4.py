with open("_input/day4.txt", encoding='utf8') as f:
    lines =  f.read().splitlines()

def getRange(input):
    a, b = input.split('-')
    return list(range(int(a), int(b) + 1))

def getRanges(line):
    e, f = line.split(',')
    return (getRange(e), getRange(f))

def part1(lines):
    m = 0
    for line in lines:
        e, f = getRanges(line)
        if (e[0] >= f[0] and e[-1] <= f[-1]):
            m += 1
            continue
        if (f[0] >= e[0] and f[-1] <= e[-1]):
            m += 1
            continue
    return m
        
def part2(lines):
    m = 0
    for line in lines:
        e, f = getRanges(line)
        if (e[-1] >= f[0] and e[0] <= f[-1]):
            m += 1
            continue
    return m

print(f'part 1 is {part1(lines)}, part 2 is {part2(lines)}')