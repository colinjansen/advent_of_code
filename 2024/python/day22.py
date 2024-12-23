from collections import defaultdict
from datetime import datetime


def calculate_diffs(n, a=2000):
    def run(n):
        n ^= n << 6        # multiply by 64
        n %= 16777216
        n ^= n >> 5        # divide by 32
        n %= 16777216
        n ^= n << 11       # multiply by 2048
        n %= 16777216
        return n

    diffs = [0] * a
    sequences = defaultdict(int)
    for i in range(a):
        last_price = n % 10
        n = run(n)
        price = n % 10
        diffs[i] = price - last_price
        if i >= 3:
            seq = tuple(diffs[i-3:i+1])
            # since the monkey will sell at the 'first' occurence of a sequence
            # only add the sequence to the dictionary if it has not been added before
            if seq not in sequences:
                sequences[seq] = price
    return sequences, n

def get_parts():
    part1 = 0
    # all possible sequences
    all_sequences = set()
    # difference sequences for each buyer
    buyer_sequences = []
    # find the best sequence to buy
    maximum_banana_count = 0

    start_time = datetime.now()
    with open('2024/_input/day22.txt') as f:
        for line in f.readlines():
            diff_sequences, value = calculate_diffs(int(line.strip()))
            part1 += value
            buyer_sequences.append(diff_sequences)
            all_sequences |= set(diff_sequences.keys())

    print('time to gather sequence data:', datetime.now() - start_time)

    for sequence in all_sequences:
        total = 0
        for buyer in buyer_sequences:
            if sequence in buyer:
                total += buyer[sequence]

        if total > maximum_banana_count:
            maximum_banana_count = total

    print('time to parse data:', datetime.now() - start_time)

    return part1, maximum_banana_count

part1, part2 = get_parts()

print('Part 1:', part1)
print('Part 2:', part2)