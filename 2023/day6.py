def race(hold, duration):
    if hold >= duration or hold ==0:
        return 0
    return hold * (duration - hold)

def lower_bound(duration, best):
    for i in range(duration):
        r = race(i, duration)
        if r > best:
            return i
    return False

def upper_bound(duration, best):
    for i in range(duration, 0, -1):
        r = race(i, duration)
        if r > best:
            return i
    return False

def part1():
    t = [35, 69, 68, 87]
    d = [213, 1168, 1086, 1248]
    total = 1
    for i in range(len(t)):
        total *= (upper_bound(t[i], d[i]) - lower_bound(t[i], d[i]) + 1)
    return total

def part2():
    t = 35696887
    d = 213116810861248
    return upper_bound(t, d) - lower_bound(t, d) + 1

print(f'part 1: {part1()} part 2: {part2()}')