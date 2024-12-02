from collections import Counter

left = []
right = []
with open(f"2024/_input/day1.txt") as fp:
    for line in fp.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
left.sort()
right.sort()
counter = Counter(right)

print('part 1', sum([ abs(left[i] - right[i]) for i in range(len(left)) ]))
print('part 2', sum([ left[i] * counter[left[i]] for i in range(len(left)) ]))