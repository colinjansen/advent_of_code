mapping = { 'A': 0, 'B': -1, 'C': 1, 'X': 1, 'Y': 2, 'Z': 3 }
with open("_input/day2.txt", encoding='utf8') as f:
    lines =  f.read().splitlines()
    input = map(lambda s: s.split(' '), lines)
sets = map(lambda x: (mapping[x[0]], mapping[x[1]]), input)
p1 = 0
p2 = 0
for a, x in sets:
    p1 += x + (3 * (x + a) % 9)
    p2 += ((x - a + 1) % 3) + 1 + (3 * (x - 1))
print(f'part 1 is {p1}, part 2 is {p2}')