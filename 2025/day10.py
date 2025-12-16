from collections import deque
import re
from z3 import Int, Sum, Optimize, sat

def parse():
    machines = []
    with open("_input/day10.txt") as f:
        for line in f.readlines():
            matches = re.match(r"\[(.+)\] (.+) {(.+)}", line)

            light_target = matches[1].replace("#", "1").replace(".", "0")
            light_target = tuple([int(l) for l in light_target])

            buttons = [b.strip("()") for b in matches[2].split(" ")]
            buttons = [[int(pos) for pos in b.split(",")] for b in buttons]

            joltage_target = tuple([int(j) for j in matches[3].split(",")])

            machines.append(tuple([light_target, buttons, joltage_target]))
    return machines

def bfs_lights(start, target, buttons):

    visited = {start}
    Q = deque([(start, 0)])

    while Q:
        state, m = Q.popleft()

        if state == target:
            return m

        for button in buttons:

            # generate a new 'state' by flipping some buttons
            new_state = list(state)
            for pos in button:
                new_state[pos] = 1 - new_state[pos]
            new_state = tuple(new_state)

            # make sure e haven't seen this before
            if new_state not in visited:
                visited.add(new_state)
                Q.append([new_state, m + 1])
    return -1

def bfs_joltage(start, target, buttons):

    def valid(state, target):
        for i, v in enumerate(state):
            if v > target[i]:
                return False
        return True

    visited = {start}
    Q = deque([(start, 0)])

    while Q:
        state, m = Q.popleft()

        if state == target:
            return m

        for button in buttons:

            new_state = list(state)
            for pos in button:
                new_state[pos] += 1
            new_state = tuple(new_state)

            if new_state not in visited and valid(new_state, target):
                visited.add(new_state)
                Q.append((new_state, m + 1))
    return -1

def min_presses(target, buttons):
    # target: tuple/list length m  (joltage needed per light)
    # buttons: list of tuples/lists of light indices that button increments

    n = len(buttons)
    m = len(target)

    x = [Int(f"x{i}") for i in range(n)]

    opt = Optimize()

    # x_i are non-negative integers
    opt.add([xi >= 0 for xi in x])

    # For each light i: sum of presses of buttons that touch i == target[i]
    for i in range(m):
        opt.add(Sum([x[j] for j, b in enumerate(buttons) if i in b]) == target[i])

    opt.minimize(Sum(x))

    if opt.check() != sat:
        return None  # no solution

    model = opt.model()
    return sum(model[xi].as_long() for xi in x)

def part1():
    total = 0
    for machine in parse():
        target, buttons, _ = machine
        start = tuple([0]*len(target))
        pushes = bfs_lights(start, target, buttons)
        total += pushes
    return total

def part2():
    total = 0
    for machine in parse():
        _, buttons, target = machine
        pushes = min_presses(target, buttons)
        total += pushes
    return total

print('part 1:', part1())
print('part 2:', part2())
