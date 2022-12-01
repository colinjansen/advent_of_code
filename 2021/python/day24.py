from itertools import product

with open('_input/day24.txt', encoding='utf8') as f:
    lines = [l.strip() for l in f.readlines()]

constants = []
for i in range(0, len(lines), 18):
    c1 = int(lines[i+5].split()[-1])
    c2 = int(lines[i+15].split()[-1])
    constants.append((c1, c2))

def solve(prod):
    for digits in prod:
        digits = iter(digits)
        pin = [0 if c[0] < 9 else next(digits) for c in constants]
        #print(f"\r{''.join([str(x) for x in pin])}", end='')
        z = 0
        for i,w in enumerate(pin):
            c1,c2 = constants[i]
            if c1 > 9:
                z = z * 26 + w + c2
            else:
                pin[i] = (z%26) + c1
                if not (0 < pin[i] < 10):
                    break
                z = z//26
        if z == 0:
            if 0 not in pin:
                return ''.join([str(x) for x in pin])

print(f"\rpart 1: {solve(product(range(9,0,-1), repeat=7))}")
print(f"\rpart 2: {solve(product(range(0, 10), repeat=7))}")