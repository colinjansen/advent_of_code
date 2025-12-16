import re
import sys
from collections import defaultdict

def parse():
    shape_idx = -1
    shapes = defaultdict(list)
    spaces = []
    with open("_input/day12.txt") as f:
        for line in f.readlines():
            m = re.match(r"^(\d+):\n$", line)
            if m:
                shape_idx = int(m.group(1))
                continue
            m = re.match(r"^([.#]+)\n$", line)
            if m:
                # Here, '#' denotes an occupied cell for the shape, '.' is empty.
                shapes[shape_idx].append([1 if c == "#" else 0 for c in m.group(1)])
                continue
            m = re.match(r"^(\d+)+x(\d+):(.+)$", line)
            if m:
                spaces.append(
                    (
                        int(m.groups()[0]),
                        int(m.groups()[1]),
                        [int(x) for x in m.groups()[2].strip().split(" ")],
                    )
                )
                continue
    return shapes, spaces

SHAPES, SPACES = parse()


def shape_to_coords(shape):
    coords = []
    for y, row in enumerate(shape):
        for x, v in enumerate(row):
            if v:
                coords.append((x, y))
    return coords


def rotate(coords):
    # Rotate 90 degrees clockwise around origin.
    return [(-y, x) for x, y in coords]


def reflect(coords):
    # Reflect across the vertical axis.
    return [(-x, y) for x, y in coords]


def normalize(coords):
    min_x = min(x for x, _ in coords)
    min_y = min(y for _, y in coords)
    return tuple(sorted([(x - min_x, y - min_y) for x, y in coords]))


def generate_orientations(shape):
    """Return unique rotations and reflections for a shape."""
    seen = set()
    orientations = []
    coords = shape_to_coords(shape)
    for variant in (coords, reflect(coords)):
        current = variant
        for _ in range(4):
            norm = normalize(current)
            if norm not in seen:
                seen.add(norm)
                xs, ys = zip(*norm)
                orientations.append(
                    {
                        "coords": norm,
                        "w": max(xs) + 1,
                        "h": max(ys) + 1,
                    }
                )
            current = rotate(current)
    return orientations


ORIENTATIONS = {idx: generate_orientations(shape) for idx, shape in SHAPES.items()}


def expand_counts(counts):
    """Expand a list of counts per shape id into a list of shape ids (one per piece)."""
    shape_ids = []
    for shape_id, count in enumerate(counts):
        if count <= 0:
            continue
        shape_ids.extend([shape_id] * count)
    return shape_ids


def shape_area(shape_id):
    return len(ORIENTATIONS[shape_id][0]["coords"])


class Node:
    __slots__ = ("left", "right", "up", "down", "column", "row_id")

    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = None


class Column(Node):
    __slots__ = ("name", "size", "primary")

    def __init__(self, name, primary=True):
        super().__init__()
        self.name = name
        self.size = 0
        self.primary = primary


def build_dlx(num_columns, primary_columns, rows):
    columns = [Column(i, primary=(i in primary_columns)) for i in range(num_columns)]
    root = Column("root", primary=True)

    # Horizontal links include all columns so overlaps are enforced.
    prev = root
    for col in columns:
        col.left = prev
        col.right = root
        prev.right = col
        root.left = col
        prev = col

    # Insert row nodes.
    for row_id, row_columns in enumerate(rows):
        first_node = None
        for col_idx in row_columns:
            col = columns[col_idx]
            node = Node()
            node.column = col
            node.row_id = row_id

            # Vertical links.
            node.up = col.up
            node.down = col
            col.up.down = node
            col.up = node
            col.size += 1

            # Horizontal links within the row.
            if first_node is None:
                first_node = node
                node.left = node.right = node
            else:
                node.left = first_node.left
                node.right = first_node
                first_node.left.right = node
                first_node.left = node
    return root, columns


def cover(column):
    column.right.left = column.left
    column.left.right = column.right
    row = column.down
    while row != column:
        node = row.right
        while node != row:
            node.down.up = node.up
            node.up.down = node.down
            node.column.size -= 1
            node = node.right
        row = row.down


def uncover(column):
    row = column.up
    while row != column:
        node = row.left
        while node != row:
            node.column.size += 1
            node.down.up = node
            node.up.down = node
            node = node.left
        row = row.up
    column.right.left = column
    column.left.right = column


def search(root, solution):
    if root.right == root:
        return True

    # Choose the smallest primary column (heuristic).
    column = None
    current = root.right
    while current != root:
        if current.primary:
            if column is None or current.size < column.size:
                column = current
        current = current.right

    # No primary columns left.
    if column is None:
        return True

    if column.size == 0:
        return False

    cover(column)
    row = column.down
    while row != column:
        solution.append(row.row_id)
        node = row.right
        while node != row:
            cover(node.column)
            node = node.right
        if search(root, solution):
            return True
        node = row.left
        while node != row:
            uncover(node.column)
            node = node.left
        solution.pop()
        row = row.down
    uncover(column)
    return False


def build_rows(width, height, shape_ids):
    """Build exact cover rows for shape placements (no implicit empty cells)."""
    rows = []
    placements = []
    grid_cols = width * height

    def cell_index(x, y):
        return y * width + x

    for instance_idx, shape_id in enumerate(shape_ids):
        shape_col = grid_cols + instance_idx
        for orientation in ORIENTATIONS[shape_id]:
            if orientation["w"] > width or orientation["h"] > height:
                continue
            for x_offset in range(width - orientation["w"] + 1):
                for y_offset in range(height - orientation["h"] + 1):
                    cells = [
                        (x_offset + x, y_offset + y) for x, y in orientation["coords"]
                    ]
                    row_columns = [shape_col] + [cell_index(x, y) for x, y in cells]
                    rows.append(row_columns)
                    placements.append(
                        {
                            "instance": instance_idx,
                            "shape": shape_id,
                            "cells": cells,
                    }
                )

    return rows, placements


