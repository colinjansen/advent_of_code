part1 = 0
part2 = 0

def fuel(weight):
    total_fuel = 0
    f = (weight // 3) - 2
    while f > 0:
        total_fuel += f
        weight = f
        f = (weight // 3) - 2
    return total_fuel

with open('2019/_input/day1.txt') as fp:
    for line in fp.readlines():
        part1 += (int(line) // 3) -2
        part2 += fuel(int(line))


print(part1)
print(part2)