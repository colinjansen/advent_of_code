
from functools import cache


with open('2019/_input/day16.txt') as f:
    data = f.read().strip()

base_pattern = [0, 1, 0, -1]
data = [int(x) for x in data]

@cache
def get_pattern(position, n):
    # Generate expanded pattern based on position
    base = [0, 1, 0, -1]
    pattern = []
    for num in base:
        pattern.extend([num] * (position + 1))
    # Shift pattern by 1 (first value is skipped)
    pattern = pattern[1:] + [pattern[0]]
    # Repeat pattern to cover the entire input length
    full_pattern = (pattern * (n // len(pattern) + 1))[:n]
    return full_pattern

@cache
def process(data, phase = 1):
    new_data = []
    pattern = get_pattern(phase-1, len(data))
    for i in range(len(data)):
        new_data.append(int(data[i]) * pattern[i])
    return new_data, str(sum(new_data))[-1]

def do_phase(numbers, n):
    result = []
    for i in range(n):
        pattern = get_pattern(i, n)
        total = sum(a * b for a, b in zip(numbers, pattern))
        result.append(abs(total) % 10)
    return result

def do_phases(data, num):
    for _ in range(num):
        data = do_phase(data, len(data))
    return ''.join(str(d) for d in data[:8])

print(do_phases(data, 100))