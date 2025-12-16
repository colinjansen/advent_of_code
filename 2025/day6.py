from collections import defaultdict

def parse():
    O = []

    spaces = defaultdict(int)
    lines = []
    with open("_input/day6.txt") as f:
        for line in f.readlines():
            if not line:
                continue
            lines.append(line.strip("\n"))
            for i, c in enumerate(line):
                if c == ' ':
                    spaces[i] += 1
    height = len(lines)
    spaces = [k for k, v in spaces.items() if v == height]
    spaces.append(len(lines[0]))

    offset = 0
    M = defaultdict(list)
    for s in spaces:
        for idx, line in enumerate(lines):
            M[idx].append(line[offset:s])
        offset = s+1
    M = list(M.values())

    O = [m.strip() for m in M[-1]]
    M = M[0:-1]

    L = defaultdict(list)
    for i, _ in enumerate(O):
        for m in M:
            L[i].append(m[i])
    L = list(L.values())
    
    return L, O

def prod(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        a *= arr[i]
    return a

def part2(nums):
    m = len(nums[0])
    a = []
    for i in range(m-1, -1, -1):
        b = ''
        for n in nums:
            b += n[i]
        #if not b.strip():
        #    print(nums)
        a.append(int(b) if b.strip() else 0)
    return a

def run(parser):
    nums, ops = parse()
    a = 0
    for i, _ in enumerate(nums):
        if ops[i] == '*':
            a += prod(parser(nums[i]))
        if ops[i] == "+":
            a += sum(parser(nums[i]))
    return a

print("part 1: ", run(lambda x: [int(i) for i in x]))
print("part 2: ", run(part2))