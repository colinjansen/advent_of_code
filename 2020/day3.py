with open('day3.txt', 'r') as f:
    map = list(map(lambda row: row.strip(), f.readlines())) 

def count_tree(r, c):
    R = 0
    C = 0
    T = 0
    while R < len(map):
        if map[R][C] == '#':
            T += 1
        R += r
        C += c
        if C >= len(map[0]):
            C %= len(map[0])
    return T

print(count_tree(1, 3))

T = 1
for r, c in [(1, 1),(1, 3),(1, 5),(1, 7),(2, 1)]:
    T *= count_tree(r, c)

print(T)