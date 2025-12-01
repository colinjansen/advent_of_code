dial = 50
part_1 = 0
part_2 = 0
with open('_input/day1.txt') as f:
    for line in f.readlines():
        line = line.strip()
        move = int(line[1:])

        M = move // 100
        D = dial
        move = move % 100
        
        if line[0] == 'L':
            dial -= move
        else:
            dial += move
        
        if D != 0 and (dial < 0 or dial > 100):
            part_2 += 1
        part_2 += M

        dial = (dial+100) % 100

        if dial == 0:
            part_1 += 1
        
print('part 1: ', part_1)
print('part 2: ', part_2+part_1)