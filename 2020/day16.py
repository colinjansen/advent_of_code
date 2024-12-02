from collections import defaultdict

def parse():
    ranges = {}
    nums = []
    with open('_input/day16.txt') as fp:
        line = None
        while line != '':
            line = fp.readline().strip()
            if line:
                key = line.split(':')[0].strip()
                ranges[key] = []
                for range in line.split(':')[1].split('or'):
                    ranges[key].append(tuple(map(lambda x: int(x), range.split('-'))))
        line = None
        while line != '':
            line = fp.readline().strip()
            if line:
                pass

        line = None
        while line != '':
            line = fp.readline().strip()
            if line == 'nearby tickets:':
                continue
            if line:
                nums.append(list(map(lambda x: int(x), line.split(','))))


    return ranges, remove_invalid_rows(nums, ranges)

def in_ranges(n, ranges):
    for k in ranges:
        for r in ranges[k]:
            if n >= r[0] and n <= r[1]:
                return True
    return False

def is_valid_row(row, ranges):
    for n in row:
        if not in_ranges(n, ranges):
            return False
    return True

def remove_invalid_rows(nums, ranges):
    errors = []
    for i, r in enumerate(nums):
        if not is_valid_row(r, ranges):
            errors.append(i)
    for e in errors[::-1]:
        del nums[e]
    return nums

def find_ranges(nums, ranges):
    result = defaultdict(int)
    for n in nums:
        for k in ranges:
            for r in ranges[k]:
                if n >= r[0] and n <= r[1]:
                    result[k] += 1
    return [r for r in result if result[r] == 190]

ranges, nums = parse()

results = defaultdict(int)
for i in range(20):
    results[i] = find_ranges([row[i] for row in nums], ranges)

while len([r for r in results if len(results[r]) > 1]) > 1:
    for final in [r for r in results if len(results[r]) == 1]:
        remove_me = results[final][0]
        # remove final from the rest
        for r in results:
            if r != final:
                results[r] = [i for i in results[r] if i != remove_me]

t = 1
ticket = [131,67,137,61,149,107,109,79,71,127,173,157,167,139,151,163,59,53,113,73]
for i in range(20):
    if 'departure' in results[i][0]:
        t *= ticket[i]
        print(results[i], i, ticket[i])
print(t)