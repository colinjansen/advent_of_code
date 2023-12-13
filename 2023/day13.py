def h_check(map, i, j):
    while i > 0 and j < len(map)-1:
        i -= 1
        j += 1
        if map[i] != map[j]:
            return False
    return True

def v_check(map, i, j):
    while i > 0 and j < len(map[0])-1:
        i -= 1
        j += 1
        if v_line(map, i) != v_line(map, j):
            return False
    return True

def v_line(map, n):
    return ''.join([map[i][n] for i in range(len(map))])

def calc(map, old=-1):
    for i in range(1, len(map)):
        if map[i] == map[i-1]:
            if h_check(map, i, i - 1):
                if i * 100 != old:
                    return i * 100
            
    for i in range(1, len(map[0])):
        if v_line(map, i) == v_line(map, i-1):
            if v_check(map, i, i - 1):
                if i != old:
                    return i
    return -1

def find_alt(map, old):
    for r in range(len(map)):
        for c in range(len(map[0])):
            map[r][c] = '.' if map[r][c] == '#' else '#'
            a = calc(map, old)
            if a != -1 and a != old:
                return a
            map[r][c] = '.' if map[r][c] == '#' else '#'
    return -1

maps = []
map = []
with open("_input/day13.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        if line.strip() == '':
            maps.append(map.copy())
            map.clear()
        else:
            map.append(list(line))
    if len(map) > 0:
        maps.append(map.copy())
        map.clear()

t1 = 0
t2 = 0
for map in maps:
    a = calc(map)
    b = find_alt(map, a)
    t1 += a
    t2 += b
print(t1, t2)