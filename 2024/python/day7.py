def can_create_value(target:int, nums:list[int], value:int, is_part_2: bool = False):
    """
    Recursively checks if target value can be created using arithmetic operations on nums
    Args:
        target: The target value to reach
        nums: List of numbers to use
        value: Current running value
        is_part_2: Whether to allow concatenation operation
    Returns:
        bool: Whether target can be created
    """
    # Base cases
    if value == target:
        return True
    if value > target or not nums:
        return False

    # Cache next number and rest of list to avoid repeated slicing
    num = nums[0]
    rest = nums[1:]

    # Try concatenation if part 2
    if is_part_2:
        concat_val = int(str(value) + str(num))
        if can_create_value(target, rest, concat_val, is_part_2):
            return True

    # Try multiplication and addition
    return (can_create_value(target, rest, value * num, is_part_2) or
            can_create_value(target, rest, value + num, is_part_2))

# Process input file
with open('2024/_input/day7.txt') as fp:
    part1 = part2 = 0
    for line in fp.readlines():
        # Parse each line into target value and list of numbers
        v, nums = line.strip().split(':')
        v = int(v)
        nums = [int(n) for n in nums.split()]

        # Check if target can be created for both parts
        if can_create_value(v, nums[1:], nums[0]):
            part1 += v
        if can_create_value(v, nums[1:], nums[0], True):
            part2 += v

    print(part1, part2)
