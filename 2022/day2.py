with open("_input/day2.txt", encoding='utf8') as f:
    lines = f.read().splitlines() 

def part1():
    acc = 0
    for game in lines:
        g = game.split(' ')
        if (g[0] == 'A' and g[1] == 'X'): acc += (1 + 3)  # r v r
        if (g[0] == 'A' and g[1] == 'Y'): acc += (2 + 6)  # r v
        if (g[0] == 'A' and g[1] == 'Z'): acc += (3 + 0)
        if (g[0] == 'B' and g[1] == 'X'): acc += (1 + 0)
        if (g[0] == 'B' and g[1] == 'Y'): acc += (2 + 3)
        if (g[0] == 'B' and g[1] == 'Z'): acc += (3 + 6)
        if (g[0] == 'C' and g[1] == 'X'): acc += (1 + 6)
        if (g[0] == 'C' and g[1] == 'Y'): acc += (2 + 0)
        if (g[0] == 'C' and g[1] == 'Z'): acc += (3 + 3)
    return acc

def part2():
    acc = 0
    for game in lines:
        g = game.split(' ')
        if (g[0] == 'A' and g[1] == 'X'): acc += (3 + 0)  # lose
        if (g[0] == 'A' and g[1] == 'Y'): acc += (1 + 3)  # draw
        if (g[0] == 'A' and g[1] == 'Z'): acc += (2 + 6)  # win
        if (g[0] == 'B' and g[1] == 'X'): acc += (1 + 0)
        if (g[0] == 'B' and g[1] == 'Y'): acc += (2 + 3)
        if (g[0] == 'B' and g[1] == 'Z'): acc += (3 + 6)
        if (g[0] == 'C' and g[1] == 'X'): acc += (2 + 0)
        if (g[0] == 'C' and g[1] == 'Y'): acc += (3 + 3)
        if (g[0] == 'C' and g[1] == 'Z'): acc += (1 + 6)
    return acc

print(part1())
print(part2())