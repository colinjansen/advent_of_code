def part_1(INPUT):
    INPUT = INPUT // 10
    houses = [0] * INPUT
    house_number = INPUT

    for i in range(1, INPUT):
        for j in range(i, INPUT, i):
            houses[j] += i
            if houses[j] >= INPUT and j < house_number:
                house_number = j
    return house_number

def part_2(INPUT):
    max_house = INPUT // 11
    houses = [0] * (max_house + 1)
    house_number = max_house

    for elf in range(1, max_house):
        visits = 0
        for house in range(elf, max_house + 1, elf):
            if houses[house] == 0:
                houses[house] = 11 + elf * 11
            else:
                houses[house] += elf * 11

            if houses[house] >= INPUT and house < house_number:
                house_number = house

            visits += 1
            if visits == 50:
                break

    return house_number

print(part_1(29000000))
print(part_2(29000000))