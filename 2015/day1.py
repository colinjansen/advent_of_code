with open("_input/day1.txt", encoding='utf8') as f:
    line = f.read()

floor = 0
idx = 0
for i, c in enumerate(line):
    if c == '(': floor += 1
    if c == ')': floor -= 1
    if idx == 0 and floor == -1: idx = i + 1

print(floor, idx)