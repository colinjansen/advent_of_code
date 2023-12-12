import functools


with open("_input/day12.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

def gen(s, nums):
    s = '.' + s + '.'
    def find_places(n, start = 0):
        def fit():
            if s[i-1] not in ['.','?']:
                return False
            if s[i + n] not in ['.', '?']:
                return False
            for j in range(n):
                if s[i+j] not in ['#', '?']:
                    return False
            return True

        res = []
        # find the first spot that n will fit
        for i in range(start + 1, len(s)-n):
            if fit():
                res.append(i-1)
        return res
    
    p = 0
    res = []
    for n in nums:
        r = find_places(n, p)
        res.append((r, n, p))
        p = r[0] + n + 1
    return list(reversed(res))

@functools.cache
def get_count(res, m, i = 0, k = [], s = []):
    for r in res[i][0]:
        if (r + res[i][1]-1) <= m:
            if len(k) + 1 == len(res):
                s.append([*k, r])
            if i < len(res)-1:
                get_count(res, r-2, i+1, [*k, r], s)
    return s

def test(pattern, nums, solutions):
    bad = 0

    def check(c):        
        for i, _ in enumerate(pattern):
            if c[i] == '.' and pattern[i] not in ['.','?']:
                return False
            if c[i] == '#' and pattern[i] not in ['#', '?']:
                return False
        return True
    
    #print(pattern, nums)
    for s in solutions:
        s = list(reversed(s))
        c = list('.'*len(pattern))
        for i, _ in enumerate(s):
            for j in range(s[i], s[i]+nums[i]):
                c[j] = '#'
        #print(pattern, nums)
        if False == check(c):
            bad += 1
            #print(''.join(c))
    return bad

t = 0
b = 0
for l in lines:
    s, p = l.split()
    n = list(map(lambda x: int(x), p.split(',')))
    res = gen(s, n)
    sol = get_count(res, len(s), 0, [], [])
    t += len(sol)
    b += test(s, n, sol)

print(t - b)