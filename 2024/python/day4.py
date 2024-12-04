X_MOVES = [(-1, -1, -1, 1), (-1, 1, 1, 1), (1, -1, -1, -1), (1, 1, 1, -1)]
ALL_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

CROSSWORD = []
with open(f"2024/_input/day4.txt") as fp:
    for line in fp.readlines():
        CROSSWORD.append(line.strip())

def xmas_check(r, c):
    def xmas(x, y, r, c):
        for spread, ch in enumerate('XMAS'):
            r_ = r + (x * spread)
            c_ = c + (y * spread)
            if r_ < 0 or r_ >= len(CROSSWORD) or c_ < 0 or c_ >= len(CROSSWORD[0]):
                return 0
            if CROSSWORD[r_][c_] != ch:
                return 0
        return 1

    return sum([xmas(rd, cd, r, c) for rd, cd in ALL_MOVES])

def xmas_cross_check(r, c):
    def xmas(x1, y1, x2, y2, r, c):
        return CROSSWORD[r][c] == 'A' and CROSSWORD[r+x1][c+y1] == 'M' and CROSSWORD[r+x2][c+y2] == 'M' and CROSSWORD[r-x1][c-y1] == 'S' and CROSSWORD[r-x2][c-y2] == 'S'
    return sum([xmas(x1, y1, x2, y2, r, c) for x1, y1, x2, y2 in X_MOVES])

part1 = sum([xmas_check(r, c) for r in range(len(CROSSWORD)) for c in range(len(CROSSWORD[0]))])
part2 = sum([xmas_cross_check(r, c) for r in range(1, len(CROSSWORD)-1) for c in range(1, len(CROSSWORD[0])-1)])

print(part1, part2)