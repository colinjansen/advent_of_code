from collections import defaultdict

def get_opcode(code):
    return int(str(code)[-2:])

def get_mode(code, n):
    code = str(code)
    if n > len(code) - 2:
        return 0
    return int(code[-(n + 2)])

class Computer:
    def __init__(self, codes, debug=False):

        self.codes = defaultdict(int)
        for i, c in enumerate([int(c) for c in (codes+'.')[:-1].split(',')]):
            self.codes[i] = c

        self.original = self.codes.copy()
        self.position = 0
        self.input_position = 0
        self.input = []
        self.halted = False
        self.debug = debug
        self.relative_base = 0

    def reset(self):
        self.position = 0
        self.relative_base = 0
        self.codes = self.original.copy()
        self.input_position = 0

    def set_memory(self, address, value):
        self.codes[address] = value

    def set_input(self, input):
        self.input = input
    
    def add_input(self, input):
        self.input.append(input)

    def get_param(self, param_number:int = 0):
        mode = get_mode(self.codes[self.position], param_number)
        if mode == 0:
            return self.codes[self.codes[self.position + param_number]]
        if mode == 1:
            return self.codes[self.position + param_number]
        if mode == 2:
            return self.codes[self.relative_base + self.codes[self.position + param_number]]
        raise ValueError(f"get_param: parameter mode {mode} is unknown")
        
    def set_param(self, val, param_number:int = 0):
        mode = get_mode(self.codes[self.position], param_number)
        if mode == 0: # position mode
            self.codes[self.codes[self.position + param_number]] = val
            return
        if mode == 2: # relative mode
            self.codes[self.relative_base + self.codes[self.position + param_number]] = val
            return
        raise ValueError(f"set_param: parameter mode {mode} is unknown")
    
    def write(self, val):
        mode = get_mode(self.codes[self.position], 1)

        if mode == 0: # position mode
            self.codes[self.codes[self.position + 1]] = val

        if mode == 2: # relative mode
            self.codes[self.relative_base + self.codes[self.position + 1]] = val

        self.position += 2

    def default_input(self):
        v = self.input[self.input_position]
        self.input_position += 1
        return v
    
    def go(self, output_function=None, input_function=None):

        if input_function == None:
            input_function = self.default_input

        while not self.halted:
            op = get_opcode(self.codes[self.position])
            if self.debug:
                print(self.position)
            if op == 99:
                self.halted = True
                return None
            if op == 1:
                v1 = self.get_param( 1) 
                v2 = self.get_param( 2)
                self.set_param(v1 + v2, 3)
                self.position += 4
            if op == 2:
                v1 = self.get_param( 1) 
                v2 = self.get_param( 2)
                self.set_param(v1 * v2, 3)
                self.position += 4

            if op == 3:
                self.write(input_function())

            if op == 4: # OUTPUT
                v1 = self.get_param(1)
                self.position += 2
                if output_function:
                    output_function(v1)
                else:
                    return v1            
            if op == 5:
                v1 = self.get_param( 1)
                v2 = self.get_param( 2)
                if v1:
                    self.position = v2
                else:
                    self.position += 3
            if op == 6:
                v1 = self.get_param( 1)
                v2 = self.get_param( 2)
                if not v1:
                    self.position = v2
                else:
                    self.position += 3
            if op == 7:
                v1 = self.get_param( 1) 
                v2 = self.get_param( 2)
                self.set_param(1 if v1 < v2 else 0, 3)
                self.position += 4
            if op == 8:
                v1 = self.get_param( 1) 
                v2 = self.get_param( 2)
                self.set_param(1 if v1 == v2 else 0, 3)
                self.position += 4
            if op == 9:
                v1 = self.get_param(1)
                self.relative_base += v1
                self.position += 2


import unittest

class TestComputer(unittest.TestCase):

    def test_equal_positional(self):
        c = Computer('3,9,8,9,10,9,4,9,99,-1,8')
        c.set_input([10])
        self.assertEqual(c.go(), False)
        c.reset()
        c.set_input([8])
        self.assertEqual(c.go(), True)

    def test_less_than_positional(self):
        c = Computer('3,9,7,9,10,9,4,9,99,-1,8')
        c.set_input([10])
        self.assertEqual(c.go(), False)
        c.reset()
        c.set_input([5])
        self.assertEqual(c.go(), True)

    def test_equal_immediate(self):
        c = Computer('3,3,1108,-1,8,3,4,3,99')
        c.set_input([10])
        self.assertEqual(c.go(), False)
        c.reset()
        c.set_input([8])
        self.assertEqual(c.go(), True)

    def test_less_than_immediate(self):
        c = Computer('3,3,1107,-1,8,3,4,3,99')
        c.set_input([10])
        self.assertEqual(c.go(), False)
        c.reset()
        c.set_input([5])
        self.assertEqual(c.go(), True)

    def test_jump_positional(self):
        c = Computer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        c.set_input([0])
        self.assertEqual(c.go(), 0)
        c.reset()
        c.set_input([5])
        self.assertEqual(c.go(), 1)

    def test_jump_immediate(self):
        c = Computer('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        c.set_input([0])
        self.assertEqual(c.go(), 0)
        c.reset()
        c.set_input([5])
        self.assertEqual(c.go(), 1)

    def test_full(self):
        c = Computer('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
        c.set_input([7])
        self.assertEqual(c.go(), 999)
        c.reset()
        c.set_input([8])
        self.assertEqual(c.go(), 1000)
        c.reset()
        c.set_input([9])
        self.assertEqual(c.go(), 1001)

    def test_relative_base(self):
        output = []
        program = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
        c = Computer(program)
        c.go(lambda v: output.append(v))
        self.assertEqual(output, [int(c) for c in program.split(',')])

    def test_relative_base2(self):
        output = []
        program = '1102,34915192,34915192,7,4,7,99,0'
        c = Computer(program)
        c.go(lambda v: output.append(v))
        self.assertEqual(len(str(output[0])), 16)

    def test_relative_base3(self):
        output = []
        program = '104,1125899906842624,99'
        c = Computer(program)
        c.go(lambda v: output.append(v))
        self.assertEqual(output[0], 1125899906842624)

if __name__ == '__main__':
    unittest.main()