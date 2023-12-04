from functools import reduce
import re

with open("_input/day4.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

part_1 = 0
card_duplicate_count = {}

def update_card_count_for_part_2(card_number, matches):
    if card_number not in card_duplicate_count:
        card_duplicate_count[card_number] = 0
    card_duplicate_count[card_number] += 1
    for _ in range(card_duplicate_count[card_number]):
        for i in range(1, matches + 1):
            if card_number + i not in card_duplicate_count:
                card_duplicate_count[card_number + i] = 0
            card_duplicate_count[card_number + i] += 1

def count_matches(arr1, arr2):
    matches = 0
    for i in arr1:
        if i in arr2:
            matches += 1
    return matches

for line in lines:
    groups = re.match('Card\s+(\d+):(.*)\|(.*)', line).groups()
    card_number = int(groups[0])
    mine = list(filter(lambda x: x, groups[1].strip().split(' ')))
    nums = list(filter(lambda x: x, groups[2].strip().split(' ')))

    matches = count_matches(mine, nums)
    part_1 += 2**matches//2

    update_card_count_for_part_2(card_number, matches)

print(f'part 1: {part_1}')
print(f'part 2: {sum(card_duplicate_count.values())}')