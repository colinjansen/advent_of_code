with open("_input/day11.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

# empty rows
ER = [i for i, l in enumerate(lines) if all(c == '.' for c in l)]
# empty columns
EC = [i for i in range(len(lines[0])) if all(l[i] == '.' for l in lines)]
# galaxies
G = [(r, c) for r, _ in enumerate(lines) for c, _ in enumerate(lines[r]) if lines[r][c] == '#']

# get the shortest path from one galaxy to another
def traverse(i, j, gap=2):
    (l, r) = (min(G[i][1], G[j][1]), max(G[i][1], G[j][1]))
    (u, d) = (min(G[i][0], G[j][0]), max(G[i][0], G[j][0]))
    Y = sum(1 if y not in ER else gap for y in range(u + 1, d + 1))
    X = sum(1 if x not in EC else gap for x in range(l + 1, r + 1))
    return Y + X

# sum the shortest paths for all the galaxies
def sum_paths(gap=2):
    return sum([traverse(i, j, gap) for i in range(len(G)) for j in range(i + 1, len(G))])
               
print(f'part 1 {sum_paths(2)} part 2 {sum_paths(1_000_000)}')