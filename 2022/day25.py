


with open('_input/day25.txt') as f:
    input = f.read().splitlines()

def from_snafu(s: str) -> int:    
    SNAFU = {}
    SNAFU['2'] = 2
    SNAFU['1'] = 1
    SNAFU['0'] = 0
    SNAFU['-'] = -1
    SNAFU['='] = -2
    c = 0
    for i in range(len(s)):
        place = len(s) - i - 1
        v = 5**place * SNAFU[s[i]]
        c += v
    return c

def to_snafu(n: int) -> int:
    SNAFU = {}
    SNAFU[2] = '2'
    SNAFU[1] = '1'
    SNAFU[0] = '0'
    SNAFU[-1] = '-'
    SNAFU[-2] = '='
    def get_snafu(n: int, place: int) -> str:
        possibles = {}
        best_index = -2
        for i in range(-2, 3):
            val = 5**place * i
            dif = val - n
            possibles[i] = (i, val, dif)
            if abs(possibles[best_index][2]) > abs(dif):
                best_index = i
        return possibles[best_index]

    def get_snafu_chars(nums:list[int]) -> str:
        s = ''
        for n in nums:
            s += SNAFU[n]
        return s

    place = 0
    s = []
    while n > 2 * 5**place:
        place += 1
    while place >= 0:
        c = get_snafu(n, place)
        place -= 1
        s.append(c[0])
        n -= c[1]
    return get_snafu_chars(s)

def part1(lines):
    t = 0
    for line in lines:
        n = from_snafu(line)
        t +=n
    return to_snafu(t)


print(part1(input))