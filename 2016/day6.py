from collections import Counter


A = [[] for _ in range(8)]

with (open("_input/day6.txt") as f):
    for line in f.readlines():
        for e, c in enumerate(line.strip()):
            A[e].append(c)
print([Counter(C).most_common(1)[-1][0] for C in A])
print([Counter(C).most_common(26)[-1][0] for C in A])
    