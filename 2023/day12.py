

def does_it_fit(p, n, i):
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

MEM = {}
def permutate(pattern, numbers):
    key = (pattern, ','.join(str(v) for v in numbers))
    if key in MEM: return MEM[key]

    min_width = len(numbers) + sum(numbers) - 1
    num = numbers[0]
    
    # the possible indexes where the number can fit
    fits = [i for i in range(len(pattern) - min_width + 1) if does_it_fit(pattern, num, i)]

    # if this was our last number, count the number of permutations
    if len(numbers[1:]) == 0:
        # remove any permutations that have a # after the last number
        b = 0
        for fit in fits:
            if '#' in pattern[fit+num:]:
                b += 1
        return len(fits)-b
    
    # recurse down into the next number
    Q = 0
    for fit in fits:
        next_index = fit+num+1
        Q += permutate(pattern[next_index:], numbers[1:])
                
    MEM[key] = Q
    return Q

permutations1 = 0
permutations2 = 0
with open("_input/day12.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        pattern, groups = line.split()
        numbers = list(map(lambda x: int(x), groups.split(',')))
        
        permutations1 += permutate(pattern, numbers)
        permutations2 += permutate('?'.join([pattern]*5), numbers*5)

print(permutations1)
print(permutations2)