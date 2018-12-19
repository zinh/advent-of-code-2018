from machine import Machine

program = []
with open('input') as f:
    f.readline() # ignore first line
    for line in f:
        op, a, b, c = line.strip().split(' ')
        program.append((op, int(a), int(b), int(c)))

#print(program)
machine = Machine(5)
print(machine.run_program(program))
