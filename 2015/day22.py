from collections import deque

# cost, damage, heal, turns, damage, armor, mana
SPELL_LIST = [
    (53,  4, 0, 0, 0, 0, 0),
    (73,  2, 2, 0, 0, 0, 0),
    (113, 0, 0, 6, 0, 7, 0),
    (173, 0, 0, 6, 3, 0, 0),
    (229, 0, 0, 5, 0, 0, 101),
]

def process(hard_mode=False):
    global STATES
    global BEST_MANA

    depth, mana_spend, player, boss, active_spells = STATES.popleft()

    if hard_mode and depth % 2 == 1:
        player = (player[0]-1, player[1], player[2])
        if player[0] <= 0:
            return

    # apply effects
    spells_left = []
    # remove armour effect
    player = (player[0], 0, player[2])
    for active_spell in active_spells:
        # do whatever the spell is supposed to do
        _, _, _, _, damage, armour, mana = SPELL_LIST[active_spell[0]]
        player = (player[0], max(player[1], armour), player[2] + mana)
        boss = (boss[0] - damage, boss[1])
        # reduce timer and remove spells
        remaining = active_spell[1] - 1
        if remaining > 0:
            spells_left.append((active_spell[0], remaining))
    
    # are we done
    if boss[0] <= 0:
        BEST_MANA = min(BEST_MANA, mana_spend)
        return
    
    if player[0] <= 0:
        return
    
    # users move 
    if depth % 2 == 1:
        did_cast_a_spell = False
        for spell_idx, spell in enumerate(SPELL_LIST):
            spells = [*spells_left]
            # would this put us over our best?
            if mana_spend + spell[0] > BEST_MANA:
                continue

            # is the effect of the spell still running?
            if spell_idx in [a[0] for a in spells]:
                continue

            # can the player afford the mana
            if player[2] < spell[0]:
                continue

            # incur emediate effects
            _player = (player[0] + spell[2], player[1], player[2] - spell[0])
            _mana_spend = mana_spend + spell[0]
            _boss = (boss[0] - spell[1], boss[1])

            # does this spell include a timed effect?
            if spell[3] > 0:
                spells.append((spell_idx, spell[3]))

            did_cast_a_spell = True
            STATES.append((depth+1, _mana_spend, _player, _boss, tuple(spells)))

        if boss[0] <= 0:
            BEST_MANA = min(BEST_MANA, mana_spend)
            return
        
        if not did_cast_a_spell:
            return
        
    
    # boss move
    else:
        STATES.append((depth+1, mana_spend, (player[0] - max(1, boss[1] - player[1]), player[1], player[2]), boss, tuple(spells_left)))


BEST_MANA = float('inf')
STATES = deque([(1, 0, (50, 0, 500), (51, 9), ())])
while STATES: 
    process()
print(BEST_MANA)


BEST_MANA = float('inf')
STATES = deque([(1, 0, (50, 0, 500), (51, 9), ())])
while STATES: 
    process(True)
print(BEST_MANA)
