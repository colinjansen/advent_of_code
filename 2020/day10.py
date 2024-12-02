from collections import defaultdict

A = []
with open('day10.txt', 'r') as file:
    for line in file.readlines():
        A.append(int(line))
A = sorted(A)
A.append(max(A)+3)
V = 0
J = defaultdict(int)
for a in A:
    J[a-V] += 1
    V = a
print(J, J[1]*J[3])