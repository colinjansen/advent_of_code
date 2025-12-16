"""Day 8 solution.

The puzzle gives 3D coordinates for nodes in space. The solution computes the
pairwise Euclidean distance between every pair of nodes, treating nodes at the
same distance as belonging to the same "circuit". Distances are processed in
ascending order so that close nodes are connected first, effectively growing
clusters over time. Once the requested number of distance tiers has been
processed, the answer is the product of the sizes of the three largest
circuits.
"""

from collections import defaultdict


def parse():
    """Parse the puzzle input into a list of coordinate tuples."""
    boxes = []
    with open("_input/day8.txt") as f:
        for line in f.readlines():
            box = map(lambda x: int(x), line.split(','))
            boxes.append(tuple(box))
    return boxes


def distance(box1, box2):
    """Return the Euclidean distance between two coordinate tuples."""
    return sum((a - b) ** 2 for a, b in zip(box1, box2)) ** 0.5


def populate_distances(boxes):
    """Generate a sorted list of all pairwise distances and their node indices."""
    distances = defaultdict(list)
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = distance(boxes[i], boxes[j])
            distances[dist].append((i, j))
    return sorted(distances.items())


def prod(iterable):
    """Compute the product of all numbers in the iterable."""
    result = 1
    for x in iterable:
        result *= x
    return result


def part1(max=5):
    """Return the product of the three largest circuits after `max` distance tiers."""
    L = parse()
    count = 0
    merges = len(L) - 1 # maximum possible merges
    circuits = []

    def get_circuit(idx):
        """Return the circuit containing the index or None if it has not been seen."""
        for c in circuits:
            if idx in c:
                return c
        return None

    def top_lengths(circuits, top=3):
        """Return the product of the sizes of the `top` largest circuits."""
        lengths = sorted([len(c) for c in circuits], reverse=True)[:top]
        return prod(lengths)

    for d in populate_distances(L):
        for a, b in d[1]:
            c_a = get_circuit(a)
            c_b = get_circuit(b)
            # if a and b are in different circuits, merge them
            if c_a and c_b and c_a != c_b:
                c_a.update(c_b)
                circuits.remove(c_b)
                merges -= 1
                continue
            # if a or b is in a circuit, add the other to it
            if c_a and not c_b:
                c_a.add(b)
                merges -= 1
                continue
            if c_b and not c_a:
                c_b.add(a)
                merges -= 1
                continue
            # if neither are in a circuit, create a new one
            if not c_a and not c_b:
                circuits.append(set([a, b]))
                merges -= 1

        count += 1
        if max and count == max:
            return top_lengths(circuits)
        
        if merges == 0:
            a = d[1][0][0]
            b = d[1][0][1]
            return L[a][0] * L[b][0]
        
    return top_lengths(circuits)


print('part 1: ', part1(1000))
print('part 2: ', part1(None))
