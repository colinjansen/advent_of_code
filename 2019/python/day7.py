from datetime import datetime
from itertools import permutations
from computer import Computer

program = []
with open('2019/_input/day7.txt') as fp:
    program = fp.readline().split(',')
    program = [int(c) for c in program]


def test_phase(phases):
    output = 0
    comp = Computer(program)
    for i in phases:
        comp.reset()
        comp.set_input([i, output])
        output = comp.go()
    return output

def test_phase_loop(phases):
    output = 0
    comps = [Computer(program)] * 5
    running = [True] * 5
    while any(running):
        for idx, phase in enumerate(phases):
            comps[idx].set_input([phase, output])
            res = comps[idx].go()
            if res == None:
                running[idx] = False
            else:
                output = res
    return output

def part1():
    m = 0
    for phases in permutations([0,1,2,3,4]):
        m = max(m, test_phase(phases))
    return m
    

def part2():
    m = 0
    for phases in permutations([5,6,7,8,9]):
        m = max(m, test_phase_loop(phases))
    return m
    
print(part2())