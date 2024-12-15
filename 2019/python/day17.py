from computer import Computer

with open('2019/_input/day17.txt') as f:
    program = f.readline().strip()

def handle_input():
    return 0

buffer = ''
def handle_output(v):
    global buffer
    buffer += chr(v)
    return

c = Computer(program)
c.go(input_function=handle_input, output_function=handle_output)

def on_map(map, r, c):
    return 0 <= r < len(map) and 0 <= c < len(map[0])

def is_intersection(map, r, c):
    if map[r][c] != '#':
        return False
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        if not on_map(map, r+dr, c+dc):
            return False
        if map[r+dr][c+dc] != '#':
            return False
    return True

map = []
for line in buffer.strip().split('\n'):
    map.append(list(line))

part1 = 0
for r, row in enumerate(map):
    for c, char in enumerate(row):
        if is_intersection(map, r, c):
            part1 += r * c
print(part1)
# for line in map:
#     print(''.join(line))