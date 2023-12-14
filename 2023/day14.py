map = []
with open("_input/day14.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        map.append(list(line))

def north(M):
    moves = 1
    while moves > 0:
        moves = 0
        for i in range(1, len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 'O' and M[i-1][j] == '.':
                    M[i][j] = '.'
                    M[i-1][j] = 'O'
                    moves += 1
    return M

def south(M):
    moves = 1
    while moves > 0:
        moves = 0
        for i in range(len(M)-2, -1, -1):
            for j in range(len(M[i])):
                if M[i][j] == 'O' and M[i+1][j] == '.':
                    M[i][j] = '.'
                    M[i+1][j] = 'O'
                    moves += 1
    return M

def east(M):
    moves = 1
    while moves > 0:
        moves = 0
        for c in range(len(M[0])-2, -1, -1):
            for r in range(len(M)):
                if M[r][c] == 'O' and M[r][c+1] == '.':
                    M[r][c] = '.'
                    M[r][c+1] = 'O'
                    moves += 1
    return M

def west(M):
    moves = 1
    while moves > 0:
        moves = 0
        for c in range(1, len(M[0])):
            for r in range(len(M)):
                if M[r][c] == 'O' and M[r][c-1] == '.':
                    M[r][c] = '.'
                    M[r][c-1] = 'O'
                    moves += 1
    return M

def show(M):
    print()
    for line in M:
        print(''.join(line))
    print()

def calc(M):
    total = 0
    weight = 0
    for line in reversed(M):
        weight += 1
        for c in line:
            if c == 'O':
                total += weight
    return total

def copy(M):
    return [r.copy() for r in M]

def cycle(M):
    M = north(M)
    M = west(M)
    M = south(M)
    M = east(M)
    return M


print(calc(north(copy(map))))

def get_hash(M):
    return ''.join([''.join(r) for r in M])

def get_map(line, w):
    return [line[i:i+w] for i in range(0, len(line), w)]

def get_cycle_repeat(M, max = 1_000_000_000):
    MEM = {}
    for i in range(max):
        M = cycle(M)
        h = get_hash(M)
        if h in MEM:
            return MEM, h, i
        MEM[h] = i


mem, h, i = get_cycle_repeat(copy(map))
start = mem[h]
rep = i - mem[h]
D = start + (1_000_000_000-start) % rep
print(start, rep, i, D)

print(calc(get_map(list(mem)[D-1], len(map[0]))))
print(calc(get_map(list(mem)[D], len(map[0]))))
print(calc(get_map(list(mem)[D+1], len(map[0]))))