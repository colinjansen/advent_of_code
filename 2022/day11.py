import re
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

    def throwTo(self, n: int) -> int:
        return self.true_monkey if n % self.denominator == 0 else self.false_monkey


def getMonkeys() -> list[Monkey]:
    return [
        Monkey(3, 4, 2, [99, 67, 92, 61, 83, 64, 98], lambda n: n * 17),
        Monkey(5, 3, 5, [78, 74, 88, 89, 50], lambda n: n * 11),
        Monkey(2, 6, 4, [98, 91], lambda n: n + 4),
        Monkey(13, 0, 5, [59, 72, 94, 91, 79, 88, 94, 51], lambda n: n * n),
        Monkey(11, 7, 6, [95, 72, 78], lambda n: n + 7),
        Monkey(17, 0, 2, [76], lambda n: n + 8),
        Monkey(19, 7, 1, [69, 60, 53, 89, 71, 88], lambda n: n + 5),
        Monkey(7, 1, 3, [72, 54, 63, 80], lambda n: n + 3)
    ]


def getLowestCommonMultiple(monkeys: list[Monkey]):
    return lcm(*map(lambda m: m.denominator, monkeys))


def inspect_item(monkey: Monkey):
    monkey.inspections += 1
    stress_level = monkey.items[0]
    stress_level = monkey.op(stress_level)
    if part == 2:
        stress_level %= lowestCommonMultiple
    if part == 1:
        stress_level = stress_level // 3
    return stress_level


def throw_item(monkeys: list[Monkey], monkey: Monkey, stress_level: int):
    monkey_index = monkey.throwTo(stress_level)
    monkey.items = monkey.items[1:]
    monkeys[monkey_index].items.append(stress_level)


def round(monkeys: list[Monkey]):
    for i in range(0, len(monkeys)):
        while (0 < len(monkeys[i].items)):
            stress_level = inspect_item(monkeys[i])
            throw_item(monkeys, monkeys[i], stress_level)


def productOfTwoHighest(monkeys: list[Monkey]):
    inspections = list(map(lambda m: m.inspections, monkeys))
    return prod(sorted(inspections)[-2:])


def go(monkeys: list[Monkey], n: int):
    for _ in range(0, n):
        round(monkeys)
    return productOfTwoHighest(monkeys)


monkeys = getMonkeys()
lowestCommonMultiple = getLowestCommonMultiple(monkeys)

part = 1
part1 = go(monkeys, 20)

part = 2
part2 = go(monkeys, 10000)

print(f'part 1 is {part1} part 2 is {part2}')
