with open('2019/_input/day5.txt') as fp:
    CODES = fp.readline().split(',')
    CODES = [int(c) for c in CODES]


def get_opcode(code):
    return code[-2:]

def get_param(code, n):
    if n > len(code) - 2:
        return 0
    return code[-(n+2)]

def go(in1, in2, CODES):
    P = 0
    CODES[1] = in1
    CODES[2] = in2

    while CODES[P] != 99:
        op = get_opcode(CODES[P])
        p1 = CODES[P+1]
        p2 = CODES[P+2]
        p3 = CODES[P+3]
        if CODES[P] == 1:
            CODES[p3] = CODES[p1] + CODES[p2]
            P += 4
        if CODES[P] == 2:
            CODES[p3] = CODES[p1] * CODES[p2]
            P += 4
        if CODES[P] == 3:
            CODES[p3] = CODES[p1] * CODES[p2]
            P += 2
        if CODES[P] == 4:
            CODES[p3] = CODES[p1] * CODES[p2]
            P += 2
    return CODES[0]

# print(go(12, 2, CODES[:]))

# for i in range(100):
#     for j in range(100):
#         if 19690720 == go(i, j, CODES[:]):
#             print(100 * i + j)
