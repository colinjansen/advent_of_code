import re

with open('2024/_input/day3.txt') as fp:
    total_part_1 = 0
    total_part_2 = 0
    do_multiplications = True
    for line in fp.readlines():
        for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            if match.startswith('don'):
                do_multiplications = False
                continue
            if match.startswith('do'):
                do_multiplications = True
                continue
            if match.startswith('mul'):
                vals = re.findall('(\d+)', match)
                total_part_1 += int(vals[0]) * int(vals[1])
                if do_multiplications:
                    total_part_2 += int(vals[0]) * int(vals[1])
    print(total_part_1, total_part_2)