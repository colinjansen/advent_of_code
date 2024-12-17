from collections import deque
from typing import Dict, List, Set, Tuple
import heapq


all_paths = set()
start, end = None, None
with open('2024/_input/day16.txt') as f:
    width = 0
    height = 0
    for r, line in enumerate(f.readlines()):
        height = r
        for c, char in enumerate(line):
            width = len(line.strip())
            if char in '.ES':
                all_paths.add((r, c))
            if char == 'S':
                start = (r, c)
            if char == 'E':
                end = (r, c)

def find_min_cost(path, start, end):
    r, c = start
    Q = deque([(r, c, (0, 1), 0)])
    visited = {}
    while Q:
        r, c, d, s = Q.popleft()
        if (r, c) in visited and visited[(r, c)] < s:
            continue
        visited[(r, c)] = s
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c, new_d = r + dr, c + dc, (dr, dc)
            if (new_r, new_c) in path:
                Q.append((new_r, new_c, new_d, s + 1 if new_d == d else s + 1001))
    return visited[end]

def get_best_paths(all_path, start, target, max_cost):
    r, c = start
    good_paths = {}
    Q = deque([(r, c, (0, 1), 0, [start])])
    while Q:
        r, c, direction, cost, current_path = Q.popleft()
        if cost > max_cost:
            continue
        if (r, c) == target:
            if cost not in good_paths:
                good_paths[cost] = []
            good_paths[cost].append(current_path)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c, new_d = r + dr, c + dc, (dr, dc)
            if (new_r, new_c) in all_path and (new_r, new_c) not in current_path:
                Q.append((new_r, new_c, new_d, cost + 1 if new_d == direction else cost + 1001, current_path + [(new_r, new_c)]))
    return good_paths

from typing import Dict, List, Set, Tuple, TypeVar

T = TypeVar('T')

def get_best_paths_2(
    all_paths: Set[Tuple[int, int]], 
    start: Tuple[int, int], 
    target: Tuple[int, int], 
    max_cost: int,
    callback=None
) -> Dict[int, List[List[Tuple[int, int]]]]:
    """
    Find all paths from start to target with cost <= max_cost.
    
    Args:
        all_paths: Set of valid coordinates
        start: Starting position (row, col)
        target: Target position (row, col)
        max_cost: Maximum allowed cost
        
    Returns:
        Dictionary mapping costs to lists of valid paths
    """
    # Pre-compute directions and their costs
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    good_paths: Dict[int, List[List[Tuple[int, int]]]] = {}
    
    # Use frozen sets for O(1) lookup of visited positions
    visited = set()
    
    def get_move_cost(curr_dir: Tuple[int, int], new_dir: Tuple[int, int]) -> int:
        return 1 if curr_dir == new_dir else 1001
    
    Q = deque([(
        start[0],           # row
        start[1],          # col
        (0, 1),           # initial direction
        0,                # cost
        [start],          # path
        frozenset([start])  # visited positions
    )])
    
    while Q:
        r, c, direction, cost, current_path, visited_positions = Q.popleft()
        
        # Early termination if cost exceeds max
        if cost > max_cost:
            continue
            
        if (r, c) == target:
            good_paths.setdefault(cost, []).append(current_path)
            if callback:
                callback(current_path)
            continue
            
        # Check all possible directions
        for new_d in DIRECTIONS:
            new_r, new_c = r + new_d[0], c + new_d[1]
            new_pos = (new_r, new_c)
            
            # Combined validation check
            if (new_pos in all_paths and 
                new_pos not in visited_positions):
                
                new_cost = cost + get_move_cost(direction, new_d)
                if new_cost <= max_cost:  # Prune paths that would exceed max_cost
                    new_path = current_path + [new_pos]
                    new_visited = visited_positions | {new_pos}
                    
                    Q.append((
                        new_r, 
                        new_c, 
                        new_d,
                        new_cost,
                        new_path,
                        new_visited
                    ))
    
    return good_paths

def get_best_paths_optimized(path: Set[Tuple[int, int]], start: Tuple[int, int], 
                           target: Tuple[int, int], max_cost: int) -> Dict[int, List[List[Tuple[int, int]]]]:
    """
    Finds all valid paths from start to target with cost <= max_cost.
    Maintains original functionality while improving performance through:
    1. Set-based path lookups
    2. Reduced tuple packing/unpacking
    3. Early termination for invalid paths
    """
    r, c = start
    good_paths: Dict[int, List[List[Tuple[int, int]]]] = {}
    
    # Convert path to set if it isn't already
    path_set = set(path)
    
    # Use deque for FIFO queue behavior to maintain breadth-first search
    Q = deque([(r, c, (0, 1), 0, [start])])
    
    # Directions as constants to avoid recreation
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while Q:
        r, c, direction, cost, current_path = Q.popleft()
        
        if cost > max_cost:
            continue
            
        if (r, c) == target:
            if cost not in good_paths:
                good_paths[cost] = []
            good_paths[cost].append(current_path)
            
        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            new_pos = (new_r, new_c)
            new_d = (dr, dc)
            
            # Quick reject conditions
            if new_pos not in path_set:
                continue
            if new_pos in current_path:
                continue
                
            # Calculate new cost
            new_cost = cost + (1 if new_d == direction else 1001)
            if new_cost > max_cost:
                continue
                
            # Add new state to queue
            Q.append((
                new_r,
                new_c,
                new_d,
                new_cost,
                current_path + [new_pos]
            ))
    
    return good_paths

best = set()
def add_path(path):
    for p in path:
        best.add(p)
    print(f'adding path: {len(best)}')

min_cost = find_min_cost(all_paths, start, end)
paths = get_best_paths_2(all_paths, start, end, min_cost, add_path)

lowest_cost = min(paths.keys())
for path in paths[lowest_cost]:
    for p in path:
        best.add(p)

for r in range(height + 1):
    for c in range(width + 1):
        if (r, c) in all_paths:
            if (r, c) in best:
                print('O', end='')
            else:
                print('.', end='')
        else:
            print(' ', end='')
    print()

print('part 1:', lowest_cost)
print('part 2:', len(best))