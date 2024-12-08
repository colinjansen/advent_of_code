from datetime import datetime
from itertools import permutations

with open('2019/_input/day7.txt') as fp:
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

def go(input):
    P = 0
    input_p = 0
    while CODES[P] != 99:
        code = CODES[P]
        op = get_opcode(CODES[P])
        if op < 0 or op > 8:
            print('NOOO', op)
            return
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
            CODES[CODES[P+1]] = input[input_p]
            input_p += 1
            P += 2
        if op == 4:
            return CODES[CODES[P+1]]
            P += 2
        if op == 5:
            v1 = get_param(code, 1, P, CODES)
            v2 = get_param(code, 2, P, CODES)
            if v1 != 0:
                P = v2
            else:
                P += 3
        if op == 6:
            v1 = get_param(code, 1, P, CODES)
            v2 = get_param(code, 2, P, CODES)
            if v1 == 0:
                P = v2
            else:
                P += 3
        if op == 7:
            v1 = get_param(code, 1, P, CODES) 
            v2 = get_param(code, 2, P, CODES)
            set_param(1 if v1 < v2 else 0, P+3, CODES)
            P += 4
        if op == 8:
            v1 = get_param(code, 1, P, CODES) 
            v2 = get_param(code, 2, P, CODES)
            set_param(1 if v1 == v2 else 0, P+3, CODES)
            P += 4
    return 

def test_phase(phases):
    output = 0
    for i in phases:
        output = go([i, output])
    return output


m = 0
t = datetime.now()
for phases in permutations([0,1,2,3,4]):
    m = max(m, test_phase(phases))
print('elapsed:', datetime.now() - t, m)