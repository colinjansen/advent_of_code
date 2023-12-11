from functools import reduce
import re

with open("_input/day5.txt") as f:
    lines = f.read().split()


def check(line):
    return (
        sum([1 for p in ["ab", "cd", "pq", "xy"] if p in line]) == 0
        and reduce(lambda a, c: (a[0] + (1 if a[1] == c else 0), c), line, (0, ""))[0]
        > 0
        and sum([1 for c in line if c in "aeiou"]) >= 3
    )


def check2(line):
    return None != re.search(r"(.).\1", line) and None != re.search(r"(.{2}).*?\1", line)


part_1 = sum([1 for line in lines if check(line) == True])
part_2 = sum([1 for line in lines if check2(line) == True])

print(part_1)
print(part_2)
