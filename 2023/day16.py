with open("_input/day16.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

M = [list(l) for l in lines]

def move(r):
    
    c = M[r[0]][r[1]]

    if r[2] == 'R':
        if c == '/':
            return [(r[0]-1, r[1], 'U')]
        if c == '\\':
            return [(r[0]+1, r[1], 'D')]
        if c == '|':
            return [(r[0]+1, r[1], 'D'), (r[0]-1, r[1], 'U')]
        return [(r[0], r[1]+1, r[2])]
    if r[2] == 'L':
        if c == '/':
            return [(r[0]+1, r[1], 'D')]
        if c == '\\':
            return [(r[0]-1, r[1], 'U')]
        if c == '|':
            return [(r[0]+1, r[1], 'D'), (r[0]-1, r[1], 'U')]
        return [(r[0], r[1]-1, r[2])]
    if r[2] == 'D':
        if c == '/':
            return [(r[0], r[1]-1, 'L')]
        if c == '\\':
            return [(r[0], r[1]+1, 'R')]
        if c == '-':
            return [(r[0], r[1]+1, 'R'), (r[0], r[1]-1, 'L')]
        return [(r[0]+1, r[1], r[2])]
    if r[2] == 'U':
        if c == '/':
            return [(r[0], r[1]+1, 'R')]
        if c == '\\':
            return [(r[0], r[1]-1, 'L')]
        if c == '-':
            return [(r[0], r[1]+1, 'R'), (r[0], r[1]-1, 'L')]
        return [(r[0]-1, r[1], r[2])]

def oob(r,c):
    return r < 0 or c < 0 or r >= len(M) or c >= len(M[0])

def show(V):
    print('')
    print(f'showing variation with {len(V)} energized tiles')
    print('')
    S = []
    for line in M:
        S.append(line.copy())
    for v in V.keys():
        S[v[0]][v[1]] = str(len(V[v]))
    for l in S:
        print(''.join(l))

def been_here(m, V):
    if (m[0], m[1]) not in V:
        return False
    if m[2] not in V[(m[0], m[1])]:
        return False
    return True

def energize(r):
    V = {}
    R = [r]
    V[(r[0],r[1])] = [r[2]]
    while len(R) > 0:
        r = R.pop(0)
        for m in move(r):
            if not been_here(m, V) and not oob(m[0], m[1]):
                R.append(m)
        
                if (m[0], m[1]) not in V:
                    V[(m[0], m[1])] = []
                V[(m[0], m[1])].append(m[2])
                
    return len(V)

print('calculating the single point of entry')
print('part 1: ', energize((0,0,'R')))

best = 0
max_c = len(M[0])-1
max_r = len(M)-1
print('calculating left and right edges...')
for r in range(len(M)):
    best = max(best, energize((r, 0, 'R')), energize((r, max_c, 'L')))
print('calculating top and bottom edges...')
for c in range(len(M[0])):
    best = max(best, energize((0, c, 'D')), energize((max_r, c, 'U')))
print('part 2: ', best)