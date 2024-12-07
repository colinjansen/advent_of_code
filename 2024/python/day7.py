def can_create_value(target:int, nums:list[int], value:int, is_part_2: bool = False):
    if value == target:
        return True
    if value > target:
        return False
    if not nums:
        return False
    if is_part_2 and can_create_value(target, nums[1:], int(str(value) + str(nums[0])), is_part_2):
        return True
    if can_create_value(target, nums[1:], value * nums[0], is_part_2):
        return True
    if can_create_value(target, nums[1:], value + nums[0], is_part_2):
        return True
    return False

with open('2024/_input/day7.txt') as fp:
    part1 = 0
    part2 = 0
    for line in fp.readlines():
        v, nums = line.strip().split(':')
        nums = nums.split()
        v = int(v)
        nums = [int(n) for n in nums]
        if can_create_value(v, nums[1:], nums[0]):
            part1 += v
        if can_create_value(v, nums[1:], nums[0], True):
            part2 += v
    print(part1, part2)
