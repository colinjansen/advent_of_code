import re
from sys import maxsize
from itertools import permutations
from functools import reduce


lines = open('_input/day9.txt', 'r').readlines()


def get_adjacency_matrix(lines):
    #
    # turn the input into a matrix of node adjacencies
    #
    matrix = []     # adjacency matrix
    dist_list = {}  # map (p1, p2) to distance
    places = {}     # map place names to ids

    def get_place_id(name):
        if name not in places:
            places[name] = len(places)
        return places[name]

    for line in lines:
        m = re.match('(\w+) to (\w+) = (\d+)', line)
        p1 = get_place_id(m.group(1))
        p2 = get_place_id(m.group(2))
        dist_list[(p1, p2)] = int(m.group(3))

    for i in (range(len(places))):
        matrix.append([])
        for j in (range(len(places))):
            if i == j:
                matrix[i].append(0)
                continue
            matrix[i].append(dist_list[tuple(sorted([i, j]))])

    return matrix


def tsp_from_node(matrix, compare_from_index, comparison_function, start_value):
    # create a list of all nodes except the one we're starting from
    vertex = [i for i in range(len(matrix)) if i != compare_from_index]
    # calculate the cost of a permutation
    def cost(permutation):
        current = 0
        idx = compare_from_index
        for i in permutation:
            current += matrix[idx][i]
            idx = i
        return current
    # return the best cost from all permutations
    return reduce(lambda b, p: comparison_function(b, cost(p)), permutations(vertex), start_value)


def tsp(matrix, comparison_function, start_value):
    # calculate the cost of the shortest path from all possible nodes
    return reduce(lambda best, idx: comparison_function(best, tsp_from_node(matrix, idx, comparison_function, start_value)), range(len(matrix)), start_value)


matrix = get_adjacency_matrix(lines)

print(f'part 1: {tsp(matrix, min, maxsize)}')
print(f'part 2: {tsp(matrix, max, 0)}')
