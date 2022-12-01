

with open('_input/day25.txt', encoding='utf8') as f:
    grid = [list(l.strip()) for l in f.readlines()]

grid_width = len(grid[0])
grid_height = len(grid)
count = 0

def show_grid(grid):
    print('             ')
    for l in range(0, grid_height):
        print(''.join(grid[l]))

def process_east(grid):
    grid_moved = False
    for l in range(0, grid_height):
        i = 0
        while (i < grid_width):
            destination = (i + 1) % grid_width
            if (grid[l][i] == '>' and grid[l][destination] == '.'):
                grid[l][destination] = '>'
                grid[l][i] = '*'
                grid_moved = True
                i += 1
            i += 1
        i = 0
        while (i < grid_width):
            if (grid[l][i] == '*'):
                grid[l][i] = '.'
            i += 1
    return grid_moved

def process_south(line):
    grid_moved = False
    for l in range(0, grid_width):
        i = 0
        while (i < grid_height):
            destination = (i + 1) % grid_height
            if (grid[i][l] == 'v' and grid[destination][l] == '.'):
                grid[destination][l] = 'v'
                grid[i][l] = '*'
                grid_moved = True
                i += 1
            i += 1
        i = 0
        while (i < grid_height):
            if (grid[i][l] == '*'):
                grid[i][l] = '.'
            i += 1

    return grid_moved


while (True):
    me = process_east(grid)
    ms = process_south(grid)
    count += 1
    if (me == False and ms == False):
        print(count)
        break