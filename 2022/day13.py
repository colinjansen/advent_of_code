import ast

with open("_input/day13.txt", encoding='utf8') as f:
    lines = f.read().splitlines()


class Packet:
    def __init__(self):
        self._1 = []
        self._2 = []


def get_packet_pairs_for_part1():
    packets = []
    for i in range(0, len(lines), 3):
        packet = Packet()
        packet._1 = ast.literal_eval(lines[i])
        packet._2 = ast.literal_eval(lines[i + 1])
        packets.append(packet)
    return packets


def get_packets_for_part2():
    packets = [
        [[2]],
        [[6]]
    ]
    for i in range(0, len(lines), 3):
        packets.append(ast.literal_eval(lines[i]))
        packets.append(ast.literal_eval(lines[i + 1]))
    return packets


def compare_ints(a: int, b: int):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def compare(list1: list, list2: list):
    for i in range(0, max(len(list1), len(list2))):
        if len(list1) <= i:
            return 1
        a = list1[i]
        if len(list2) <= i:
            return -1
        b = list2[i]
        if type(a) is int and type(b) is int:
            r = compare_ints(a, b)
            if r == 1:
                return -1
            if r == -1:
                return 1
            continue
        if type(a) is int:
            a = [a]
        if type(b) is int:
            b = [b]
        r = compare(a, b)
        if r != 0:
            return r
    return 0


def sort(packets):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(1, len(packets)):
            result = compare(packets[i-1], packets[i])
            if (result == -1):
                t = packets[i]
                packets[i] = packets[i-1]
                packets[i-1] = t
                sorted = False


def get_packet_index(p, packets):
    for i in range(0, len(packets)):
        if packets[i] == p:
            return i
    return -1


def part1():
    ordered = []
    pairs_for_part1 = get_packet_pairs_for_part1()
    for i in range(0, len(pairs_for_part1)):
        result = compare(pairs_for_part1[i]._1, pairs_for_part1[i]._2)
        if result == 1:
            ordered.append(i + 1)
    return sum(ordered)


def part2():
    packets = get_packets_for_part2()
    sort(packets)
    a = get_packet_index([[2]], packets) + 1
    b = get_packet_index([[6]], packets) + 1
    return a * b


print(f'part 1 is {part1()} part 2 is {part2()}')
