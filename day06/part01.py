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
    grids = [[(0, None) for col in range(0, max_col)] for row in range(0, max_row)]
    for idx, point in enumerate(points):
        update_grids(grids, idx, [point], 1, max_col, max_row)

def update_grids(grids, label, points, distance, max_col, max_row):
    for point in points:
        col, row = point
        print(row, col)
        print(max_col, max_row)
        d, l = grids[row][col]
        if l is None:
            grids[row][col] = (distance, label)
            update_grids(grids, label, adjecent_points(point, max_col, max_row), distance + 1, max_col, max_row)
        elif l != label:
            if distance < d:
                grids[row][col] = (distance, label)
                update_grids(grids, label, adjecent_points(point, max_col, max_row), distance + 1, max_col, max_row)
    return grids

def adjecent_points(point, max_col, max_row):
    col, row = point
    return [(col + i, row + j) for i in [0, 1, -1] for j in [0, 1, -1] if valid(col, i, row, j, max_col, max_row)]

def valid(col, i, row, j, max_col, max_row):
    next_col, next_row = col + i, row + i
    return (i != 1 or j != 1) and next_col >= 0 and next_col < max_col and next_row >= 0 and next_row < max_row

process()
