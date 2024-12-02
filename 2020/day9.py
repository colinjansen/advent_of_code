D = []
with open('day9.txt', 'r') as file:
    for line in file.readlines():
        D.append(int(line))

def can_find_target(t, nums):
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == t:
                return True
    return False

def part1(pre):
    for n in range(pre, len(D)):
        d = D[n]
        nums = D[n-pre:n]
        if not can_find_target(d, nums):
            return d

def part2(target):
    s = 0
    e = 0
    T = D[0]
    while T != target:
        if T > target:
            T -= D[s]
            s += 1
            continue
        if T < p1:
            e += 1
            T += D[e]
            continue
    nums = D[s:e+1]
    return min(nums) + max(nums)

p1 = part1(25)  # 248131121
p2 = part2(p1)

print(p1, p2)