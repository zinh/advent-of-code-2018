def count_pot(s, left):
    result = 0
    for c in s:
        if c == '#':
            result += left
        left += 1
    return result

def run():
    with open('input') as f:
        initial_state = ['.', '.', '.', '.', '.'] + [c for c in f.readline().strip()] + ['.', '.', '.', '.', '.'] 
        rules = {}
        for line in f:
            inp, out = line.strip().split('=>')
            rules[inp.strip()] = out.strip()
    
    max_generation = 40
    state = initial_state
    left = -5
    for gen in range(0, max_generation):
        new_state = ['.' for _ in range(0, len(state))]
        for i in range(0, len(state) - 4):
            sub_str = state[i:i+5]
            next_cell = rules.get(''.join(sub_str), '.')
            new_state[i+2] = next_cell
        state = new_state
        print(''.join(state))
    print(left)
    return count_pot(state, left)

print(run())