def build_instance_placements(width, height, shape_ids):
    """Precompute bitmask placements for each shape instance."""
    placements = []

    def cell_bit(x, y):
        return 1 << (y * width + x)

    for instance_idx, shape_id in enumerate(shape_ids):
        options = []
        for orientation in ORIENTATIONS[shape_id]:
            if orientation["w"] > width or orientation["h"] > height:
                continue
            for x_offset in range(width - orientation["w"] + 1):
                for y_offset in range(height - orientation["h"] + 1):
                    cells = [
                        (x_offset + x, y_offset + y) for x, y in orientation["coords"]
                    ]
                    mask = 0
                    for x, y in cells:
                        mask |= cell_bit(x, y)
                    options.append(
                        {
                            "mask": mask,
                            "cells": cells,
                            "instance": instance_idx,
                            "shape": shape_id,
                        }
                    )
        placements.append(options)
    return placements


def solve_with_bitmasks(width, height, shape_ids):
    # Avoid recursion depth issues on larger searches.
    sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))
    from functools import lru_cache

    placements = build_instance_placements(width, height, shape_ids)
    if any(len(opts) == 0 for opts in placements):
        return False, []

    # Split masks and cells for faster filtering.
    placement_masks = [[opt["mask"] for opt in opts] for opts in placements]
    placement_cells = [[opt["cells"] for opt in opts] for opts in placements]
    if any(len(opts) == 0 for opts in placement_masks):
        return False, []

    n = len(shape_ids)
    full_mask = (1 << n) - 1

    @lru_cache(maxsize=None)
    def dfs(occupied, remaining_mask):
        if remaining_mask == 0:
            return True

        # Pick the instance with the fewest valid options.
        best_inst = None
        best_opts = None
        m = remaining_mask
        idx = 0
        while m:
            if m & 1:
                valid_idxs = [
                    i for i, mask in enumerate(placement_masks[idx]) if mask & occupied == 0
                ]
                if not valid_idxs:
                    return False
                if best_opts is None or len(valid_idxs) < len(best_opts):
                    best_opts = valid_idxs
                    best_inst = idx
                    if len(best_opts) == 1:
                        break
            m >>= 1
            idx += 1

        next_mask = remaining_mask & ~(1 << best_inst)
        masks = placement_masks[best_inst]
        for opt_idx in best_opts:
            if dfs(occupied | masks[opt_idx], next_mask):
                return True
        return False

    if not dfs(0, full_mask):
        return False, []

    # Reconstruct one layout (deterministically choose the first valid option per step).
    solution_idx = [None] * n
    occupied = 0
    remaining_mask = full_mask
    while remaining_mask:
        best_inst = None
        best_opts = None
        m = remaining_mask
        idx = 0
        while m:
            if m & 1:
                valid_idxs = [
                    i for i, mask in enumerate(placement_masks[idx]) if mask & occupied == 0
                ]
                if best_opts is None or len(valid_idxs) < len(best_opts):
                    best_opts = valid_idxs
                    best_inst = idx
                    if len(best_opts) == 1:
                        break
            m >>= 1
            idx += 1
        chosen = None
        next_mask = remaining_mask & ~(1 << best_inst)
        masks = placement_masks[best_inst]
        for opt_idx in best_opts:
            if dfs(occupied | masks[opt_idx], next_mask):
                chosen = opt_idx
                break
        solution_idx[best_inst] = chosen
        occupied |= masks[chosen]
        remaining_mask = next_mask

    grid = [["." for _ in range(width)] for _ in range(height)]
    for inst, opt_idx in enumerate(solution_idx):
        marker = chr(ord("A") + inst % 26)
        for x, y in placement_cells[inst][opt_idx]:
            grid[y][x] = marker
    return True, ["".join(row) for row in grid]


def solve_space(width, height, shape_counts):
    """Return whether the required counts of each shape can fit into the space."""
    shape_ids = expand_counts(shape_counts)
    if not shape_ids:
        return False, []

    total_area = sum(shape_area(s_id) for s_id in shape_ids)
    # Require shapes to fit but allow empty cells.
    if total_area > width * height:
        return False, []

    # Use the fast bitmask solver when the board fits in 64 bits.
    if width * height <= 64:
        fits, layout = solve_with_bitmasks(width, height, shape_ids)
        return fits, layout

    # For larger boards, use DLX with shape instance columns as primary and
    # grid cells as secondary (to forbid overlaps without requiring coverage).
    rows, placements = build_rows(width, height, shape_ids)
    if not rows:
        return False, []

    grid_cols = width * height
    total_cols = grid_cols + len(shape_ids)
    primary_cols = list(range(grid_cols, total_cols))
    root, _ = build_dlx(total_cols, primary_cols, rows)
    solution = []
    if not search(root, solution):
        return False, []

    grid = [["." for _ in range(width)] for _ in range(height)]
    for row_id in solution:
        placement = placements[row_id]
        marker = chr(ord("A") + placement["instance"] % 26)
        for x, y in placement["cells"]:
            grid[y][x] = marker
    return True, ["".join(row) for row in grid]


total_true = 0
for space in SPACES:
    width, height, shape_counts = space
    fits, layout = solve_space(width, height, shape_counts)
    if fits:
        total_true += 1

print('part 1:', total_true)
