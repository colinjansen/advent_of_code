def build_map():
    M = []
    with open("_input/day18.txt") as f:
        for line in f.read().splitlines():
            M.append(list(line.strip()))
    return M

def show(M):
    for row in M:
        print(row)

def animate(a):
    def count_neighbors(r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(a) and 0 <= nc < len(a[0]) and a[nr][nc] == '#':
                    count += 1
        return count
    
    b = []
    for r, row in enumerate(a):
        b.append(['.'] * len(row))
        for c, char in enumerate(row):
            n = count_neighbors(r, c)
            if char == '#':
                b[r][c] = '#' if n in [2, 3] else '.'
            else:
                b[r][c] = '#' if n == 3 else '.'

    return b

def count_lights(M):
    return sum(row.count('#') for row in M)

def part_1(M):
    for _ in range(100):
        M = animate(M)
    print(f"Number of lights on: {count_lights(M)}")

def part_2(M):
    def set_corners_on(M):
        M[0][0] = '#'
        M[0][-1] = '#'
        M[-1][0] = '#'
        M[-1][-1] = '#'
        return M
    M = set_corners_on(M)
    for _ in range(100):
        M = animate(M)
        M = set_corners_on(M)
    print(f"Number of lights on: {count_lights(M)}")

part_1(build_map())
part_2(build_map())