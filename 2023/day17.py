import heapq

M = []
with open("_input/day17.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        M.append(list(line))


def get_positions(r, c, d, s, part_2):
    def check(nr, nc, nd, ns=1):
        # check bounding
        if nr < 0 or nr > len(M) - 1 or nc < 0 or nc > len(M[0]) - 1:
            return
        if part_2:
            # no lines longer than 10
            # no turns unless line is at least 4
            # allow the move if this is the first move
            if ns <= 10 and (nd == d or s >= 4 or s == 0):
                q.append((nr, nc, nd, ns))
        else:
            # no lines longer than three
            if ns <= 3:
                q.append((nr, nc, nd, ns))

    q = []
    if d == '':
        check(r, c - 1, 'L')
        check(r, c + 1, 'R')
        check(r + 1, c, 'D')
        check(r - 1, c, 'U')
    if d == 'R':
        check(r, c + 1, 'R', s + 1)
        check(r + 1, c, 'D')
        check(r - 1, c, 'U')
    if d == 'L':
        check(r, c - 1, 'L', s + 1)
        check(r + 1, c, 'D')
        check(r - 1, c, 'U')
    if d == 'U':
        check(r, c - 1, 'L')
        check(r, c + 1, 'R')
        check(r - 1, c, 'U', s + 1)
    if d == 'D':
        check(r, c - 1, 'L')
        check(r, c + 1, 'R')
        check(r + 1, c, 'D', s + 1)

    return q


def search(part_2=False):
    # start the queue at the lava pit
    Q = [(0, 0, 0, '', 0)]

    # memoize so that this doesn't take a long time
    MEM = {}
    while len(Q) > 0:
        h, r, c, d, s = heapq.heappop(Q)
        # memoize so we don't repeat paths
        if (r, c, d, s) in MEM:
            continue
        MEM[(r, c, d, s)] = h
        # get all the directions we could go
        for r, c, d, s in get_positions(r, c, d, s, part_2):
            heapq.heappush(Q, (h + int(M[r][c]), r, c, d, s))

    return min([v for k, v in MEM.items() if k[0] == len(M) - 1 and k[1] == len(M[0]) - 1])

# get the lowest value from a path that led to the factory
print('running part 1...')
print(search())

print('running part 2...')
print(search(True))
