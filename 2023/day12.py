
MEM = {}
def get_permutations(p, nums, parts=[]):
    key = (p, ','.join(str(v) for v in nums))
    if key in MEM: return MEM[key]
    print(parts)
    n = nums[0]
    indexes = [i for i in range(len(p)-n+1) if 1 == get_possible_fits(p, n, i)]
    Q = 0
    for idx in indexes:
        if len(nums) > 1:
            parts.append(p[:idx+n])
            Q += get_permutations(p[idx+n+1:], nums[1:], parts)
        else: 
            parts.clear()
            return len(indexes)
        
    MEM[key] = Q
    return Q


def get_possible_fits(p, n, i):
    # no hash left behind
    for j in range(max(i-1, 0)):
        if p[j] == '#':
            return False
    # previous block should be null or . or ?
    start = i - 1
    if start >= 0 and p[start] not in ['.','?']:
        return False
    # all blocks should be # or ?
    for j in range(n):
        if p[i+j] not in ['#', '?']:
            return False
    # proper ending block . or ?
    end = i + n
    if end < len(p) and p[end] not in ['.', '?']:
        return False
    return 1


permutations1 = 0
permutations2 = 0
with open("_input/day12.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        pattern, groups = line.split()
        numbers = list(map(lambda x: int(x), groups.split(',')))
        permutations1 += get_permutations(pattern, numbers)
        #permutations2 += get_permutations('?'.join([pattern]*5), numbers*5)
#print(permutations1)
#print(permutations2)