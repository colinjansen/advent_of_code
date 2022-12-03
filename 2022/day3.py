mapping = { 'A': 0, 'B': -1, 'C': 1, 'X': 1, 'Y': 2, 'Z': 3 }

with open("_input/day2.txt", encoding='utf8') as f:
    lines =  f.read().splitlines()

p1 = 0
p2 = 0

for line in lines:
    l1, l2 = line.split(' ')
    a = mapping[l1]
    x = mapping[l2]
    p1 += x + (3 * (x + a) % 9)
    p2 += ((x - a + 1) % 3) + 1 + (3 * (x - 1))

print(f'part 1 is {p1}, part 2 is {p2}')