def react(a, b):
    return 32 == abs(ord(a)-ord(b))

def collapse(line):
    i = len(line)
    r = []
    while i >= 0:
        i -= 1
        # if we're at the tail end, move one so that 
        # we can compare this and this + 1
        if i == len(line) - 1:
            i -= 1
        if react(line[i], line[i+1]):
            del line[i+1]
            del line[i]
    return line

with open('_input/day5.txt') as fp:
    line = fp.readline()
    lens = []
    for i in range(65, 91):
        c = line.replace(chr(i), '').replace(chr(i+32), '')
        lens.append(len(collapse(list(c))))
    print(min(lens))