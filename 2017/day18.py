import re

ops = []
registers = {}
pointer = 0
sounds = []

class operation:
    def __init__(self, op, reg, val):
        self.op = op
        self.register = reg
        self.val = val
    
    def go(self):

        if self.register not in registers:
            registers[self.register] = 0

        if self.op == 'snd':
            sounds.append(registers[self.register])
            return 1
        
        if self.op == 'set':
            registers[self.register] = get_value(self.val)
            return 1
        
        if self.op == 'add':
            registers[self.register] += get_value(self.val)
            return 1
        
        if self.op == 'mul':
            registers[self.register] *= get_value(self.val)
            return 1
        
        if self.op == 'mod':
            registers[self.register] %= get_value(self.val)
            return 1
        
        if self.op == 'rcv':
            if registers[self.register] != 0:
                return -(pointer + 1)
            else:
                return 1    
            
        if self.op == 'jgz':
            if registers[self.register] > 0:
                return get_value(self.val)
            else:
                return 1

def get_value(val):
    if val.lstrip('-').isnumeric():
        return int(val)
    return int(registers[val])


for line in open('./_input/day18.txt', 'r').readlines():
    m = re.match('([a-z]+)\s+([a-z]+)\s*([a-z-0-9]*)', line)
    ops.append(operation(m.group(1), m.group(2), m.group(3)))

while pointer > -1 and pointer < len(ops):
    pointer += ops[pointer].go()

print(sounds[-1])