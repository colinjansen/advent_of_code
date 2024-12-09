from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
import re

with open('2024/_input/day9.txt') as f:
    line = f.readline().strip()

def checksum(id, offset, size):
    t = 0
    for i in range(size):
        t += (offset + i) * id
    return t

def part1(line):
    disk = []
    mode = 1
    id = 0
    for n in line:
        n = int(n)
        if mode == 1:
            for i in range(n):
                disk.append(id)
            id += 1
        if mode == 0:
            for i in range(n):
                disk.append(None)
        mode = 1 - mode

    i = 0
    j = len(disk) - 1
    while i < j:
        # find empty slot≈
        while i < len(disk) and disk[i] != None:
            i += 1
        # find non-empty slot
        while disk[j] == None:
            j -= 1
        if i >= j:
            break
        disk[i] = disk[j]
        disk[j] = None
    disk = list(filter(lambda x: x != None, disk))

    t = 0
    for i, d in enumerate(disk):
        t += i*d
    print(t)

def part2(line):
    def get_disk():
        disk = {}
        free = []
        mode = 1
        id = 0
        offset = 0
        for size in line:
            size = int(size)
            if mode == 1:
                disk[id] = {
                    'offset': offset,
                    'size': size
                }
                id += 1
            if mode == 0:
                free.append({
                    'offset': offset,
                    'size': size
                })
            offset += size
            mode = 1 - mode
        return disk, free
    
    disk, free = get_disk()
    
    for key in sorted(disk.keys(), reverse=True):
        file = disk[key]
        for slot in free:
            if file['offset'] > slot['offset'] and slot['size'] >= file['size']:
                file['offset'] = slot['offset']
                slot['offset'] += file['size']
                slot['size'] -= file['size']
                break

    disk_sum = sum([checksum(id, file['offset'], file['size']) for id, file in disk.items()])
    print(disk_sum)

part1(line)
part2(line)