from datetime import datetime
from itertools import permutations
from computer import Computer

program = []
with open('2019/_input/day7.txt') as fp:
    program = fp.readline().strip()

def test_phase(phases):
    output = 0
    comp = Computer(program)
    for i in phases:
        comp.reset()
        comp.set_input([i, output])
        output = comp.go()
    return output

def test_phase_loop(phases):

    comps = {}
    for idx, phase in enumerate(phases):
        comps[idx] = Computer(program)
        comps[idx].add_input(phase)

    signal = [0,0,0,0,0]
    loop_detect = None
    loop = 0

    while signal != None:

        for idx in range(5):
            comps[idx].add_input(signal[idx])
            output = comps[idx].go()
            if output == None:
                return signal[(idx)%5]
            signal[(idx+1)%5] = output
        
        if loop_detect == signal:
            loop += 1
            if loop > 1:
                print('loop detected', signal)
                return
        else:
            loop_detect = signal[:]

    return signal

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

print(part1())
print(part2())