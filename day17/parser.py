def parse(file_name):
    input_data = []
    with open(file_name) as f:
        for line in f:
            first, second = line.strip().split(', ')
            input_data.append([split_expr(first), split_expr(second)])
    return input_data

def split_expr(s):
    label, numbers = s.split('=')
    if '..' in numbers:
        start, end = numbers.split('..')
        return label, list(range(int(start), int(end) + 1))
    else:
        return label, [int(numbers)]

print(parse('input'))
