from itertools import combinations
from collections import defaultdict
import networkx as nx

C = defaultdict(set)
G = nx.Graph()
with open('2024/_input/day23.txt') as f:
    for line in f.readlines():
        a, b = line.strip().split('-')
        G.add_edge(a, b)
        C[a].add(b)
        C[b].add(a)

def part1():
    triangles = set()
    for a in C:
        for b in C[a]:
            for c in C[b]:
                if c != a and a in C[c]:
                    if 't' == a[0] or 't' == b[0] or 't' == c[0]:
                        triangles.add(tuple(sorted([a, b, c])))
    return len(triangles)

def part2():
    cliques = nx.find_cliques(G)
    cliques = sorted(cliques, key=len, reverse=True)
    biggest = cliques[0]
    return ','.join(sorted(biggest))

print(part1())
print(part2())