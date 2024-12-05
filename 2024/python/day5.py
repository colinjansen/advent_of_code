import re
from collections import Counter, defaultdict


def check_valid(nums, before, after):
    for i in range(len(nums)):
        for b in range(0, i):
            if nums[b] not in before[nums[i]]:
                return False
        for a in range(i+1, len(nums)):
            if nums[a] not in after[nums[i]]:
                return False
    return True

def fix_order(nums, before, after):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums)-1):
            a = nums[i]
            b = nums[i+1]
            if b in before[a] or a in after[b]:
                nums[i] = b
                nums[i+1] = a
                sorted = False
                break
    return nums

before = defaultdict(set)
after = defaultdict(set)
part1 = 0
part2 = 0
with open('2024/_input/day5.txt') as fp:
    for line in fp.readlines():
        if '|' in line:
            d1, d2 = line.split('|')
            d1 = int(d1)
            d2 = int(d2)
            after[d1].add(d2)
            before[d2].add(d1)

        if ',' in line:
            nums = list(map(lambda x: int(x), line.split(',')))
            if check_valid(nums, before, after):
                part1 += nums[len(nums)//2]
            else:
                fixed = fix_order(nums, before, after)
                part2 += fixed[len(fixed)//2]
print(part1)
print(part2)
