def extract(text, start_delimiter='(', end_delimiter=')'):
    result = []
    stack = []
    start = -1
    
    for i, char in enumerate(text):
        if char == start_delimiter:
            if start == -1:
                start = i
            stack.append(char)
        elif char == end_delimiter:
            if stack:
                stack.pop()
                if not stack:
                    result.append((text[start + 1:i], start, i+1))
                    start = -1
    
    return result

def compute(line):
    d = 0
    for t, s, e in extract(line):
        c = compute(t)
        line = line[:(s+d)] + c + line[(e+d):]
        d += len(c) - (len(t)+2)

    return str(bedmas(line))

def add_parts(parts):
    for i in range(len(parts)-1, -1, -1):
        if parts[i] == '+':
            i -= 1
            parts[i] = int(parts[i]) + int(parts[i+2])
            del parts[i+2]
            del parts[i+1]
    return parts

def multiply_parts(parts):
    for i in range(len(parts)-1, -1, -1):
        if parts[i] == '*':
            i -= 1
            parts[i] = int(parts[i]) * int(parts[i+2])
            del parts[i+2]
            del parts[i+1]
    return parts

def bedmas(line):
    parts = line.split(' ')
    parts = add_parts(parts)
    parts = multiply_parts(parts)
    return str(parts[0])

with open('_input/day18.txt') as fp:
    total = 0
    for line in fp.readlines():
        total += int(compute(line))
        print(total, '=', line.strip())
    print('=', total)