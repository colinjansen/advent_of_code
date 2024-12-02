import re

def day1(input):
    m = re.match('(\d*)-(\d*)\s*(\w*):\s*(\w*)', input)
    l, h, c, p = m.groups()
    C = p.count(c)
    return C >= int(l) and C <= int(h)


def day2(input):
    m = re.match('(\d*)-(\d*)\s*(\w*):\s*(\w*)', input)
    l, h, c, p = m.groups()
    a = p[int(l)-1]
    b = p[int(h)-1]
    return a != b and (a == c or b == c)


with open('2020\day2.txt', 'r') as fd:
    lines = fd.readlines()
    print(len([v for v in list(map(day1, lines)) if v == True]))
    print(len([v for v in list(map(day2, lines)) if v == True]))

