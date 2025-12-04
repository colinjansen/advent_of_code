
def parse():
    M = []
    with open('_input/day4.txt') as f:
        for line in f.readlines():
            M.append(list(line.strip()))
    return M

def adjacent_rolls(M, r, c):
    adjacent = 0
    for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1, 1)]:
        _r = r + dr
        _c = c + dc
        if _r < 0 or _c < 0 or _r >= len(M) or _c >= len(M[0]):
            continue
        if M[_r][_c] == '@':
            adjacent += 1
    return adjacent

def can_remove(M, r, c):
    return  M[r][c] == '@' and adjacent_rolls(M, r, c) < 4

def part_1(M):
    part_1 = 0
    for r in range(len(M)):
        for c in range(len(M[0])):
            if can_remove(M, r, c):
                part_1 += 1
    return part_1

def part_2(M):
    part_2 = 0

    def turn():
        removed = 0
        for r in range(len(M)):
            for c in range(len(M[0])):
                if can_remove(M, r, c):
                    M[r][c] = '.'
                    removed += 1
        return removed
    
    r = turn()
    while r > 0:
        part_2 += r
        r = turn()
    
    return part_2

print('part 1: ', part_1(parse()))
print('part 2: ', part_2(parse()))