def get_opcode(code):
    return int(str(code)[-2:])

def get_mode(code, n):
    code = str(code)
    if n > len(code) - 2:
        return 0
    return int(code[-(n + 2)])

class Computer:
    def __init__(self, codes):
        self.codes = codes
        self.position = 0
        self.input_position = 0

    def reset(self):
        self.position = 0
        self.input_position = 0

    def set_input(self, input):
        self.input = input

    def get_param(self, code, offset):
        mode = get_mode(code, offset)
        if mode == 0:
            return self.codes[self.codes[self.position + offset]]
        else:
            return self.codes[self.position + offset]
        
    def set_param(self, val, offset:int = 0):
        self.codes[self.codes[self.position + offset]] = val

    def go(self):
        while self.codes[self.position] != 99:
            code = self.codes[self.position]
            op = get_opcode(self.codes[self.position])
            if op == 1:
                v1 = self.get_param(code, 1) 
                v2 = self.get_param(code, 2)
                self.set_param(v1 + v2, 3)
                self.position += 4
            if op == 2:
                v1 = self.get_param(code, 1) 
                v2 = self.get_param(code, 2)
                self.set_param(v1 * v2, 3)
                self.position += 4
            if op == 3:
                self.codes[self.codes[self.position + 1]] = self.input[self.input_position]
                self.input_position += 1
                self.position += 2
            if op == 4:
                v = self.codes[self.codes[self.position+1]]
                self.position += 2
                return v
            if op == 5:
                v1 = self.get_param(code, 1)
                v2 = self.get_param(code, 2)
                if v1 != 0:
                    self.position = v2
                else:
                    self.position += 3
            if op == 6:
                v1 = self.get_param(code, 1)
                v2 = self.get_param(code, 2)
                if v1 == 0:
                    self.position = v2
                else:
                    self.position += 3
            if op == 7:
                v1 = self.get_param(code, 1) 
                v2 = self.get_param(code, 2)
                self.set_param(1 if v1 < v2 else 0, 3)
                self.position += 4
            if op == 8:
                v1 = self.get_param(code, 1) 
                v2 = self.get_param(code, 2)
                self.set_param(1 if v1 == v2 else 0, 3)
                self.position += 4
        return None