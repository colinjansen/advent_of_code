from collections import Counter
import re

def is_ordered(nums):
    s = sorted(nums)
    r = sorted(nums, reverse=True)
    return nums == s or nums == r

def is_safe(nums):
    if not is_ordered(nums):
        return False
    for i in range(1, len(nums)):
        d = abs(nums[i-1] - nums[i])
        if d == 0 or d > 3:
            return False
    return True

def try_all(nums, func):
    if func(nums):
        return True
    for i in range(len(nums)):
        if func(nums[:i] + nums[i+1:]):
            return True
    return False

part1 = 0
part2 = 0

with open(f"2024/_input/day2.txt") as fp:
    for line in fp.readlines():
        nums = [int(n) for n in line.split()]
        if is_safe(nums):
            part1 += 1
        if try_all(nums, is_safe):
            part2 += 1
        
print('part 1:', part1)
print('part 2:', part2)