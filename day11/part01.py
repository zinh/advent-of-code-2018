max_coor = 300

def calculate_grid(serial):
    grid = [[0 for row in range(0, max_coor)] for col in range(0, max_coor)]
    for col in range(0, max_coor):
        for row in range(0, max_coor):
            grid[col][row] = calculate_power(col, row, serial)
    return grid

def calculate_power(x, y, serial):
    rack_id = x + 10
    return (rack_id * y + serial) * rack_id % 1000 // 100 - 5

def find_subgrid(grid, size):
    max_power = 0
    pos = None
    for col in range(0, max_coor - size + 1):
        for row in range(0, max_coor - size + 1):
            p = sum([grid[col + i][row + j] for i in range(0, size) for j in range(0, size)])
            if p > max_power:
                max_power = p
                pos = (col, row)
    return max_power, pos

def subgroups(grid):
    memo = {col_no: {row_no: row for row_no, row in enumerate(col)} for col_no, col in enumerate(grid)}
    max_size = 0
    max_pos = None
    max_power = 0
    for size in range(2, 300):
        new_memo = {}
        for col in range(0, max_coor - size + 1):
            new_memo[col] = {}
            for row in range(0, max_coor - size + 1):
                new_power = memo[col][row]
                for i in range(col, col + size):
                    new_power += grid[i][row + size - 1]
                for j in range(row, row + size - 1):
                    new_power += grid[col + size - 1][j]
                new_memo[col][row] = new_power
                if new_power > max_power:
                    max_power = new_power
                    max_pos = (col, row)
                    max_size = size
        memo = new_memo
    return max_pos, max_size

grid = calculate_grid(4842)
print(subgroups(grid))
