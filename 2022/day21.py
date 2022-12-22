import re

with open('_input/day21.txt') as f:
    lines = f.read().splitlines()


def solve(op: str, n1: int, n2: int):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 // n2


def part1(lines, debug=False):

    numbers = {}
    operations = {}

    for line in lines:
        match = re.match('(\w+): (\d+)', line)
        if match:
            # add to our known numbers
            g = match.groups()
            numbers[g[0]] = int(g[1])
            continue
        match = re.match('(\w+): (\w+) (.) (\w+)', line)
        if match:
            # add to operations
            g = match.groups()
            operations[g[0]] = (g[1], g[2], g[3])
            continue
        assert False, 'we should not be here - parsing numbers has failed'

    while operations:
        debug and print(f'we know {len(numbers)} numbers')
        debug and print(f'running through {len(operations)} operations')
        delete_me = []
        for key in operations:
            if operations[key][0] in numbers and operations[key][2] in numbers:
                numbers[key] = solve(
                    operations[key][1], numbers[operations[key][0]], numbers[operations[key][2]])
                delete_me.append(key)
        for key in delete_me:
            del operations[key]

    return numbers['root']


def part1_v2(lines, debug=False):

    numbers = {}
    operations = {}

    def r_solve(key):
        # memoized numbers
        if key in numbers:
            return numbers[key]
        op = operations[key]
        if op[1] == '+':
            r = r_solve(op[0]) + r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '-':
            r = r_solve(op[0]) - r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '*':
            r = r_solve(op[0]) * r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '/':
            r = r_solve(op[0]) // r_solve(op[2])
            numbers[key] = r
            return r
        assert False, 'we should not be here... something is terribly wrong'

    for line in lines:
        match = re.match('(\w+): (\d+)', line)
        if match:
            # add to our known numbers
            g = match.groups()
            numbers[g[0]] = int(g[1])
            continue
        match = re.match('(\w+): (\w+) (.) (\w+)', line)
        if match:
            # add to operations
            g = match.groups()
            operations[g[0]] = (g[1], g[2], g[3])
            continue
        assert False, 'we should not be here - parsing numbers has failed'

    return r_solve('root')


def part2(lines, debug=False):

    numbers = {}
    operations = {}
    r1 = ''
    r2 = ''

    for line in lines:
        match = re.match('(\w+): (\d+)', line)
        if match:
            # add to our known numbers
            g = match.groups()
            if g[0] == 'humn':
                humn = int(g[1])
                continue
            numbers[g[0]] = int(g[1])
            continue
        match = re.match('(\w+): (\w+) (.) (\w+)', line)
        if match:
            # add to operations
            g = match.groups()
            if g[0] == 'root':
                r1 = g[1]
                r2 = g[3]
                continue
            operations[g[0]] = (g[1], g[2], g[3])
            continue
        assert False, 'we should not be here - parsing numbers has failed'

    original = numbers.copy()

    def r_solve(key):
        # memoized numbers
        if key in numbers:
            return numbers[key]
        op = operations[key]
        if op[1] == '+':
            r = r_solve(op[0]) + r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '-':
            r = r_solve(op[0]) - r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '*':
            r = r_solve(op[0]) * r_solve(op[2])
            numbers[key] = r
            return r
        if op[1] == '/':
            r = r_solve(op[0]) // r_solve(op[2])
            numbers[key] = r
            return r
        assert False, 'we should not be here... something is terribly wrong'

    r2s = r_solve(r2)

    ld = 1
    hd = 1
    r = 0
    while r <= 0:
        ld = hd
        hd *= 10
        numbers = original.copy()
        numbers['humn'] = hd
        r = r2s - r_solve(r1)

    while r != 0:
        numbers = original.copy()
        m = ld + ((hd - ld) // 2)
        numbers['humn'] = m
        r = r2s - r_solve(r1)
        if r < 0:
            ld = m
        else:
            hd = m

    a = numbers['humn']
    answers = []
    # i found that it could be a few numbers
    for i in range(a - 3, a + 4):
        numbers = original.copy()
        numbers['humn'] = i
        r = r2s - r_solve(r1)
        if (r == 0):
            answers.append(i)

    #3243420789721

    return answers


#print(f'part1 is: {part1(lines)}')
print(f'part1_v2 is: {part1_v2(lines)}')
print(f'part2 is: {part2(lines)}')
