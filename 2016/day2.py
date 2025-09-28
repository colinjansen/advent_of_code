PART1 = [
    '123',
    '456',
    '789'
]
PART2 = [
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  '
]

def move(p, chars, PAD):
    for c in chars:
        if c == 'U' and (p[0] - 1) >= 0 and PAD[p[0]-1][p[1]] != ' ':
            p = (p[0]-1, p[1])
        if c == 'D' and (p[0] + 1) < len(PAD) and PAD[p[0]+1][p[1]] != ' ':
            p = (p[0]+1, p[1])
        if c == 'L' and (p[1] - 1) >= 0 and PAD[p[0]][p[1]-1] != ' ':
            p = (p[0], p[1]-1)
        if c == 'R' and (p[1] + 1) < len(PAD[0]) and PAD[p[0]][p[1]+1] != ' ':
            p = (p[0], p[1]+1)
    return p

def num(p, PAD):
    return 

def go_with_pad(pad, start):
    p = start
    b = ''
    with(open('2016/_input/day2.txt') as fp):
        for chars in fp.readlines():
            p = move(p, chars, pad);
            b += pad[p[0]][p[1]]
    return b

print('part 1 ', go_with_pad(PART1, (1, 1)))
print('part 1 ', go_with_pad(PART2, (2, 0)))
