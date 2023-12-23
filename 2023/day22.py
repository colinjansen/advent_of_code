

import re


def parse():
    B = []
    with open("_input/day22.txt", encoding='utf8') as f:
        for line in f.read().splitlines():
            a, b, c, d, e, f = re.match(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', line).groups()
            #print((int(a), int(b), int(c)), (int(d), int(e), int(f)))
            B.append(((int(a), int(b), int(c)), (int(d), int(e), int(f))))
    return B

def make_points(blocks):
    p = set()
    for b in blocks:
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                for z in range(b[0][2], b[1][2] + 1):
                    if (x, y, z) in p:
                        print("ERROR", (x, y, z))
                    p.add((x, y, z))
    return p

def drop(blocks):
    highest_points = {}
    
    def lowest_block(blocks):
        _y = 1000
        _i = -1
        for i, _ in enumerate(blocks):
            y = min(blocks[i][0][2], blocks[i][1][2])
            if (y < _y):
                _y = y
                _i = i
        return _i, _y

    def highest_point(block):
        h = 0
        for x in range(block[0][0], block[1][0] + 1):
            for y in range(block[0][1], block[1][1] + 1):
                if (x, y) not in highest_points:
                    highest_points[(x, y)] = 0
                h = max(h, highest_points[(x, y)])
        return h

    def update_highest_points(block):
        z = max(block[0][2], block[1][2])
        for x in range(block[0][0], block[1][0] + 1):
            for y in range(block[0][1], block[1][1] + 1):
                if (x, y) not in highest_points:
                    highest_points[(x, y)] = z
                else:
                    highest_points[(x, y)] = max(highest_points[(x, y)], z)

    dropped = []
    count = 0
    while blocks:
        idx, y = lowest_block(blocks)
        b = blocks.pop(idx)
        d = highest_point(b) + 1 - y
        if d < 0:
            count += 1
            b = ((b[0][0], b[0][1], b[0][2] + d), (b[1][0], b[1][1], b[1][2] + d))
        dropped.append(b)
        update_highest_points(b)

    return dropped, count

def insersecting_block(blocks, point):
    for b in blocks:
        if b[0][0] <= point[0] <= b[1][0] and b[0][1] <= point[1] <= b[1][1] and b[0][2] <= point[2] <= b[1][2]:
            return b
    return None

def supporting_blocks(blocks, b):
    supported_by = set()
    low_z = min(b[0][2], b[1][2]) - 1
    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            bl = insersecting_block(blocks, (x, y, low_z))
            if bl != None:
                supported_by.add(bl)
    return supported_by


blocks = parse()
blocks, dropped_count = drop(blocks)

stable_bricks = set()
unstable_bricks = set()

for b in blocks:
    supporting = set()
    low_z = min(b[0][2], b[1][2]) - 1
    high_z = max(b[0][2], b[1][2]) + 1
    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):

            bl = insersecting_block(blocks, (x, y, high_z))
            if bl != None:
                supports = supporting_blocks(blocks, bl)
                if len(supports) == 1:
                    supporting.add(bl)

    if len(supporting) == 0:
        stable_bricks.add(b)
    else: 
        unstable_bricks.add(b)

print('part 1: ', len(stable_bricks))

total_part_2 = 0
print(f'doing part 2 for {len(unstable_bricks)} bricks')
for i, ub in enumerate(unstable_bricks):
    if (i % 100 == 0):
        print(f'{i} done')
    nb = blocks.copy()
    _ = nb.pop(blocks.index(ub))
    _, c = drop(nb)
    total_part_2 += c
print('part 2: ', total_part_2)