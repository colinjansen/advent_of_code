def parse():
    data = []
    with open('_input/day3.txt') as f:
        for l in f.readlines():
            data.append(l.strip())
    return data

