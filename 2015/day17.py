from itertools import combinations

containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

result = [seq for i in range(len(containers), 0, -1) for seq in combinations(containers, i) if sum(seq) == 150]

print(f"Part 1: {len(result)}")
min_length = min(len(seq) for seq in result)
print(f"Part 2: {len([seq for seq in result if len(seq) == min_length])}")