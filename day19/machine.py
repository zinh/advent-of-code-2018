class Machine:
    def __init__(self, ip_register = 0, registers = []):
        if registers:
            self.registers = registers
        else:
            self.registers = [1, 0, 0, 0, 0, 0]

        self.ip_register = ip_register
        self.ip = self.registers[self.ip_register]

    def execute(self, insn):
        op, a, b, c = insn
        if op == 'addr':
            self.registers[c] = self.registers[a] + self.registers[b]
        elif op == 'addi':
            self.registers[c] = self.registers[a] + b
        elif op == 'mulr':
            self.registers[c] = self.registers[a] * self.registers[b]
        elif op == 'muli':
            self.registers[c] = self.registers[a] * b
        elif op == 'banr':
            self.registers[c] = self.registers[a] & self.registers[b]
        elif op == 'bani':
            self.registers[c] = self.registers[a] & b
        elif op == 'borr':
            self.registers[c] = self.registers[a] | self.registers[b]
        elif op == 'bori':
            self.registers[c] = self.registers[a] | b
        elif op == 'setr':
            self.registers[c] = self.registers[a]
        elif op == 'seti':
            self.registers[c] = a
        elif op == 'gtir':
            if a > self.registers[b]:
                self.registers[c] = 1
            else:
                self.registers[c] = 0
        elif op == 'gtri':
            if self.registers[a] > b:
                self.registers[c] = 1
            else:
                self.registers[c] = 0
        elif op == 'gtrr':
            if self.registers[a] > self.registers[b]:
                self.registers[c] = 1
            else:
                self.registers[c] = 0
        elif op == 'eqir':
            if a == self.registers[b]:
                self.registers[c] = 1
            else:
                self.registers[c] = 0
        elif op == 'eqri':
            if self.registers[a] == b:
                self.registers[c] = 1
            else:
                self.registers[c] = 0
        elif op == 'eqrr':
            if self.registers[a] == self.registers[b]:
                self.registers[c] = 1
            else:
                self.registers[c] = 0

    def run_program(self, program):
        i = 0
        while self.ip < len(program):
            self.registers[self.ip_register] = self.ip
            insn = program[self.ip]
            s = 'IP = ' + str(self.ip) + ' Start: ' + str(self.registers) + str(insn)
            self.execute(insn)
            s += ' -> ' + str(self.registers)
            print(s)
            self.ip = self.registers[self.ip_register]
            if i > 100:
                break
            i += 1
            self.ip += 1
        return self.registers
