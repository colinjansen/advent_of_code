
def seat_row(id):
    row = 0
    for i in range(7):
        row += (2 ** (6 - i)) * (id[i] == 'B')
    return row

def seat_isle(id):
    isle = 0
    for i in range(3):
        isle += (2 ** (2 - i)) * (id[i] == 'R')
    return isle

def encode(row, isle):
    R = ''
    L = ''
    for i in range(7):
        R += 'B' if (2 ** (6 - i)) & row else 'F'
    for i in range(3):
        L += 'R' if (2 ** (2 - i)) & isle else 'L'
    return (R, L)

H = 0
M = {}
with open('day5.txt', 'r') as file:
    for line in file:
        R = seat_row(line[:7])
        I = seat_isle(line[7:])
        H = max(H, R * 8 + I)
        if R not in M:
            M[R] = ['.'] * 8
        M[R][I] = '#'

M = dict(sorted(M.items()))
min = min(M.keys())
max = max(M.keys())
for k, v in M.items():
    if k == min or k == max:
        continue
    if '.' in v:
        r, l = encode(k, v.index('.'))
        print(k * 8 + v.index('.'))