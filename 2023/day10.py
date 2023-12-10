with open("_input/day10.txt", encoding="utf8") as f:
    L = f.read().splitlines()
for i,_ in enumerate(L):
    L[i] = list(L[i])


def find_start(L):
    for i, r in enumerate(L):
        for j, c in enumerate(r):
            if c == "S":
                return (j, i)
            
VISITED = set()
def move_along_pipe(C):
    VISITED.add(C)
    c, r = C
    # go up
    if (c, r - 1) not in VISITED and r > 0 and L[r][c] in ['S','|','L','J'] and L[r - 1][c] in ['|','F','7']:
        return (c, r - 1)
    # go down
    if (c, r + 1) not in VISITED and r < len(L) and L[r][c] in ['S','|','F','7'] and L[r + 1][c] in ['|','L','J']:
        return (c, r + 1)
    # go right
    if (c + 1, r) not in VISITED and c < len(L[0]) and L[r][c] in ['S','-','F','L'] and L[r][c + 1] in ['-','7','J']:
        return (c+1, r )
    # go left
    if (c - 1, r) not in VISITED and c > 0 and L[r][c] in ['S','-','J','7'] and L[r][c - 1] in ['-','F','L']:
        return (c-1, r)
    return False

S = find_start(L)
v = S
while v is not False:
    v = move_along_pipe(v)
part_1 = len(VISITED)//2
print(part_1)

def count(r, c):
    t = 0
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        if (c, r) in VISITED:
            if L[r][c] in ['L','7']:
                t += 2
            else:
                t += 1
    return t

move_along_pipe = 0
for r, R in enumerate(L):
    for c, C in enumerate(R):
        if (c, r) in VISITED:
            continue
        if 1 == count(r, c) % 2:
            move_along_pipe += 1

print(move_along_pipe)