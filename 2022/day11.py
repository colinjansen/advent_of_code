from math import prod, lcm
from functools import cache


class Monkey:

    def __init__(self, denominator: int, true_monkey: int, false_monkey: int, items: list[int], op):
        self.inspections = 0
        self.items: list[int] = items
        self.denominator: int = denominator
        self.true_monkey: int = true_monkey
        self.false_monkey: int = false_monkey
        self.op = op

    def inspect(self, monkeys, lcm):
        self.inspections += 1
        stress_level = self.calculate_stress_level(lcm)
        monkey_index = self.get_monkey_to_throw_to(stress_level)
        self.throw_item(monkeys[monkey_index], stress_level)

    def calculate_stress_level(self, lcm):
        stress_level = self.items[0]
        stress_level = self.op(stress_level)
        # for part 1 we just want to divide the stress level by three each round
        if part == 1:
            stress_level = stress_level // 3
        # for part 2 we need to keep the stress level boxes to the smallest
        # ceiling we can while still having all of the math work
        if part == 2:
            stress_level %= lcm
        return stress_level

    def get_monkey_to_throw_to(self, n: int) -> int:
        return self.true_monkey if n % self.denominator == 0 else self.false_monkey

    def throw_item(self, monkey, stress_level):
        self.items = self.items[1:]
        monkey.items.append(stress_level)


def getMonkeys() -> list[Monkey]:
    monkeys = [
        Monkey(3, 4, 2, [99, 67, 92, 61, 83, 64, 98], lambda n: n * 17),
        Monkey(5, 3, 5, [78, 74, 88, 89, 50], lambda n: n * 11),
        Monkey(2, 6, 4, [98, 91], lambda n: n + 4),
        Monkey(13, 0, 5, [59, 72, 94, 91, 79, 88, 94, 51], lambda n: n * n),
        Monkey(11, 7, 6, [95, 72, 78], lambda n: n + 7),
        Monkey(17, 0, 2, [76], lambda n: n + 8),
        Monkey(19, 7, 1, [69, 60, 53, 89, 71, 88], lambda n: n + 5),
        Monkey(7, 1, 3, [72, 54, 63, 80], lambda n: n + 3)
    ]
    lowestCommonMultiple = getLowestCommonMultiple(monkeys)
    return (monkeys, lowestCommonMultiple)


def getLowestCommonMultiple(monkeys: list[Monkey]):
    return lcm(*map(lambda m: m.denominator, monkeys))


def round(monkeys: list[Monkey], lcm: int):
    for i in range(0, len(monkeys)):
        while (0 < len(monkeys[i].items)):
            monkeys[i].inspect(monkeys, lcm)


def productOfTwoHighest(monkeys: list[Monkey]):
    inspections = list(map(lambda m: m.inspections, monkeys))
    return prod(sorted(inspections)[-2:])


def go(n: int):
    monkeys, lcm = getMonkeys()
    for _ in range(0, n):
        round(monkeys, lcm)
    return productOfTwoHighest(monkeys)



part = 1
part1 = go(20)

part = 2
part2 = go(10000)

print(f'part 1 is {part1} part 2 is {part2}')
