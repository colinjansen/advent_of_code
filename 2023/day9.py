def all_zeros(S):
    for i in S:
        if i != 0:
            return False
    return True

def get_to_zero(source):
    entries = []
    entries.append(source)
    entry = []
    current = source
    while not all_zeros(current):
        entry = []
        for i in range(1, len(current)):
            entry.append(current[i] - current[i-1])
        entries.append(entry)
        current = entry
    return entries

def ex(line):
    entries = get_to_zero([int(x) for x in line.split()])
    accumulator_1 = 0
    accumulato_2 = 0
    for i in range(len(entries)-2, -1, -1):
        accumulator_1 = entries[i][-1] + accumulator_1
        accumulato_2 = entries[i][0] - accumulato_2
    return (accumulator_1, accumulato_2)


with open("_input/day9.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

total_1 = 0
total_2 = 0
for line in lines:
    extrapolations = ex(line)
    total_1 += extrapolations[0]
    total_2 += extrapolations[1]
    
print(total_1, total_2)