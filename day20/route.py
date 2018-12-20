def parse(file_name):
    routes = []
    with open(file_name) as f:
        f.read(1)
        c = f.read(1)
        while c != '$':
            routes.append(c)
            c = f.read(1)
    return routes

def main():
    route = parse('input1')
    m = {}
    stack = []
    pos = 0
    max_len = len(route)
    current_coord = (0, 0)
    while pos < max_len:
        c = route[pos]
        print(current_coord)
        if c == '(':
            stack.append(current_coord)
        elif c == ')':
            current_coord = stack.pop()
        elif c == '|':
            current_coord = stack[-1]
        else:
            row, col = current_coord
            if c == 'N':
                row += 1
            elif c == 'S':
                row -= 1
            elif c == 'E':
                col += 1
            elif c == 'W':
                col -= 1
            else:
                print("Invalid character")
            m.setdefault(row, dict())[col] = True
            current_coord = (row, col)
        pos += 1
    print(stack)
    draw_map(m)
    return m

def draw_map(m):
    rows = list(m.keys())
    cols = [col_no for row_no, row in m.items() for col_no, _ in row.items() ]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    arr = [['x' if r == 0 and c == 0 else '.' if m.get(r, {}).get(c, False) else '#' for c in range(min_col - 1, max_col + 1)] for r in range(min_row - 1, max_row + 1)]
    print('\n'.join([''.join(a) for a in arr]))
print(main())
