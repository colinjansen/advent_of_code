pass_from = 264360
pass_to = 746325

MIN_LENGTH = 6


def criteria(p, mf):
    if len(p) != MIN_LENGTH or any(p[i] > p[i + 1] for i in range(MIN_LENGTH - 1)):
        return False
    groups = [p.count(ch) for ch in set(p)]
    return any([mf(g) for g in groups])


part1 = sum([criteria(str(p), lambda x: x >= 2) for p in range(pass_from, pass_to + 1)])
part2 = sum([criteria(str(p), lambda x: x == 2) for p in range(pass_from, pass_to + 1)])

print(part1, part2)
