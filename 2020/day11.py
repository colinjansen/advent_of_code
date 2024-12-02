def get_seats():
    M = []
    with open('day11.txt', 'r') as fp:
        for row in fp.readlines():
            M.append(list(row.strip()))
    return M

def get_moves(M, r, c, d=1):
    return [(r+Ri, c+Ci) for Ri, Ci in [(0, d), (0, -d), (d, 0), (-d, 0), (d, d), (-d, -d), (d, -d), (-d, d)] if r+Ri >= 0 and r+Ri < len(M) and c+Ci >= 0 and c+Ci < len(M[0]) ]

def adjacent_occupied(M, r, c):
    return len([(Ri, Ci) for Ri, Ci in get_moves(M, r, c) if M[Ri][Ci] == '#'])

def insight_occupied(M, r, c, d=1):
    oc = 0
    for Rd, Cd in [(0, d), (0, -d), (d, 0), (-d, 0), (d, d), (-d, -d), (d, -d), (-d, d)]:
        ri = r+Rd
        ci = c+Cd
        while ci >= 0 and ci < len(M[0]) and ri >= 0 and ri < len(M):
            if M[ri][ci] == 'L':
                break
            if M[ri][ci] == '#':
                oc += 1
                break
            ri += Rd
            ci += Cd
    return oc

def update(M, f, threshold=4):
    updates = []
    for r in range(len(M)):
        for c in range(len(M[r])):
            if M[r][c] == 'L':
                if 0 == f(M, r, c):
                    updates.append((r, c, '#'))
                    continue
            if M[r][c] == '#':
                if threshold <= f(M, r, c):
                    updates.append((r, c, 'L'))
                    continue
    return updates

def apply(M, updates):
    for r, c, s in updates:
        M[r][c] = s

def part(search, threshold):
    M = get_seats()
    u = update(M, search, threshold)
    while len(u) > 0:
        # for r in M:
        #     print(''.join(r))
        # print()
        apply(M, u)
        u = update(M, search, threshold)

    return sum([1 for r in M for c in r if c == '#'])

print(part(adjacent_occupied, 4))
print(part(insight_occupied, 5))