from collections import deque
import re

def parse():
    machines = []
    with open("_input/day10.txt") as f:
        for line in f.readlines():
            matches = re.match(r"\[(.+)\] (.+) {(.+)}", line)

            lights = matches[1].replace("#", "1").replace(".", "0")
            lights = tuple([int(l) for l in lights])

            target = tuple([1]*len(lights))

            buttons = [b.strip("()") for b in matches[2].split(" ")]
            buttons = [[int(pos) for pos in b.split(",")] for b in buttons]

            joltage = [int(j) for j in matches[3].split(",")]

            machines.append(tuple([lights, target, buttons, joltage]))
    return machines


def bfs(start, target, buttons):

    visited = {start}
    Q = deque([(start, 0)])

    while Q:
        state, m = Q.popleft()

        if state == target:
            return m

        for button in buttons:
            new_state = list(state)
            for pos in button:
                new_state[pos] = 1 - new_state[pos]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                Q.append((new_state, m + 1))
    return -1


for machine in parse():
    lights, target, buttons, joltage = machine
    print(bfs(lights, target, buttons))