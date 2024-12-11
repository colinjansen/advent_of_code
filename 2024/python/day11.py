from collections import deque
from functools import cache

with open('2024/_input/day11.txt') as f:
    stones = [int(s) for s in f.read().strip().split()]

@cache
def blink(stone:int, n:int) -> int:
    if n == 0: 
        return 1
    
    if stone == 0: 
        return blink(1, n - 1)
    
    stone_as_string = str(stone)
    length_of_stone = len(stone_as_string)

    if length_of_stone % 2:
        return blink(stone * 2024, n - 1)
    
    left = stone_as_string[:length_of_stone // 2]
    right = stone_as_string[length_of_stone // 2:]
    return blink(int(left), n - 1) + blink(int(right), n - 1)
    

print('part 1', sum(blink(c, 25) for c in stones))
print('part 2', sum(blink(c, 75) for c in stones))
