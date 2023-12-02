import re

with open("_input/day1.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

def trans(num):
    if num == 'one': return 1
    if num == 'two': return 2
    if num == 'three': return 3
    if num == 'four': return 4
    if num == 'five': return 5
    if num == 'six': return 6
    if num == 'seven': return 7
    if num == 'eight': return 8
    if num == 'nine': return 9
    if num.isnumeric():
        return num

t = 0
for line in lines:
    res = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    c = int(f'{trans(res[0])}{trans(res[-1])}')
    t += c
print(t)