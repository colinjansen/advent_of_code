from collections import deque
from functools import lru_cache

class KeyPad:

    def __init__(self, keypad=[]):
        self.positions = {}
        self.chars = {}
        for r, line in enumerate(keypad):
            for c, char in enumerate(line):
                if char != ' ':
                    self.positions[(r, c)] = char
                    self.chars[char] = (r, c)

@lru_cache(None)
def find_all_paths(keypad: KeyPad, key_from: str, key_to: str):
    """
    find all possible paths from key_from to key_to

    Args:
        key_from (str): The starting key
        key_to (str): The ending key

    Returns:
        list: A list of all possible paths from key_from to key_to
    """
    r, c = keypad.chars[key_from]
    Q = deque([(r, c, [])])
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
            if (r + dr, c + dc) in keypad.positions:
                Q.append((r + dr, c + dc, [*p, d]))

    return [ ''.join(v)+'A' for v in V[keypad.chars[key_to]] ]

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

KEYPAD = KeyPad(["789","456","123"," 0A"])
CONTROLS = KeyPad([" ^A", "<v>"])

CODES = [
    '539A',
    '964A',
    '803A',
    '149A',
    '789A'
]

@lru_cache(None)
def min_cost_for_move(a:str, b:str, keys:KeyPad, depth:int):
    """
    Returns the minimum cost of moving from a to b on the given keypad
    
    Args:
        a (str): The starting character
        b (str): The ending character
        keys (KeyPad): The keypad to use
        depth (int): The recursion depth
    
    Returns:
        int: The minimum cost of moving from a to b
    """
    if depth == 0: return min(len(p) for p in find_all_paths(CONTROLS, a, b))
    best = float('inf')
    for path in find_all_paths(keys, a, b):
        path = 'A' + path
        best = min(best, sum(min_cost_for_move(path[i], path[i+1], CONTROLS, depth - 1) for i in range(len(path) - 1)))
    return best

def min_cost_for_code(code, depth):
    """
    Returns the minimum cost of moving through a code
    
    Args:
        code (str): The code to move through
        depth (int): The recursion depth
        
    Returns:
        int: The minimum cost of moving through the code
    """
    return sum(min_cost_for_move(code[i], code[i+1], KEYPAD, depth) for i in range(len(code) - 1))
    
def get_costs_for_depth(depth):
    """
    Returns the sum of the minimum costs for all codes
    
    Args:
        depth (int): The recursion depth

    Returns:
        int: The sum of the minimum costs for all codes
    """
    return sum(min_cost_for_code('A' + code, depth) * int(code[0:-1]) for code in CODES)


print('part 1:', get_costs_for_depth(2))
print('part 2:', get_costs_for_depth(25))
