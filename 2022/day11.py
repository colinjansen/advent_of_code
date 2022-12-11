import re
import math


class Monkey:

    def __init__(self, d: int, t: int, f: int, items: list[int], op):
        self.inspections = 0
        self.items: list[int] = items
        self.test_d: int = d
        self.test_t: int = t
        self.test_f: int = f
        self.op = op

    def __str__(self) -> str:
        return f'Monkey {self.inspections} {self.items}'

    def throwTo(self, n: int) -> int:
        return self.test_t if n % self.test_d == 0 else self.test_f


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


def getSuperModulo(monkeys: list[Monkey]):
    sm = 1
    for m in monkeys:
        sm *= m.test_d
    return sm


def round(monkeys: list[Monkey], sm, p):
    for i in range(0, len(monkeys)):
        while (0 < len(monkeys[i].items)):
            monkeys[i].inspections += 1
            wl = monkeys[i].items[0]
            wl = monkeys[i].op(wl)
            if p == 2: wl %= sm
            if p == 1: wl = wl // 3
            m = monkeys[i].throwTo(wl)
            monkeys[i].items = monkeys[i].items[1:]
            monkeys[m].items.append(wl)


def productOfTwoHighest(monkeys: list[Monkey]):
    two = sorted(list(map(lambda m: m.inspections, monkeys)))[-2:]
    return two[0] * two[1]


def go(n: int, p: int):
    monkeys = getMonkeys()
    sm = getSuperModulo(monkeys)
    for _ in range(0, n):
        round(monkeys, sm, p)
    return productOfTwoHighest(monkeys)


print(f'part 1 is {go(20, 1)} part 2 is {go(10000, 2)}')

