import functools


with open("_input/day12.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

def get_possible_fits(p, n, i):
    if i > 0:
        # previous block should be null or . or ?
        if p[i-1] not in ['.','?']:
            return -3
        # no hash left behind
        for j in range(i-1):
            if p[j] == '#':
                return -4
    # proper ending block . or ?
    if i + n < len(p) and p[i + n] not in ['.', '?']:
        return -2
    # all blocks should be # or ?
    for j in range(n):
        if p[i+j] not in ['#', '?']:
            return -1
    return 1

MEM = {}
def generate(p, nums):
    key = (p, ','.join(str(v) for v in nums))
    if key in MEM: return MEM[key]
    
    n = nums[0]
    indexes = [i for i in range(len(p)-n+1) if 1 == get_possible_fits(p, n, i)]
    Q = 0
    for idx in indexes:
        if len(nums) > 1:
            Q += generate(p[idx+n+1:], nums[1:])
        else:
            return len(indexes)
        
    MEM[key] = Q
    return Q

t = 0
for l in lines:
    s, p = l.split()
    n = list(map(lambda x: int(x), p.split(',')))
    t += generate(s, n)
print(t)