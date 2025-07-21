
with open('2024/_input/day25.txt') as f:
    lines = f.read()
    things = lines.split('\n\n')
locks = set()
keys = set()
for thing in things:
    thing = thing.split('\n')
    if thing[0] == '#####' and thing[-1] == '.....':
        l = []
        for c in range(5):
            l.append(sum([1 for r in range(5) if thing[r+1][c] == '#']))
        locks.add(tuple(l))
    if thing[0] == '.....' and thing[-1] == '#####':
        l = []
        for c in range(5):
            l.append(sum([1 for r in range(5) if thing[r+1][c] == '#']))
        keys.add(tuple(l))

def fit(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return False
    return True

part1 = 0
for lock in locks:
    for key in keys:
        if fit(lock, key):
            part1 += 1
print(part1)