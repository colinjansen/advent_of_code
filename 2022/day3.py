with open("_input/day3.txt", encoding='utf8') as f:
    lines =  f.read().splitlines()

def getMatchingChar(a, b):
    for c in a:
        if (c in b):
            return c

def getOrdVal(c):
    v = ord(c)
    if (v >= 97):
        return v - 96
    else:
        return v - 38

def part1(lines):
    a = 0
    for line in lines:
        m = int(len(line)/2)
        c = getMatchingChar(line[:m], line[m:])
        a += getOrdVal(c)
    return a

def part2(lines):
    acc = 0
    for i in range(0, len(lines), 3):
        a = {}
        for c in lines[i]:
            if (c not in a):
                a[c] = 1
        for c in lines[i + 1]:
            if (c in a and a[c] == 1):
                a[c] = 2
        for c in lines[i + 2]:
            if (c in a and a[c] == 2):
                a[c] = 3
        for (k, v) in a.items():
            if (v == 3):
                acc += getOrdVal(k)
    return acc
        

print(f'part 1 is {part1(lines)}, part 2 is {part2(lines)}')