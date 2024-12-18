from computer import Computer

def get_path():
    with open('2019/_input/day17.txt') as f:
        program = f.readline().strip()

    def handle_input():
        return 0

    buffer = ''
    def handle_output(v):
        nonlocal buffer
        buffer += chr(v)

    c = Computer(program)
    c.go(input_function=handle_input, output_function=handle_output)

    path = set()
    position = None
    for r, line in enumerate(buffer.strip().split('\n')):
        for c, char in enumerate(line):
            if char == '^':
                position = (r, c)
            if char == '#':
                path.add((r, c))

    return path, position

def is_intersection(p, path):
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        if (p[0] + dr, p[1] + dc) not in path:
            return False
    return True

def part1():
    path, _ = get_path() 
    result = 0
    for p in path:
        if is_intersection(p, path):
            result += p[0] * p[1]
    return result

def turn(direction, position, path):
    if direction == (-1, 0):
        if (position[0], position[1] - 1) in path:
            return (0, -1), 'L'
        if (position[0], position[1] + 1) in path:
            return (0, 1), 'R'
    if direction == (1, 0):
        if (position[0], position[1] + 1) in path:
            return (0, 1), 'L'
        if (position[0], position[1] - 1) in path:
            return (0, -1), 'R'
    if direction == (0, -1):
        if (position[0] + 1, position[1]) in path:
            return (1, 0), 'L'
        if (position[0] - 1, position[1]) in path:
            return (-1, 0), 'R'
    if direction == (0, 1):
        if (position[0] - 1, position[1]) in path:
            return (-1, 0), 'L'
        if (position[0] + 1, position[1]) in path:
            return (1, 0), 'R'
    return None, None
    
def get_directions():
    path, p = get_path() 
    d = (-1, 0)
    buffer = []
    while True:
        length = 0
        while (p[0] + d[0], p[1] + d[1]) in path:
            p = (p[0] + d[0], p[1] + d[1])
            length += 1
        if length:
            buffer.append(str(length))
        d, D = turn(d, p, path)
        if D == None:
            break
        buffer.append(D)
    return buffer

def find_largest_repeating_subarrays(arr, min_length=2):
    """
    Find the largest repeating subarrays in the input array.
    
    Args:
        arr: Input array/list
        min_length: Minimum length of subarrays to consider (default: 2)
        
    Returns:
        List of tuples, each containing (subarray, list of start indices)
    """
    n = len(arr)
    # Dictionary to store all found subarrays and their occurrences
    subarrays = {}
    
    # Try all possible subarray lengths, from longest to shortest
    for length in range(n-min_length+1, min_length-1, -1):
        # Try all possible starting positions for this length
        for start in range(n - length + 1):
            # Extract the subarray
            subarray = tuple(arr[start:start + length])
            
            # If we haven't seen this subarray before
            if subarray not in subarrays:
                # Find all occurrences
                occurrences = []
                for i in range(n - length + 1):
                    if tuple(arr[i:i + length]) == subarray:
                        occurrences.append(i)
                
                # If we found multiple occurrences
                if len(occurrences) > 1:
                    subarrays[subarray] = occurrences
                    # Since we're going from longest to shortest,
                    # we can return as soon as we find repeating subarrays
                    return [(list(subarray), occurrences)]
    
    return []

print('part 1:', part1())
directions = get_directions()

# [
#  'R', '4', 'L', '10', 'L', '10',             A
#  'L', '8', 'R', '12', 'R', '10', 'R', '4',   B
#  'R', '4', 'L', '10', 'L', '10',             A
#  'L', '8', 'R', '12', 'R', '10', 'R', '4',   B
#  'R', '4', 'L', '10', 'L', '10',             A
#  'L', '8', 'L', '8', 'R', '10', 'R', '4',    C
#  'L', '8', 'R', '12', 'R', '10', 'R', '4',   B
#  'L', '8', 'L', '8', 'R', '10', 'R', '4',    C
#  'R', '4', 'L', '10', 'L', '10',             A
#  'L', '8', 'L', '8', 'R', '10', 'R', '4'     C
#  ]

with open('2019/_input/day17.txt') as f:
    program = f.readline().strip()

c = Computer(program)
c.codes[0] = 2

IN = [ord(c) for c in 'A,B,A,B,A,C,B,C,A,C']+[10]
IN.extend([ord(c) for c in 'R,4,L,10,L,10']+[10])
IN.extend([ord(c) for c in 'L,8,R,12,R,10,R,4']+[10])
IN.extend([ord(c) for c in 'L,8,L,8,R,10,R,4']+[10])
IN.extend([110, 10])

c.go(input_function=lambda: IN.pop(0), output_function=lambda v: print(v))