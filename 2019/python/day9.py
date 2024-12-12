from computer import Computer

with open('2019/_input/day9.txt') as f:
    program = f.read().strip()

c = Computer(program)
c.set_input([1])

print('part 1:', c.go())
c.reset()

c.set_input([2])
print('part 2:', c.go())