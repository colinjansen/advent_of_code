from collections import deque
from functools import cache

with open('2024/_input/day11.txt') as f:
    stones = [int(s) for s in f.read().strip().split()]

@cache
def blink(stone:int, n:int, target:int) -> int:
    if n == target: 
        return 1
    
    n += 1
    if stone == 0: 
        return blink(1, n, target)
    
    stone_as_string = str(stone)
    length_of_stone = len(stone_as_string)

    if length_of_stone % 2:
        return blink(stone * 2024, n, target)
    
    left = stone_as_string[:length_of_stone // 2]
    right = stone_as_string[length_of_stone // 2:]
    return blink(int(left), n, target) + blink(int(right), n, target)
    

print('part 1', sum(blink(c, 0, 25) for c in stones))
print('part 2', sum(blink(c, 0, 75) for c in stones))
