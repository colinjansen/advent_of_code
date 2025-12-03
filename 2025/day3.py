def parse():
    data = []
    with open('_input/day3.txt') as f:
        for line in f.readlines():
            data.append([int(c) for c in line.strip()])
    return data

def best(bank, start_position, search_length):
    max_digit = 0
    position = 0
    for index in range(start_position, min(len(bank), start_position+search_length)):
        if max_digit < bank[index]:
            max_digit = bank[index]
            position = index
    return (max_digit, position)
    
def find_joltage(bank, width=12):
    digits = [0]*width
    start_position = 0
    for index in range(width):
        search_length = len(bank) - start_position - (width-index) + 1
        digit, found_position = best(bank, start_position, search_length)
        digits[index] = digit
        start_position = found_position + 1
    return int(''.join([str(d) for d in digits]))


banks = parse()

print('part 1: ', sum([find_joltage(bank, 2) for bank in banks]))
print('part 2: ', sum([find_joltage(bank, 12) for bank in banks]))
