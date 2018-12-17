class Unit:
    def __init__(self, position, unit_type):
        self.unit_type = unit_type
        self.hit_point = 200
        self.position = position

    def is_opponent(self, other):
        return (other is Unit and self.unit_type == 'G' and other.unit_type == 'E') or (self.unit_type == 'E' and other.unit_type == 'G')


class Board:
    def __init__(self, lines):
        board = [[None for col_num, cell in enumerate(line)] for row_num, line in enumerate(lines)]
        for row_num, line in enumerate(lines):
            for col_num, cell in enumerate(line):
                if cell == 'E' or cell == 'G':
                    board[row_num][col_num] = Unit((row_num, col_num), cell)
                else:
                    board[row_num][col_num] = cell
        self.board = board
        self.max_row = len(board)
        self.max_col = len(board[0])

    # Return all position of unit
    def unit_positions(self):
        result = []
        for row_num, row in enumerate(self.board):
            for col_num, cell in enumerate(row):
                if cell is Unit:
                    result.append(cell)
        return result

    # return neighbor cells of an unit
    def unit_neighbors(self, position):
        row_num, col_num = position
        neighbors = [(row_num - 1, col_num), (row_num, col_num - 1), (row_num, col_num + 1), (row_num + 1, col_num)]
        return [((r, c), self.board[r][c]) for (r, c) in neighbors if r >= 0 and r < self.max_row and c >= 0 and c < self.max_col and self.board[r][c] != '#']

    # check if an unit is targeting another unit
    def is_target(self, unit):
        neighbors = self.unit_neighbors(unit.position)
        targets = [for neighbor in neighbors if neighbor is Unit and unit.is_opponent(neighbor)]

    def is_opponent(self, unit1, unit2):
        return (unit1 == 'G' and unit2 == 'E') or (unit1 == 'E' and unit2 == 'G')
