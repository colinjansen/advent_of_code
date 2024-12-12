import re

def parse_input():
    with open('day6.txt', 'r') as file:
        ans = []
        data = []
        for line in file.readlines():
            if line == '\n':
                ans.append(data)
                data = []
            else:
                data.append(line.strip())
        ans.append(data)
    return ans

ans = parse_input()

def part_1(ans):
    G = {}
    for i, group in enumerate(ans):
        G[i] = set()
        for perons in group:
            G[i].update(perons)
        
    return sum( [len(s) for s in G.values()] )

def part_2(ans):
    G = {}
    for i, group in enumerate(ans):
        G[i] = set('abcdefghijklmnopqrstuvwxyz')
        for answers in group:
            G[i] &= set(answers)
        
    return sum( [len(s) for s in G.values()] )

print(part_1(ans))
print(part_2(ans))

