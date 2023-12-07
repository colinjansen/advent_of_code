import functools

with open("_input/day7.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

# holders for the hands and bids
hands = []
bids = []

# holders for the various kinds of hands
five = []
four = []
full = []
three = []
twopair = []
pair = []
high = []

def card_val(c, with_jokers=False) -> int:
    if c == 'A': return 14
    if c == 'K': return 13
    if c == 'Q': return 12
    if c == 'J': return 1 if with_jokers else 11
    if c == 'J': return 1
    if c == 'T': return 10
    return int(c)

def stage_1_sort(h, b, with_jokers=False):
    card_sets = {}
    jokers = 0
    groups_of_three = []
    groups_of_two = []

    for i in range(len(h)):
        if with_jokers and h[i] == 'J':
            jokers += 1
            continue
        if h[i] in card_sets:
            card_sets[h[i]] += 1
        else:
            card_sets[h[i]] = 1
    for k in card_sets.keys():
        if card_sets[k] == 5:
            return five.append((h, b))
        if card_sets[k] == 4:
            if jokers == 1:
                return five.append((h, b))
            return four.append((h, b))
        if card_sets[k] == 3:
            groups_of_three.append(k)
        if card_sets[k] == 2:
            groups_of_two.append(k)

    if len(groups_of_three) == 1 and len(groups_of_two) == 1:
        return full.append((h, b))
    
    if len(groups_of_three) == 1:
        if jokers == 2:
            return five.append((h, b))
        if jokers == 1:
            return four.append((h, b))
        return three.append((h, b))
    
    if len(groups_of_two) == 2:
        if jokers == 1:
            return full.append((h, b))
        return twopair.append((h, b))
    
    if len(groups_of_two) == 1:
        if jokers == 3:
            return five.append((h, b))
        if jokers == 2:
            return four.append((h, b))
        if jokers == 1:
            return three.append((h, b))
        return pair.append((h, b))
    
    if jokers == 4 or jokers == 5:
        return five.append((h, b))
    if jokers == 3:
        return four.append((h, b))
    if jokers == 2:
        return three.append((h, b))
    if jokers == 1:
        return pair.append((h, b))
    return high.append((h, b))

def get_value(with_jokers=False):

    # make sure our hand lists are empty
    for group in [high, pair, twopair, three, full, four, five]:
        group.clear()

    # sort the hands into their groups
    for i in range(len(hands)):
        stage_1_sort(hands[i], int(bids[i]), with_jokers)

    #comparison functions for stage 2 sorting
    def step_2_sort(a, b):
        h1 = a[0]
        h2 = b[0]
        for i in range(5):
            v1 = card_val(h1[i], with_jokers)
            v2 = card_val(h2[i], with_jokers)
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0
    
    rank = 0
    total = 0
    # for all of the (ordered) kinds of hands
    for group in [high, pair, twopair, three, full, four, five]:
        # sort the hands in the group by their value
        for e in sorted(group, key=functools.cmp_to_key(step_2_sort)):
            rank += 1
            total += rank * e[1]

    return total 

# parse the input into hands and bids
for line in lines:
    l = line.split(' ')
    hands.append(l[0])
    bids.append(l[1])

print(f'part 1: {get_value()} part 2: {get_value(True)}')