def file_process(file_name):
    with open(file_name) as f:
        initial_state = [c for c in f.readline().strip()]
        rules = {}
        for line in f:
            inp, out = line.strip().split('=>')
            rules[inp.strip()] = out.strip()
    return initial_state, rules

def print_score(left_most, state):
    result = 0
    for c in state:
        if c == '#':
            result += left_most
        left_most += 1
    return result

def generate(initial_state, rules, max_generation):
    append_group = ['.','.','.','.','.']
    state = append_group + initial_state + append_group
    left_most = -5
    history = {}
    for gen in range(0, max_generation):
        new_state = ['.' for _ in range(0, len(state))]
        for i in range(0, len(state) - 5):
            subgroup = state[i:i+5]
            next_group = rules.get(''.join(subgroup), '.')
            new_state[i + 2] = next_group
        for i in range(0, len(new_state)):
            if new_state[i] == '#':
                start = i
                break
        for i in range(len(state) - 1, -1, -1):
            if new_state[i] == '#':
                end = i
                break
        state = append_group + new_state[start:end + 1] + append_group
        left_most += (start - 5)
        state_text = ''.join(state)
        if history.get(state_text):
            print(f'{gen}', left_most, print_score(left_most, state))
            break
        else:
            history[state_text] = gen

initial_state, rules = file_process('input4')
generate(initial_state, rules, 150)
