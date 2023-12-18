import re

with open("_input/day18.txt", encoding="utf8") as f:
    lines = f.read().splitlines()


def area(p):
    C = []
    P = 0
    X = 0
    Y = 0
    for line in lines:
        dr, di = p(line)
        di = int(di)
        if dr == 'U':
            X -= di
        if dr == 'D':
            X += di
        if dr == 'R':
            Y += di
        if dr == 'L':
            Y -= di
        P += di
        C.append((X, Y))
    return ss(C) + (P//2)+1


def p1(line):
    return re.match(r'([UDRL]) (\d+) \(#.*\)', line).groups()


def p2(line):
    _, _, g = re.match(r'([UDRL]) (\d+) \(#(.*)\)', line).groups()
    return 'RDLU'[int(g[5:])], int(g[:5], 16)


def ss(C):
    s1 = sum([C[i-1][0] * C[i][1] for i in range(1, len(C))])
    s2 = sum([C[i][0] * C[i-1][1] for i in range(1, len(C))])
    return abs(s1-s2) // 2


print(area(p1))
print(area(p2))