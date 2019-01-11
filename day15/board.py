class Cell:
    def __init__(self, position, cell_type):
        self.position = position
        self.type = cell_type
        self.hit_point = 200

    def is_unit(self):
        return self.type == 'E' or self.type == 'G'

    def is_opponent_of(self, other):
        return (self.type == 'E' and other.type == 'G') or (self.type == 'G' and other.type == 'E')

    def is_moveable(self):
        return self.type == '.'

class Board:
    def __init__(self, lines):
        self.board = [[Cell((row_no, col_no), cell) for col_no, cell in enumerate(line)] for row_no, line in enumerate(lines)]
        self.max_row = len(self.board)
        self.max_col = len(self.board[0])

    def __str__(self):
        return Board.print_board(self.board)

    def __iter__(self):
        return iter([cell for row in self.board for cell in row])

    # return all units
    def units(self):
        return [cell for cell in self if cell.is_unit()]

    # return neighbor cells
    def neighbors(self, cell):
        row, col = cell.position
        return [self.board[r][c] for r, c in (row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col) if r >= 0 and r < self.max_row and c >= 0 and c < self.max_col]

    # return all opponent of an unit
    def opponents(self, unit):
        pass

    @staticmethod
    def print_board(board):
        return "\n".join(["".join([cell.type for cell in row]) for row in board])

class Game:
    def __init__(self, lines):
        self.board = Board(lines)

    # one game turn
    def turn(self):
        for unit in self.board.units():
            print(unit.position)

    # move a unit
    def move(self, unit):
        # check if neighbors cell is opponent
        for cell in self.board.neighbors(unit):
            if unit.is_opponent_of(cell): # attack opponent with fewest hit point
                pass

    def __str__(self):
        return str(self.board)
