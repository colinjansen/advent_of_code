import re
from collections import Counter

def do_thing(s:str):
    b = ''
    for n in Counter(sorted(re.sub('[^a-z]', '', s))).most_common(5):
        b += n[0]
    return b

def real(l):
    m = re.match('(.*)-(\d+)\[(.*)\]', l)
    g = m.groups()
    return int(g[1]), g[0], do_thing(g[0]) == g[2]

def decrypt(n, v):
    b = ''
    for c in n:
        if c == '-':
            b += ' '
        else:
            b += chr(((ord(c) - 97 + v) % 26) + 97)
    return b

with(open('_input/day4.txt') as fp):
    part1 = 0
    for l in fp.readlines():
        id, n, v = real(l)
        if v:
            part1 += id
            d = decrypt(n, id)
            if 'northpole' in d:
                print(d, id)
    print('part 1: ', part1)
