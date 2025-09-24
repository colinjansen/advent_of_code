REG = {
    'a': 1,
    'b': 0
}

COMMANDS = []
idx = 0

def run(idx):
    command = COMMANDS[idx]
    if command[0] == 'hlf':
        REG[command[1]] //= 2
        return idx + 1
    
    if command[0] == 'tpl':
        REG[command[1]] *= 3
        return idx + 1

    if command[0] == 'inc':
        REG[command[1]] += 1
        return idx + 1

    if command[0] == 'jmp':
        return idx + int(command[1])

    if command[0] == 'jie':
        if REG[command[1]] % 2 == 0:
            return idx + int(command[2])
        return idx + 1

    if command[0] == 'jio':
        if REG[command[1]] == 1:
            return idx + int(command[2])
        return idx + 1


with(open('2015/_input/day23.txt') as fp):
    COMMANDS = [line.replace(',', '').replace('+','').split() for line in fp.readlines()]

while idx >= 0 and idx < len(COMMANDS):
    idx = run(idx)

print(REG)