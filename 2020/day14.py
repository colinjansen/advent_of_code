import re

with open('_input/day14.txt') as fp:
    part1 = {}
    part2 = {}
    for line in fp.readlines():

        m = re.match('mask = ([X10]*)', line)
        if m:
            mask = m.groups()[0]     
            ones = int(mask.replace('X', '0'), 2)  # use |
            nones = int(mask.replace('X', '1'), 2) # use &
            floats = [i for i in range(len(mask)) if mask[i] == 'X']
            continue

        m = re.match('mem\[(\d*)\] = (\d*)', line)
        if m:
            address = int(m.groups()[0])
            value = int(m.groups()[1])

        part1[address] = (value | ones) & nones

        for i in range(int('1'*len(floats), 2)+1):
            a = list(bin(address | ones)[2:].zfill(36))
            b = bin(i)[2:].zfill(len(floats))
            
            for j in range(len(floats)):
                a[floats[j]] = b[j]
            a2 = int(''.join(a), 2)
            part2[a2] = value
        



print(sum(part1.values()))
print(sum(part2.values()))
    
