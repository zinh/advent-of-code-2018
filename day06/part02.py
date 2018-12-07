from part01 import read_file

def process():
    MAX_DISTANCE = 10000
    points = read_file('input')
    max_col = max(points, key=lambda x: x[0])[0]
    max_row = max(points, key=lambda x: x[1])[1]
    grid = [[0 for cell in range(0, max_col)] for row in range(0, max_row)]
    for row in range(0, max_row):
        for col in range(0, max_col):
            grid[row][col] = sum([distance(point, (col, row)) for point in points])
    return sum([1 for row in grid for cell in row if cell < MAX_DISTANCE])

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(process())
