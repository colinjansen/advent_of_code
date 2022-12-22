import re

with open('_input/day19.txt.test') as f:
    lines = f.read().splitlines()

class Blueprint:
    def __init__(self, id:int, ore:int, clay:int, obsidian_ore: int, obsidian_clay: int, geode_ore: int, geode_obsidian: int):
        self.id = int(id)
        self.cost_ore_ore = int(ore)
        self.cost_clay_ore = int(clay)
        self.cost_obsidian_ore = int(obsidian_ore)
        self.cost_obsidian_clay = int(obsidian_clay)
        self.cost_geode_ore = int(geode_ore)
        self.cost_geode_obsidian = int(geode_obsidian)
    def __repr__(self):
        return f'#{self.id} ORE:{self.cost_ore_ore} CLAY:{self.cost_clay_ore} OBSIDIAN:{self.cost_obsidian_ore}/{self.cost_obsidian_clay} GEODE:{self.cost_geode_ore}/{self.cost_geode_obsidian}'
    

blueprints = []
for line in lines:
    result = re.match('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian', line)
    blueprints.append(Blueprint(*result.groups()))

def run(bp: Blueprint, time: int):

    # mineral cache
    ore = 0
    clay = 0
    obsidian = 0
    geode = 0

    # bots
    ore_bots = 1
    clay_bots = 0
    obsidian_bots = 0
    geode_bots = 0

    # bots being built
    ore_bots_building = 0
    clay_bots_building = 0
    obsidian_bots_building = 0
    geode_bots_building = 0

    # the big stinking BL loop
    for minute in range(1, time + 1):
        print(f"minute {minute}")

        # build a geode bot?
        if obsidian >= bp.cost_geode_obsidian and ore >= bp.cost_geode_ore:
            obsidian -= bp.cost_geode_obsidian
            ore -= bp.cost_geode_ore
            geode_bots_building += 1
            print('\tbuilding a geode bot')

        # build an obsidian bot?
        if clay >= bp.cost_obsidian_clay and ore >= bp.cost_obsidian_ore:
            clay -= bp.cost_obsidian_clay
            ore -= bp.cost_obsidian_ore
            obsidian_bots_building += 1
            print('\tbuilding an obsidian bot')

        # build a clay bot?
        if ore >= bp.cost_clay_ore:
            ore -= bp.cost_clay_ore
            clay_bots_building += 1
            print('\tbuilding a clay bot')

        # collect your minerals, bots
        ore += ore_bots
        clay += clay_bots
        obsidian += obsidian_bots
        geode += geode_bots

        if ore_bots:
            print(f'\t{ore_bots} ore bots collected {ore_bots} ore: we now have {ore}')
        if clay_bots:
            print(f'\t{clay_bots} clay bots collected {clay_bots} ore: we now have {clay}')
        if obsidian_bots:
            print(f'\t{obsidian_bots} obsidian bots collected {obsidian_bots} ore: we now have {obsidian}')
        if geode_bots:
            print(f'\t{geode_bots} geode bots collected {geode_bots} ore: we now have {geode}')

        # add the bots being built
        if ore_bots_building:
            print(f"\tadding {ore_bots_building} ore bots")
        ore_bots += ore_bots_building
        ore_bots_building = 0

        if clay_bots_building:
            print(f"\tadding {clay_bots_building} clay bots")
        clay_bots += clay_bots_building
        clay_bots_building = 0

        if obsidian_bots_building:
            print(f"\tadding {obsidian_bots_building} obsidian bots")
        obsidian_bots += obsidian_bots_building
        obsidian_bots_building = 0

        if geode_bots_building:
            print(f"\tadding {geode_bots_building} geode bots")
        geode_bots += geode_bots_building
        geode_bots_building = 0


    #return how many geodes we cracked
    return geode


print(run(blueprints[0], 24))