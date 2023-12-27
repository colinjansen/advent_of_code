PL = {}
M = []
S = None

with open("_input/day21.txt", encoding='utf8') as f:
    for r, line in enumerate(f.read().splitlines()):
        M.append(list(line))
        if 'S' in line:
            S = (r, line.index('S'))
def show(s):
    for r, l in enumerate(M):
        for c, ch in enumerate(l):
            if (r,c) in PL and PL[(r,c)]:
                print('O', end='')
            else:
                print(ch, end='')
        print()
    print(f'after {steps} steps')
    print()

PL[S] = True


def take_step(fr):
    res = []
    for p in fr:
        PL[p] = True
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            np = (p[0]+d[0], p[1]+d[1])
            if np not in PL and np not in res and 0 <= np[0] <= len(M)-1 and 0 <= np[1] <= len(M[0])-1 and M[np[0]][np[1]] == '.':
                res.append(np)
    return res

st = [S]
for steps in range(64+1):
    for p in PL:
        PL[p] = not PL[p]
    st = take_step(st)
    print(f'step: {steps + 1} {len(st)} {sum([1 for p in PL if PL[p]])}')
    #show(steps)