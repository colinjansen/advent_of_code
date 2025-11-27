from collections import defaultdict

def get_joltages():
    A = set()
    with open('_input/day10.txt', 'r') as file:
        for line in file.readlines():
            A.add(int(line))
    A.add(0)
    A.add(max(A)+3)
    return sorted(A)

def part1():
    v = 0
    J = defaultdict(int)
    for a in get_joltages():
        J[a-v] += 1
        v = a
    return J[1] * J[3]

def part2():
    J = get_joltages()
    W = defaultdict(int)
    W[max(J)] = 1
    for i in range(len(J) - 2, -1, -1):
        j = J[i];
        W[j] += W[j + 1] if (j + 1) in J else 0
        W[j] += W[j + 2] if (j + 2) in J else 0
        W[j] += W[j + 3] if (j + 3) in J else 0
    return W[0]

print('part 1: ', part1())
print('part 2: ', part2())