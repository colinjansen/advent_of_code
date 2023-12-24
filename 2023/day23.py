
M = []
with open("_input/day23.txt", encoding='utf8') as f:
    for line in f.read().splitlines():
        M.append(list(line))

S = (M[0].index('.'), 0)
G = (M[len(M)-1].index('.'), len(M)-1)
MEM = set()


def valid(fx, fy, dx, dy):
    if 0 > dx or dx >= len(M[0]) or 0 > dy or dy >= len(M):
        return False
    c = M[dy][dx]
    if c == '#':
        return False
    # if dx - fx == 1 and c == '<':
    #     return False
    # if dx - fx == -1 and c == '>':
    #     return False
    # if dy - fy == 1 and c == '^':
    #     return False
    # if dy - fy == -1 and c == 'v':
    #     return False
    return True

def show(MEM):
    for r, line in enumerate(M):
        for c, chr in enumerate(line):
            if (c, r) in MEM and chr == '.':
                print(' ', end='')
            else:
                print(chr, end='')
        print()
    
t = 0
def get_paths():
    global t
    Q = [(S[0], S[1], [])]
    P = []
    while Q:
        x, y, mem = Q.pop(0)
        mem.append((x, y))

        if (x, y) == G:
            P.append(mem)
            t = max(t, len(mem))
            print('best is :', t)
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if valid(x, y, nx, ny) and (nx, ny) not in mem:
                Q.append((nx, ny, mem.copy()))
    return P

print(max([len(p) for p in get_paths()])-1)
