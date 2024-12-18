class Computer:

    A= 60589763
    B= 0
    C= 0

    def __init__(self, program, A, B, C):
        self.program = program
        self.A = A
        self.B = B
        self.C = C

    def combo(self, v):
        if v <= 3:
            return v
        if v == 4:
            return self.A
        if v == 5:
            return self.B
        if v == 6:
            return self.C
        if v == 7:
            raise Exception('Invalid combo value')

    def go(self, output_function):
        self.position = 0

        while self.position < len(self.program):

            op = self.program[self.position]
            v = self.program[self.position + 1]
            self.position += 2

            if op == 0:  # ADV
                self.A = self.A // (2 ** self.combo(v))

            elif op == 1: # BXL
                self.B ^= v

            elif op == 2: # BST
                self.B = self.combo(v) % 8

            elif op == 3: # JNZ
                if self.A != 0:
                    self.position = v

            elif op == 4: # BXC
                self.B = self.B ^ self.C

            elif op == 5: # OUT
                output_function(self.combo(v) % 8)

            elif op == 6: # BDV
                self.B = self.A // (2 ** self.combo(v))

            elif op == 7:
                self.C = self.A // (2 ** self.combo(v))

program = [2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0]
A = 60589763

def go(program=[], A=0, B=0, C=0):
    output = []
    c = Computer(program, A, B, C)
    c.go(lambda x: output.append(x))
    return output

print('part 1:', go(program, A, 0, 0))

A = 241575164155700
A += 65
print(go(program, A, 0, 0))
print(program)

# out = 0
# check = int(''.join(str(d) for d in program))
# count = 0
# val = 10000000000000
# while out != check:

#     output = go(program, A, 0, 0)
#     out = int(''.join(str(d) for d in output))
    
#     result = check - out
#     print('check:', result, val)
    
#     # going down and we passed zero
#     if val > 0 and result < 0:
#         val //= 2
#         val *= -1

#     # gong up and we passed zero
#     if val < 0 and result > 0:
#         val //= 2
#         val *= -1

#     if val == 0:
#         break

#     A += val
