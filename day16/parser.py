import pdb
import re
import sys
from machine import Machine

#sys.setrecursionlimit(100000)

op_codes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def parse(file_name):
    count = 0
    with open(file_name) as f:
        state = []
        result = {}
        for line in f:
            if len(line) == 1:
                continue
            state.append(line.strip())
            if len(state) >= 3:
                h = execute(state)
                for insn, ops in h.items():
                    r = result.get(insn, set())
                    result[insn] = r.union({op for op in ops})
                state = []
    return filter_op_codes(result, {'bori': 2})

def execute(state):
    before, instruction, after = state
    bf_register = extract_list(before)
    af_register = extract_list(after)
    ins, a, b, c = [int(o) for o in instruction.split(' ')]
    count = 0
    h = {}
    for op in op_codes:
        m = Machine([b for b in bf_register])
        m.execute([op, a, b, c])
        if m.registers == af_register:
            count += 1
            r = h.setdefault(ins, [])
            r.append(op)
    return h

def extract_list(line):
    p = re.compile(r'\[(\d+), (\d+), (\d+), (\d+)\]')
    op, a, b, c = p.search(line).groups()
    return [int(op), int(a), int(b), int(c)]

# h: {op: insn}
def filter_op_codes(codes, h):
    # remove duplicated
    new_codes = {}
    for insn, ops in codes.items():
        new_codes[insn] = {op for op in ops if op not in h.keys()}
    tmp = {}
    for insn, ops in new_codes.items():
        if len(ops) <= 0:
            if insn not in h.values():
                return None
        else:
            tmp[insn] = ops
    new_codes = tmp
    if not new_codes:
        return h
    # get insn with lowest ops
    insn, ops = min(new_codes.items(), key=lambda param: len(param[1]))
    #pdb.set_trace()
    for op in ops:
        m = {op: insn}
        new_h = filter_op_codes(new_codes, {**m, **h})
        if new_h:
            return new_h

h = {v: k for k, v in parse('input').items()}
machine = Machine()
with open('testcase') as f:
    for line in f:
        insn, a, b, c = [int(c) for c in line.split(' ')]
        machine.execute([h[insn], a, b, c])

print(machine.registers)
