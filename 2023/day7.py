import functools

with open("_input/day7.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

C = len(lines)
H = []
B = []
five = []
four = []
full = []
three = []
twopair = []
pair = []
high = []

for line in lines:
    l = line.split(' ')
    H.append(l[0])
    B.append(l[1])

def card_val(c, with_jokers=False) -> int:
    if c == 'A': return 14
    if c == 'K': return 13
    if c == 'Q': return 12
    if c == 'J': return 1 if with_jokers else 11
    if c == 'J': return 1
    if c == 'T': return 10
    return int(c)

def step_1_sort(h, b, with_jokers=False):
    s = {}
    J = 0
    _three = []
    _two = []
    for i in range(len(h)):
        if with_jokers and h[i] == 'J':
            J += 1
            continue
        if h[i] in s:
            s[h[i]] += 1
        else:
            s[h[i]] = 1
    for k in s.keys():
        if s[k] == 5:
            return five.append((h, b))
        if s[k] == 4:
            if with_jokers and J == 1:
                return five.append((h, b))
            return four.append((h, b))
        if s[k] == 3:
            _three.append(k)
        if s[k] == 2:
            _two.append(k)

    if len(_three) == 1 and len(_two) == 1:
        return full.append((h, b))
    
    if len(_three) == 1:
        if with_jokers:
            if J == 2:
                return five.append((h, b))
            if J == 1:
                return four.append((h, b))
        return three.append((h, b))
    
    if len(_two) == 2:
        if with_jokers:
            if J == 1:
                return full.append((h, b))
        return twopair.append((h, b))
    
    if len(_two) == 1:
        if with_jokers:
            if J == 3:
                return five.append((h, b))
            if J == 2:
                return four.append((h, b))
            if J == 1:
                return three.append((h, b))
        return pair.append((h, b))
    
    if with_jokers:
        if J == 4 or J == 5:
            return five.append((h, b))
        if J == 3:
            return four.append((h, b))
        if J == 2:
            return three.append((h, b))
        if J == 1:
            return pair.append((h, b))
    return high.append((h, b))

def get_value(with_jokers=False):
    for i in range(len(H)):
        step_1_sort(H[i], int(B[i]), with_jokers)

    t = 0
    def step_2_sort(a, b):
        h1 = a[0]
        h2 = b[0]
        for i in range(5):
            if card_val(h1[i], with_jokers) > card_val(h2[i], with_jokers):
                return 1
            if card_val(h1[i], with_jokers) < card_val(h2[i], with_jokers):
                return -1
        return 0

    rank = 0
    t = 0
    for e in sorted(high, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(pair, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(twopair, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(three, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(full, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(four, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]
    for e in sorted(five, key=functools.cmp_to_key(step_2_sort)):
        rank += 1
        t += rank * e[1]

    return t

print(f'part 1: {get_value()} part 2: {get_value(True)}')