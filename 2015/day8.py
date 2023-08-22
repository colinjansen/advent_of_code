import functools
import re

lines = open('_input/day8.txt', 'r').readlines()


def raw(a, l):
    return a + len(l)


def escaped(a, l):
    return a + (len(l) + 2 + l.count("\\") + l.count("\""))


def unescaped(a, l):
    e = re.sub(r"\\x[0-9A-Fa-f]{2}", ' ', l[1:-1:])
    e = re.sub(r"\\\\", ' ', e)
    e = re.sub(r'\\\"', ' ', e)
    return a + len(e)


r = functools.reduce(raw, lines, 0)
u = functools.reduce(unescaped, lines, 0)
e = functools.reduce(escaped, lines, 0)

print(f'part 1 {r - u}  ---  part 2 {e - r}')
