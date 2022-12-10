import re

with open("_input/day7.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

class Directory:
    def __init__(self):
        self.name = '/'
        self.directories = []
        self.files = []
        self.parent = self
        self.size = 0
    def show(self, level = ''):
        print(f'{level}[{self.name}]')
        for f in self.files:
            f.show(level+ '  ')
        for d in self.directories:
            d.show(level + '  ')
    def getChildDirectory(self, name):
        for entry in self.directories:
            if (name == entry.name):
                return entry
        return self
    def getDirectorySizes(self, sizes = []):
        size = 0
        for f in self.files:
            size += f.size
        for d in self.directories:
            size += d.getDirectorySizes(sizes)
        self.size = size
        sizes.append(size)
        return size

class File:
    def __init__(self):
        self.name = ''
        self.size = 0
    def show(self, level = ''):
        return print(f'{level}{self.name} {self.size}')

def parseToTree(lines):
    base = Directory()
    current = base

    for line in lines:
        if (line.startswith('$ cd /')):
            current = base
            continue
        if (line.startswith('$ cd ..')):
            current = current.parent
            continue
        if (line.startswith('$ cd')):
            current = current.getChildDirectory(line[4:].strip())
            continue
        if (line.startswith('$ ls')):
            continue
        if (line.startswith('dir')):
            d = Directory()
            d.name = line[4:]
            d.parent = current
            current.directories.append(d)
            continue
        m = re.match("(\d+) (.+)", line)
        if (m):
            f = File()
            f.size = int(m.groups()[0])
            f.name = m.groups()[1]
            current.files.append(f)
    return base

d = parseToTree(lines)

sizes = []
d.getDirectorySizes(sizes)

currentFree = 70000000 - d.size
neededSpace = 30000000 - currentFree

part1 = 0
part2 = d.size

for s in sizes:
    if (s <= 100000):
        part1 += s
    if (s >= neededSpace):
        if (s < part2):
            part2 = s

print(f'part 1 is {part1}, part 2 is {part2}')