from collections import deque
from functools import cache
from itertools import product

"""
KEYPAD
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
CONTROLS
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
KEYPAD = ["789","456","123"," 0A"]
CONTROLS = [" ^A", "<v>"]
CODES = [
    '539A',
    '964A',
    '803A',
    '149A',
    '789A'
]

class KeyPad:
    cache = {}

    def __init__(self, keypad=[]):
        self.keypad = {}
        self.chars = {}
        for r, line in enumerate(keypad):
            for c, char in enumerate(line):
                if char != ' ':
                    self.keypad[(r, c)] = char
                    self.chars[char] = (r, c)

    def find_all_paths(self, key_from, key_to):
        key = tuple([key_from, key_to])
        if key in self.cache:
            return self.cache[key]
        r, c = self.chars[key_from]
        Q = deque([(r, c, '')])
        V = {}
        while Q:
            r, c, p = Q.popleft()
            if (r, c) in V:
                if len(V[(r, c)][0]) < len(p):
                    continue
                if len(V[(r, c)][0]) > len(p):
                    V[(r, c)] = [p]
                V[(r, c)].append(p)
            else:
                V[(r, c)] = [p]
            for dr, dc, d in [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]:
                if (r + dr, c + dc) in self.keypad:
                    Q.append((r + dr, c + dc, p+d))
        self.cache[key] = V[self.chars[key_to]]
        return self.cache[key]

    def get_sequences(self, code):
        last = 'A'
        parts = []
        for c in code:
            paths = [s+'A' for s in self.find_all_paths(last, c)]
            parts.append(paths)
        prod = ["".join(x) for x in product(*parts)]
        return prod
    

keypad = KeyPad(KEYPAD)
controls = KeyPad(CONTROLS)

def get_min_sequence_length(code):
    s1 = keypad.get_sequences(code)
    print(s1)
    s2 = []
    s3 = []
    for s in s1:
        s2.extend(controls.get_sequences(s))
    for s in s2:
        s3.extend(controls.get_sequences(s))
    m = min([len(s) for s in s3])
    return m

part1 = 0
for code in CODES:
    m = get_min_sequence_length(code)
    c = int(code[0:-1])
    print(code, m, c)
    part1 += m*c

print(part1)