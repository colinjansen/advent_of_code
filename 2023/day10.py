with open("_input/day10.txt", encoding="utf8") as f:
    L = f.read().splitlines()

VISITED = set()

START = next(
    ((j, i) for i, r in enumerate(L) for j, c in enumerate(r) if c == "S"), None
)


def move_along_pipe(coordinate):
    VISITED.add(coordinate)
    c, r = coordinate
    # go up
    if (
        (c, r - 1) not in VISITED
        and r > 0
        and L[r][c] in ["S", "|", "L", "J"]
        and L[r - 1][c] in ["|", "F", "7"]
    ):
        return (c, r - 1)
    # go down
    if (
        (c, r + 1) not in VISITED
        and r < len(L)
        and L[r][c] in ["S", "|", "F", "7"]
        and L[r + 1][c] in ["|", "L", "J"]
    ):
        return (c, r + 1)
    # go right
    if (
        (c + 1, r) not in VISITED
        and c < len(L[0])
        and L[r][c] in ["S", "-", "F", "L"]
        and L[r][c + 1] in ["-", "7", "J"]
    ):
        return (c + 1, r)
    # go left
    if (
        (c - 1, r) not in VISITED
        and c > 0
        and L[r][c] in ["S", "-", "J", "7"]
        and L[r][c - 1] in ["-", "F", "L"]
    ):
        return (c - 1, r)
    return False


def count_intersections_with_pipe(r, c):
    intersections = 0
    while r > 0 and c > 0:
        # moving up and left
        r -= 1
        c -= 1
        if (c, r) in VISITED:
            # these corners count as two line intersections
            if L[r][c] in ["L", "7"]:
                intersections += 2
            else:
                intersections += 1
    return intersections


# trace the pipe
v = START
while v is not False:
    v = move_along_pipe(v)

# half the length of the pipe
part_1 = len(VISITED) // 2

# count the contained blocks
part_2 = sum(
    1
    for r, R in enumerate(L)
    for c, C in enumerate(R)
    if (c, r) not in VISITED and count_intersections_with_pipe(r, c) % 2 == 1
)

print(f"part 1: {part_1} part 2: {part_2}")
