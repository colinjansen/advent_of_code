with open('2019/_input/day5.txt') as fp:
    CODES = fp.readline().split(',')
    CODES = [int(c) for c in CODES]

def get_opcode(code):
    return int(str(code)[-2:])

def get_mode(code, n):
    code = str(code)
    if n > len(code) - 2:
        return 0
    return int(code[-(n+2)])

def get_param(code, n, p, CODES):
    mode = get_mode(code, n)
    if mode == 0:
        return CODES[CODES[p+n]]
    else:
        return CODES[p+n]
    
def set_param(val, p, CODES):
    CODES[CODES[p]] = val
    
def go(CODES):
    P = 0
    while CODES[P] != 99:
        code = CODES[P]
        op = get_opcode(CODES[P])
        if op == 1:
            v1 = get_param(code, 1, P, CODES) 
            v2 = get_param(code, 2, P, CODES)
            set_param(v1+v2, P+3, CODES)
            P += 4
        if op == 2:
            v1 = get_param(code, 1, P, CODES) 
            v2 = get_param(code, 2, P, CODES)
            set_param(v1*v2, P+3, CODES)
            P += 4
        if op == 3:
            CODES[CODES[P+1]] = 1 
            P += 2
        if op == 4:
            print(CODES[CODES[P+1]])
            P += 2
    return 


# for i in range(100):
#     for j in range(100):
#         if 19690720 == go(i, j, CODES[:]):
#             print(100 * i + j)
