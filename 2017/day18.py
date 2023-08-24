import re

class program:

    def __init__(self, id):
        self.id = id            # the program's id - used to set the 'p' register
        self.operations = []    # the operations to execute
        self.pointer = 0        # the index of the current operation to execute
        self.registers = {}     # the registers holding various values
        self.queue = []         # the queue of values sent by the other program
        self.program = None     # the other program (it sends us values)
        self.sends = 0          # for tracking the number of 'sends' we perform

    def execute_operation(self, operation):
        (o, v1, v2) = operation

        # if the register doesn't exist, create it but check the the key isn't a number first
        if not v1.isnumeric() and v1 not in self.registers:
            self.registers[v1] = self.id if v1 == 'p' else 0

        if o == 'snd':
            # for part 1, we just need to play the sound
            if self.id == -1:
                self.queue.append(self.get_value(v1))
                return 1
            # for part 2, we need to send the value to the other program
            self.program.queue.append(self.get_value(v1))
            self.sends += 1
            return 1

        if o == 'set':
            self.registers[v1] = self.get_value(v2)
            return 1

        if o == 'add':
            self.registers[v1] += self.get_value(v2)
            return 1

        if o == 'mul':
            self.registers[v1] *= self.get_value(v2)
            return 1

        if o == 'mod':
            self.registers[v1] %= self.get_value(v2)
            return 1

        if o == 'rcv':
            # for part 1 we need to check if v1 is > 0 and if so, we know the last sound played
            if self.id == -1:
                if self.get_value(v1) != 0:
                    return -(self.pointer + 1)
                else:
                    return 1
            # for part 2, we need to check if the queue is empty and if so, we could be deadlocked
            if len(self.queue) == 0:
                return 0
            else:
                self.registers[v1] = self.queue.pop(0)
                return 1

        if o == 'jgz':
            if self.get_value(v1) > 0:
                return self.get_value(v2)
            else:
                return 1

    def out_of_bounds(self):
        return self.pointer < 0 or self.pointer >= len(self.operations)

    def tick(self):
        move = self.execute_operation(self.operations[self.pointer])
        self.pointer += move
        return move

    def get_value(self, val):
        if val.lstrip('-').isnumeric():
            return int(val)
        return int(self.registers[val])




# create the program
p = program(-1) # -1 is the id for the 'sound' program

# read in the lines and populate the program with operations
for line in open('./_input/day18.txt', 'r').readlines():
    m = re.match('([a-z]+)\s+([a-z-0-9]+)\s*([a-z-0-9]*)', line)
    p.operations.append((m.group(1), m.group(2), m.group(3)))

iteration = 0
while not p.out_of_bounds():
    iteration += 1
    # have the programs try to execute their next operation, m# is the pointer movement from the operation
    p.tick()

print(f'part 1: {p.queue[-1]}')


# create the programs and 'link' them together
p0 = program(0)
p1 = program(1)
p0.program = p1
p1.program = p0

# read in the lines and populate the programs with operations
for line in open('./_input/day18.txt', 'r').readlines():
    m = re.match('([a-z]+)\s+([a-z-0-9]+)\s*([a-z-0-9]*)', line)
    p0.operations.append((m.group(1), m.group(2), m.group(3)))
    p1.operations.append((m.group(1), m.group(2), m.group(3)))

iteration = 0
while not p0.out_of_bounds() and not p1.out_of_bounds():
    iteration += 1
    # have the programs try to execute their next operation, m# is the pointer movement from the operation
    m0 = p0.tick()
    m1 = p1.tick()
    # if we're in a deadlock, stop
    if m0 == 0 and m1 == 0:
        break

print(f'part 2: {p1.sends}')
