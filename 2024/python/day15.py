def get_map():
    map = []
    walls = set()
    blocks = set()
    P = (0, 0)
    instruction_set = []
    line_width = None
    with open('2024/_input/day15.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if line_width is None:
                line_width = len(line)
            if len(line) == line_width:
                map.append(list(line))
            if len(line) != line_width:
                instruction_set.append(list(line))

    width = len(map[0])
    height = len(map)
    for r, row in enumerate(map):
        for c, char in enumerate(row):
            if char == '#':
                walls.add((r, c))
            if char == 'O':
                blocks.add((r, c))
            if char == '@':
                P = (r, c)

    return walls, blocks, P, width, height, instruction_set

def show(width, height, walls, blocks, P):
    buffer = ''
    for r in range(height):
        for c in range(width):
            if (r, c) in walls:
                buffer += '#'
            elif (r, c) in blocks:
                a = (r, c)
                if a[1] < blocks[a][0][1]:
                    buffer += '['
                else:
                    buffer += ']'
            elif (r, c) == P:
                buffer += '@'
            else:
                buffer += ' '
        buffer += "\n"
    return buffer.strip()

def get_left_most_blocks(b):
    blocks = set()
    for a, rel in b.items():
        b = rel[0]
        if a[1] < b[1]:
            blocks.add(a)
        else:
            blocks.add(b)
    return blocks

def double_set(s):
    d = {}
    for r, c in s:
        a = (r, c*2)
        b = (r, (c*2)+1)
        d[a] = [b]
        d[b] = [a]
    return d;


def part1():

    walls, blocks, P, width, height, instruction_set = get_map()

    def move_block(P, D):
        NP = (P[0] + D[0], P[1] + D[1])
        if NP in walls:
            return False
        if NP in blocks and not move_block(NP, D):
            return False
        blocks.add(NP)
        blocks.remove(P)
        return True

    def move(D):
        nonlocal P
        NP = (P[0] + D[0], P[1] + D[1])
        if NP in walls:
            return False
        if NP in blocks and not move_block(NP, D):
            return False
        P = NP

    for instructions in instruction_set:
        for instruction in instructions:
            if instruction == '^':
                move((-1, 0))
            if instruction == 'v':
                move((1, 0))
            if instruction == '>':
                move((0, 1))
            if instruction == '<':
                move((0, -1))

    return blocks

def part2():
    w, b, P, width, height, instruction_set = get_map()
    walls = double_set(w)
    blocks = double_set(b)
    width *= 2

    P = (P[0], P[1]*2)

    def move_block(P, D):
        NP = (P[0] + D[0], P[1] + D[1])
        if NP in walls:
            return False
        if NP in blocks and not move_block(NP, D):
            return False
        
        attached = blocks[P][0]
        blocks[NP] = [attached]
        blocks[attached] = [NP]
        del blocks[P]
        return True

    def move_block2(P, D, adds=[], removes=set()):
        A = blocks[P][0]
        NP1 = (P[0] + D[0], P[1] + D[1])
        NP2 = (A[0] + D[0], A[1] + D[1])
        if NP1 in walls or NP2 in walls:
            return False, [], []
        if NP1 in blocks:
            c, a, r = move_block2(NP1, D, adds, removes)
            if not c:
                return False, [], []
            else:
                removes.update(r)
                adds.extend(a)
        if NP2 in blocks:
            c, a, r = move_block2(NP2, D, adds, removes)
            if not c:
                return False, [], []
            else:
                removes.update(r)
                adds.extend(a)
        adds.append((NP1, NP2))
        adds.append((NP2, NP1))
        removes.add(P)
        removes.add(A)
        return True, adds, removes
    
    def move(D):
        nonlocal P
        NP = (P[0] + D[0], P[1] + D[1])
        if NP in walls:
            return
        if D[0] == 0:
            if NP in blocks and not move_block(NP, D):
                return
        else:
            if NP in blocks:
                can, adds, removes = move_block2(NP, D)
                if not can:
                    return
                else:
                    for r in removes:
                        if r in blocks:
                            del blocks[r]
                    for a, b in adds:
                        blocks[a] = [b]
                        blocks[b] = [a]
                return
        P = NP
    
    for instructions in instruction_set:
        for instruction in instructions:
            if instruction == '^':
                move((-1, 0))
            if instruction == 'v':
                move((1, 0))
            if instruction == '>':
                move((0, 1))
            if instruction == '<':
                move((0, -1))
                
    print(show(width, height, walls, blocks, P))
    return blocks

print('part 1', sum( b[0] * 100 + b[1] for b in part1()))
print('part 2', sum( b[0] * 100 + b[1] for b in get_left_most_blocks(part2())))