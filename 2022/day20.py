with open('_input/day20.txt') as f:
    lines = f.read().splitlines()

items = []
for i in range(0, len(lines)):
    items.append((i, 811589153 * int(lines[i])))


def find_index(l: list[tuple], s: int) -> int:
    for i in range(0, len(l)):
        if l[i][0] == s: return i
    return None

def find_value(l: list[tuple], s: int) -> int:
    for i in range(0, len(l)):
        if l[i][1] == s: return i
    return None

for _ in range(10):
    for i in range(0, len(items)):
        idx = find_index(items, i)
        assert items[idx] != None, "t can not be None"
        element = items.pop(idx)
        to = ((idx + element[1]) % len(items))
        if to == 0: to = len(items)
        items.insert(to, element)

idx = find_value(items, 0)
i1 = items[(idx + 1000) % len(items)][1]
i2 = items[(idx + 2000) % len(items)][1]
i3 = items[(idx + 3000) % len(items)][1]
print(sum([i1, i2, i3]))
