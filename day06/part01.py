def read_file(file_name):
    points = []
    with open(file_name) as f:
        for line in f:
            col, row = [int(i) for i in line.split(',')]
            points.append((col, row))
    return points

def process():
    points = read_file('input')
    max_col = max(points, key=lambda x: x[0])[0]
    max_row = max(points, key=lambda x: x[1])[1]
    #print(max_col, max_row)
    grids = [[(None, None) for col in range(0, max_col + 1)] for row in range(0, max_row + 1)]
    for idx, point in enumerate(points):
        print(idx)
        update_grids(grids, idx, [point], 0, max_col, max_row)
    all_labels = {cell[1] for row in grids for cell in row}
    border_points = grids[0] + grids[max_row] + [row[0] for row in grids] + [row[max_col] for row in grids]
    border_labels = {point[1] for point in border_points}
    finite_labels = all_labels - border_labels
    m = max([count_label(grids, label) for label in finite_labels])
    print(m)

def count_label(grids, label):
    return sum([1 for row in grids for cell in row if cell[1] == label])

def update_grids(grids, label, points, distance, max_col, max_row):
    #print_grid(grids)
    neightbors = []
    if not points:
        return grids
    for point in points:
        col, row = point
        d, l = grids[row][col]
        if l is None:
            grids[row][col] = (distance, label)
        elif l != label:
            if distance < d:
                grids[row][col] = (distance, label)
        for p in adjecent_points(point, max_col, max_row):
            c, r = p
            d, l = grids[r][c]
            if (l is None or (l != label and d > distance + 1 )) and not duplicated(neightbors, p):
                neightbors.append(p)
    update_grids(grids, label, neightbors, distance + 1, max_col, max_row)

def adjecent_points(point, max_col, max_row):
    col, row = point
    return [(next_col, next_row) for next_col, next_row in [(col, row + 1), (col, row - 1), (col + 1, row), (col - 1, row)] if valid(next_col, next_row, max_col, max_row)]

def duplicated(points, point):
    for p in points:
        if p[0] == point[0] and p[1] == point[1]:
            return True
    return False

def valid(col, row, max_col, max_row):
    return col >= 0 and col <= max_col and row >= 0 and row <= max_row

def print_grid(grids):
    print("========")
    for row in grids:
        print("".join([str(cell[1]) if cell[1] is not None else 'x' for cell in row]))
# process()
