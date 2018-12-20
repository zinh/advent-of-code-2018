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
    route = parse('input3')
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
    draw_map(m)
    #print('m = ', m)
    count_doors(m)
    return m

def draw_map(m):
    rows = list(m.keys())
    cols = [col_no for row_no, row in m.items() for col_no, _ in row.items() ]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    arr = [['x' if r == 0 and c == 0 else m.get(r, {}).get(c, '#') for c in range(min_col - 1, max_col + 2)] for r in range(min_row - 1, max_row + 2)]
    print('\n'.join([''.join(a) for a in arr]))

def count_doors(m):
    distances = {0: {0: 0}}
    for row_no, row in m.items():
        distances[row_no] = {}
        for col_no, col in row.items():
            distances[row_no][col_no] = None
    update_distance(m, distances, (0, 0), 0)
    print('distances = ', distances)

def update_distance(m, distances, pos, current_distance):
    r, c = pos
    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    #print(pos)
    for (row, col) in neighbors:
        cell = m.get(row, {}).get(col)
        #import pdb; pdb.set_trace()
        if cell == '|' or cell == '-':
            if distances[row][col] is None:
                update_distance(m, distances, (row, col), current_distance + 1)
        elif cell == '.':
            if distances[row][col] is None:# or distances[row][col] < current_distance:
                distances[row][col] = current_distance
                update_distance(m, distances, (row, col), current_distance)

main()
