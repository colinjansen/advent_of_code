operations = []
with open('day8.txt', 'r') as file:
    for line in file.readlines():
        operations.append(line.strip().split())

def swap(op):
    if op == 'nop':
        return 'jmp'
    else:
        return 'nop'
    
def scan(swap_index = -1):
    idx = 0
    A = 0
    visited = set()
    while idx < len(operations) and idx not in visited:
        visited.add(idx)
        op, val = operations[idx]
        if idx == swap_index:
            op = swap(op)
        if op == 'acc':
            A += int(val)
            idx += 1
            continue
        if op == 'jmp':
            idx += int(val)
            continue
        if op == 'nop':
            idx += 1
            continue
        print('unkown instruction: ', op, val)
    return A, idx in visited

for i in range(len(operations)):
    op = operations[i][0]
    if op == 'nop' or op == 'jmp':
        a, v = scan(i)
        if v == False:
            print(i, a)
