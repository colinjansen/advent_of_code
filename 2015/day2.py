with open("_input/day2.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

def measure_wrap(l, w, h):
    a = l*w
    b = w*h
    c = h*l
    return (2*a) + (2*b) + (2*c) + min(a, b, c)

def measure_ribbon(l, w, h):
    a = (2*l)+(2*w)
    b = (2*w)+(2*h)
    c = (2*h)+(2*l)
    return (l*w*h) + min(a, b, c)

part1 = 0
part2 = 0
for line in lines:
    d = line.split('x')
    part1 += measure_wrap(int(d[0]), int(d[1]), int(d[2]))
    part2 += measure_ribbon(int(d[0]), int(d[1]), int(d[2]))

print(part1, part2)