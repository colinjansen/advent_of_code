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

for t in range(8):
    print(1 << 3 | t)

def deconstruct(program, answer=0):
    """
    Recursively deconstruct the program to find the answer

    Thanks to HyperNeutrino for explaining how to accomplish
    the deconstruction of the program.
    """
    if program == []: return answer
    # keep things octal
    for t in range(8):
        # move our current answer left by one octal place
        # and try the octal value for 't'
        a = answer << 3 | t
        # run our deconstructed program with the new answer
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        b = b ^ c
        # if the last octal place of b matches the last value of
        # our program, we have a match, recurse into the program
        # again but chop off the bit we found
        if b % 8 == program[-1]:
            _answer = deconstruct(program[:-1], a)
            # if we were unable to find an octal value that
            # works, continue the loop
            if _answer == None: continue
            # if we found a solution, return it
            return _answer

print('part 1:', go(program, A, 0, 0))
print('part 2:', deconstruct(program))


