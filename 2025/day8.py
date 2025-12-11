from collections import defaultdict


def parse():
    boxes = []
    with open("_input/day8.txt") as f:
        for line in f.readlines():
            box = map(lambda x: int(x), line.split(','))
            boxes.append(tuple(box))
    return boxes

def distance(box1, box2):
    return sum((a - b) ** 2 for a, b in zip(box1, box2)) ** 0.5

def populate_distances(boxes):
    distances = defaultdict(list)
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = distance(boxes[i], boxes[j])
            distances[dist].append((i, j))
    return sorted(distances.items())

def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result

def part1(max=5):
    count = 0
    cicuits = []

    def get_circuit(idx):
        for c in cicuits:
            if idx in c:
                return c
        return None
    
    def top_lengths(circuits, top=3):
        lengths = sorted([len(c) for c in circuits], reverse=True)[:top]
        return prod(lengths)

    for d in populate_distances(parse()):
        for a, b in d[1]:
            c_a = get_circuit(a)
            c_b = get_circuit(b)
            # if a and b are in different circuits, merge them
            if c_a and c_b and c_a != c_b:
                c_a.update(c_b)
                cicuits.remove(c_b)
                continue
            # if a or b is in a circuit, add the other to it
            if c_a and not c_b:
                c_a.add(b)
                continue
            if c_b and not c_a:
                c_b.add(a)
                continue
            # if neither are in a circuit, create a new one
            if not c_a and not c_b:
                cicuits.append(set([a, b]))
        
        #print(d, cicuits)
        count += 1
        if count == max:
            return top_lengths(cicuits)
        
    return top_lengths(cicuits)

print('part 1: ', part1(1000))