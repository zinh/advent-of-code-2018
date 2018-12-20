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
    route = parse('input2')
    m = {}
    stack = []
    pos = 0
    max_len = len(route)
    current_coord = (0, 0)
    while pos < max_len:
        c = route[pos]
        #print(current_coord)
        if c == '(':
            stack.append(current_coord)
        elif c == ')':
            current_coord = stack.pop()
        elif c == '|':
            current_coord = stack[-1]
        else:
            row, col = current_coord
            if c == 'N':
                m.setdefault(row + 1, dict())[col] = '-'
                row += 2
            elif c == 'S':
                m.setdefault(row - 1, dict())[col] = '-'
                row -= 2
            elif c == 'E':
                m.setdefault(row, dict())[col + 1] = '|'
                col += 2
            elif c == 'W':
                m.setdefault(row, dict())[col - 1] = '|'
                col -= 2
            else:
                print("Invalid character")
            m.setdefault(row, dict())[col] = '.'
            current_coord = (row, col)
        pos += 1
    #print(stack)
    #print('m = ', m)
    distances = count_doors(m)
    draw_map(m, distances)
    return m

def draw_map(m, distances):
    rows = list(m.keys())
    cols = [col_no for row_no, row in m.items() for col_no, _ in row.items() ]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    arr = [[print_cell(r, c, m, distances) for c in range(min_col - 1, max_col + 2)] for r in range(min_row - 1, max_row + 2)]
    print('\n'.join([''.join(a) for a in arr]))

def print_cell(row, col, m, distances):
    if row == 0 and col == 0:
        return 'x'
    cell = m.get(row, {}).get(col, '#')
    if cell == '.':
        #return '{:02d}'.format(distances[row][col])
        return str(distances[row][col])
    return cell

def count_doors(m):
    distances = {0: {0: 0}}
    for row_no, row in m.items():
        distances[row_no] = {}
        for col_no, col in row.items():
            distances[row_no][col_no] = None
    update_distance(m, distances, (0, 0), 0)
    return distances

def update_distance(m, distances, pos, current_distance):
    print(pos)
    r, c = pos
    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for (row, col) in neighbors:
        cell = m.get(row, {}).get(col)
        #if pos == (2, -2):
        #    import pdb; pdb.set_trace()
        if cell == '|' or cell == '-':
            if distances[row][col] is None:
                distances[row][col] = current_distance
                update_distance(m, distances, (row, col), current_distance + 1)
        elif cell == '.':
            if distances[row][col] is None or distances[row][col] < current_distance:
                distances[row][col] = current_distance
                update_distance(m, distances, (row, col), current_distance)

main()
