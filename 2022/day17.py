import time

with open('_input/day17.txt') as f:
    input = f.read()


input_length = len(input)
shapes = [
    [60],             # horizontal line
    [16, 56, 16],     # plus shape
    [56, 8, 8],       # L shape
    [32, 32, 32, 32],  # vertical line
    [48, 48],         # square
]
grid = {
    2: 0,
    1: 0,
    0: 0,
    -1: 254
}
highest_rock = -1
shape_p = 0
input_p = 0


def get_push():
    """
    get the direction to move the shape
    """
    global input_p, shape_p
    c = input[input_p]
    input_p = (input_p + 1) % input_length
    return 1 if c == '>' else -1


def get_shape(insert_at: int) -> dict:
    """
    get the next direction to 'push' in
    """
    global shape_p
    s = {insert_at + i: v for i, v in enumerate([*shapes[shape_p]])}
    shape_p = (shape_p + 1) % len(shapes)
    return s


def add_shape_to_grid(grid: dict[int, int], shape: dict[int, int], top: int) -> tuple[int, dict[int, int]]:
    """
    adds the shape to the 'rocks' of the grid
    """
    for k in shape:
        grid[k] = grid[k] | shape[k]
    return (max(top, list(shape)[-1:][0]), grid)


def draw_grid(grid: dict[int, int], shape: dict[int, int] = None, tail: int = None):
    """
    draw a representation of the current state of the graph with
    an optional shape
    """
    g = dict(sorted(grid.items(), reverse=True))
    if shape != None:
        for k in shape:
            g[k] = (g[k] if k in g else 0) | shape[k]
    for k in g:
        if tail > 0:
            tail -= 1
        print(f'{k+1: >8} : 1{bin(g[k] + 1)[2:]:0>8}')
        if tail == 0:
            return


def move(grid: dict[int, int], shape: dict[int, int]) -> dict[int, int]:
    """
    try to move the shape from side to side
    """
    shift = get_push()
    if shift == -1:
        s = {k: shape[k] << 1 for k in shape}
        for k in shape:
            if s[k] & (256 | grid[k]):
                return shape
        return s
    if shift == 1:
        s = {k: shape[k] >> 1 for k in shape}
        for k in shape:
            if s[k] & (1 | grid[k]):
                return shape
        return s
    return shape


def drop(grid: dict[int, int], shape: dict[int, int]) -> tuple[bool, dict[int, int]]:
    """
    try to drop the shape down one row
    """
    dropped = {k - 1: shape[k] for k in shape}
    for k in dropped:
        if dropped[k] & grid[k] > 0:
            return False, shape
    return True, dropped


def run_simulation(t: int) -> int:
    global grid, highest_rock, shape_p, input_p
    """
    for each 1730 iterations we gain 2644 blocks of height except
    for the first iteration that seems to be 15 higher than the
    others
    """

    # set out state to the starting positions
    grid = { 2: 0, 1: 0, 0: 0, -1: 254 }
    highest_rock = -1
    shape_p = 0
    input_p = 0

    iterations_per_loop = 1730
    height_gain_per_iteration = 2644
    loops = t // iterations_per_loop
    starting_height = (height_gain_per_iteration * loops) + 15
    remaining_iterations = t - (iterations_per_loop * loops)

    for _ in range(iterations_per_loop + remaining_iterations):

        shape = get_shape(highest_rock + 4)
        for k in shape:
            grid[k] = 0

        while True:
            #
            # push the shape
            #
            shape = move(grid, shape)
            #
            # drop the shape
            #
            dropped, shape = drop(grid, shape)
            if (dropped == False):
                break

        highest_rock, grid = add_shape_to_grid(grid, shape, highest_rock)

    return starting_height + (highest_rock - 2659) + 1


start = time.time()
print(f'part 1: {run_simulation(2022)} @ {round(1000 * (time.time() - start), 3)}ms')
print(f'part 2: {run_simulation(1_000_000_000_000)} @ {round(1000 * (time.time() - start), 3)}ms')