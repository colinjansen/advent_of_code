with open("_input/day2.txt", encoding='utf8') as f:
    lines = f.read().splitlines() 

p1 = { 'A': 0, 'B': -1, 'C': 1, 'X': 1, 'Y': 2, 'Z': 3 }
p2 = { 'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6 }

def part1():
    acc = 0
    for game in lines:
        g = game.split(' ')
        a = p1[g[0]]
        x = p1[g[1]]
        acc += x + (3 * (x + a) % 9)
    return acc

def part2():
    acc = 0
    for game in lines:
        g = game.split(' ')
        a = p1[g[0]]
        x = p1[g[1]]
 
        acc += x + (3 * (x + a ) % 9)

        # x + ( (x + 9) % 9 )                                        a x

        # if (g[0] == 'A' and g[1] == 'X'): acc += (3 + 0)  # lose   1 0 = 3
        # if (g[0] == 'A' and g[1] == 'Y'): acc += (1 + 3)  # draw   1 3 = 1
        # if (g[0] == 'A' and g[1] == 'Z'): acc += (2 + 6)  # win    1 6 = 2

        # if (g[0] == 'B' and g[1] == 'X'): acc += (1 + 0)           2 0 = 1
        # if (g[0] == 'B' and g[1] == 'Y'): acc += (2 + 3)           2 3 = 2
        # if (g[0] == 'B' and g[1] == 'Z'): acc += (3 + 6)           2 6 = 3

        # if (g[0] == 'C' and g[1] == 'X'): acc += (2 + 0)           3 0 = 2
        # if (g[0] == 'C' and g[1] == 'Y'): acc += (3 + 3)           3 3 = 3
        # if (g[0] == 'C' and g[1] == 'Z'): acc += (1 + 6)           3 6 = 1

    return acc

print( (6 + 9) % 9 )

print(part1()) # 15632
print(part2()) # 14416