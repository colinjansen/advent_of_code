from itertools import permutations
from math import ceil

WEAPONS = [
    ('Dagger' ,     8, 4, 0),
    ('Shortsword', 10, 5, 0),
    ('Warhammer',  25, 6, 0),
    ('Longsword',  40, 7, 0),
    ('Greataxe',   74, 8, 0)
]
ARMOUR = [
    ('Leather',     13,  0, 1),
    ('Chainmail',   31,  0, 2),
    ('Splintmail',  53,  0, 3),
    ('Bandedmail',  75,  0, 4),
    ('Platemail',  102,  0, 5)
]
RINGS = [
    ('Damage',  25,  1,  0),
    ('Damage',  50,  2,  0),
    ('Damage', 100,  3,  0),
    ('Defense', 20,  0,  1),
    ('Defense', 40,  0,  2),
    ('Defense', 80,  0,  3)
]

def fight(player, boss):
    p_hit = max(1, player[1] - boss[2])
    b_hit = max(1, boss[1] - player[2])
    return ceil(player[0] / b_hit) >= ceil(boss[0] / p_hit)

def part1():
    BEST = float('inf')
    for weapon in [(perm, sum([p[1] for p in perm])) for n in [1] for perm in permutations(WEAPONS, n)]:
        for armour in [(perm, sum([p[1] for p in perm])) for n in [0, 1] for perm in permutations(ARMOUR, n)]:
            for rings in [(perm, sum([p[1] for p in perm])) for n in [0, 1, 2] for perm in permutations(RINGS, n)]:
                total = weapon[1] + armour[1] + rings[1]
                if total < BEST:
                    damage = sum([w[2] for w in weapon[0]]) + sum([r[2] for r in rings[0]])
                    defense = sum([a[3] for a in armour[0]]) + sum([r[3] for r in rings[0]])
                    if fight((100, damage, defense), (103, 9, 2)):
                        BEST = total
    return BEST

def part2():
    BEST = 0
    for weapon in [(perm, sum([p[1] for p in perm])) for n in [1] for perm in permutations(WEAPONS, n)]:
        for armour in [(perm, sum([p[1] for p in perm])) for n in [0, 1] for perm in permutations(ARMOUR, n)]:
            for rings in [(perm, sum([p[1] for p in perm])) for n in [0, 1, 2] for perm in permutations(RINGS, n)]:
                total = weapon[1] + armour[1] + rings[1]
                if total > BEST:
                    damage = sum([w[2] for w in weapon[0]]) + sum([r[2] for r in rings[0]])
                    defense = sum([a[3] for a in armour[0]]) + sum([r[3] for r in rings[0]])
                    if not fight((100, damage, defense), (103, 9, 2)):
                        BEST = total
    return BEST

print(part1(), part2())