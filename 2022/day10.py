with open("_input/day10.txt", encoding='utf8') as f:
  lines = f.read().splitlines()

def parse_commands(lines):
  register = 1
  cycles = [register]
  for command in lines:
    if command.startswith('noop'):
      cycles.append(register)
      continue
    if command.startswith('addx '):
      cycles.append(register)
      register += int(command.split('addx ')[1])
      cycles.append(register)
      continue
  return cycles
  
cycles = parse_commands(lines)
part1 = 0
for i in [20, 60, 100, 140, 180, 220]:
  part1 += i * cycles[i - 1]
  
mask = [0, 1, 2]
buffer = ''
for i in range(0, len(cycles)):
  mask = [cycles[i] - 1, cycles[i], cycles[i] + 1]
  buffer += '#' if i % 40 in mask else '.'

print(f'part 1 is {part1}')

print('part 2 is')
for line in [buffer[i:i + 40] for i in range(0, len(buffer), 40)]:
  print(line)