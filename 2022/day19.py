import re
from collections import deque

with open('_input/day19.txt') as f:
    lines = f.read().splitlines()

blueprints = {}
for line in lines:
    result = re.match('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian', line)
    g = result.groups()
    blueprints[int(g[0])] = (int(g[1]), int(g[2]), int(g[3]), int(g[4]), int(g[5]), int(g[6]))

def run_blueprint(BP, d = 24):

    DP = set()
    Q = deque()
    # state = robots: ore, clay, obsidian, geode
    #           ores: ore, clay, obsidian, geode
    #                 day
    Q.append((0, 0, 0, 0, 1, 0, 0, 0, d))
    BEST = 0
    CoO, CcO, CobO, CobC, CgeO, CgeOb = BP
    while Q:
        # remember what we already know
        state = Q.popleft()
        # pull out the variables from the state
        o, c, ob, g, Ro, Rc, Rob, Rg, day = state
        # update our 'best'
        BEST = max(BEST, g)
        # if our time has run out...
        if day == 0: continue

        # optimize robots
        max_ore = max([CoO, CcO, CobO, CgeO])
        if Ro >= max_ore: 
            Ro = max_ore
        if Rc >= CobC: 
            Rc = CobC
        if Rob >= CgeOb: 
            Rob = CgeOb

        # optimize minerals
        if o  >= max(max_ore, day * max_ore - Ro  * (day-1)): 
            o = max(max_ore, day * max_ore - Ro * (day-1))
        if c  >= max(CobC,    day * CobC    - Rc  * (day-1)): 
            c = max(0, day * CobC - Rc * (day-1))
        if ob >= max(CgeOb,   day * CgeOb   - Rob * (day-1)): 
            ob = max(0, day * CgeOb - Rob * (day-1))

        state = (o, c, ob, g, Ro, Rc, Rob, Rg, day)
        if state in DP: 
            continue
        DP.add(state)

        if (len(DP) % 1_000_000 == 0):
            print(state)
        
        # buy an ore robot
        if o >= CoO:
            Q.append((Ro + o - CoO, Rc + c, Rob + ob, Rg + g, Ro + 1, Rc, Rob, Rg, day - 1))

        # buy a clay robot
        if o >= CcO: 
            Q.append((Ro + o - CcO, Rc + c, Rob + ob, Rg + g, Ro, Rc + 1, Rob, Rg, day - 1))
            
        # buy an obsidian robot
        if o >= CobO and c >= CobC: 
            Q.append((Ro + o - CobO, Rc + c - CobC, Rob + ob, Rg + g, Ro, Rc, Rob + 1, Rg, day - 1))
        
        # buy a geode robot
        if o >= CgeO and ob >= CgeOb: 
            Q.append((Ro + o - CgeO, Rc + c, Rob + ob - CgeOb, Rg + g, Ro, Rc, Rob, Rg + 1, day - 1))

        # no robot builds
        Q.append((Ro + o, Rc + c, Rob + ob, Rg + g, Ro, Rc, Rob, Rg, day - 1))

    return BEST

def part1():
    minutes = 24
    total = 0
    for i in range(len(blueprints)):
        best = run_blueprint(blueprints[i+1], minutes)
        total += (i+1) * best
        print(f'blueprint {i + 1} has best {best} - total {total}')

def part2():
    minutes = 32
    totals = []
    for i in range(3):
        best = run_blueprint(blueprints[i+1], minutes)
        totals.append(best)
        print(f'blueprint {i + 1} has best {best}')
    print(totals[0] * totals[1] * totals[2])

part2()