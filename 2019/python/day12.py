import math
import re

moons = []

with open('2019/_input/day12.txt') as f:
    for line in f.readlines():
        x, y, z = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line).groups()
        moons.append([int(x), int(y), int(z), 0, 0, 0])

def tick():                 
    l = len(moons)
    for i in range(l - 1):
        for j in range(i+1, l):
            m1 = moons[i]
            m2 = moons[j]
            for k in [0,1,2]:
                if m1[k] < m2[k]:
                    m1[k+3] += 1
                    m2[k+3] -= 1
                elif m1[k] > m2[k]:
                    m1[k+3] -= 1
                    m2[k+3] += 1
    
    for m1 in moons:
        for k in [0,1,2]:
            m1[k] += m1[k+3]

def energy():
    total = 0
    for moon in moons:
        pot = sum(abs(moon[k]) for k in [0,1,2])
        kin = sum(abs(moon[k]) for k in [3,4,5])
        total += pot * kin
    return total

def get_state(moons, k):
    return tuple((m[k], m[k+3]) for m in moons)

state = [set(), set(), set()]
repeat = [0, 0, 0]
t = 0
while 0 in repeat:
    for k in [0,1,2]:
        s = get_state(moons, k)
        if s in state[k] and repeat[k] == 0:
            repeat[k] = t
        state[k].add(s)
    tick()
    t += 1
    
print(energy(), math.lcm(*repeat))