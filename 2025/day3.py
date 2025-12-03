from itertools import combinations

def parse():
    data = []
    with open('_input/day3.txt') as f:
        for l in f.readlines():
            data.append(l.strip())
    return data

def find_joltage(b, w=2):
    m = 0
    for c in combinations(b, w):
        m = max(m, int(''.join(c)))
    return m

def best(bank, start, length):
    max_digit = 0
    position = 0
    for index in range(start, min(len(bank), start+length)):
        if max_digit < bank[index]:
            max_digit = bank[index]
            position = index
    return (max_digit, position)
    
def find_joltage_2(bank, width=12):
    digits = [0]*12
    start_position = 0
    for index in range(12):
        search_length = len(bank) - start_position - (width-index) + 1
        digit, found_position = best(bank, start_position, search_length)
        digits[index] = digit
        start_position = found_position + 1
    return int(''.join([str(d) for d in digits]))


part_1 = 0
part_2 = 0
for bank in parse():
    part_1 += find_joltage(bank)
    p2 = find_joltage_2([int(b) for b in bank])
    part_2 += p2

print('part 1: ', part_1)
print('part 2: ', part_2)
