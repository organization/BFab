import sys, re

# 심플한 BF 인터프리터

class Runtime:
    def __init__(self, tape, stdin=sys.stdin, stdout=sys.stdout, memSize=30000):
        self.stdin = stdin
        self.stdout = stdout
        self.mem = [0] * memSize
        self.tape = re.sub("[^\.,<>\-+\[\]]", "", tape)
        self.offset = 0
        self.memOffset = 0
        self.brackets = dict()
        self.parse_bracket()

    def parse_bracket(self):
        stack = list()
        for i, c in enumerate(self.tape):
            if c == "[":
                stack.append(i)
            if c == "]":
                match = stack.pop()
                self.brackets[i] = match
                self.brackets[match] = i

        if len(stack) > 0:
            raise RuntimeError("Brackets mismatch!")

    def run(self):
        while self.offset < len(self.tape):
            code = self.tape[self.offset]
            self.readTape(code)
            self.offset += 1

    def readTape(self, code):
        if code == "+":
            self.mem[self.memOffset] += 1
        elif code == "-":
            self.mem[self.memOffset] -= 1
        elif code == ">":
            self.memOffset += 1
        elif code == "<":
            self.memOffset -= 1
        elif code == "[" and self.mem[self.memOffset] == 0:
            self.offset = self.brackets[self.offset]
        elif code == "]" and self.mem[self.memOffset] != 0:
            self.offset = self.brackets[self.offset]
        elif code == ".":
            self.stdout.write(chr(self.mem[self.memOffset]))
        elif code == ",":
            self.mem[self.memOffset] = ord(self.stdin.read(1))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <.bf file>" % sys.argv[0])
        sys.exit()

    fp = open(sys.argv[1], "r")
    tape = fp.read()
    fp.close()
    runtime = Runtime(tape)
    runtime.run()
