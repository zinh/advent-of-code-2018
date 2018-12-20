import pdb

class Unit:
    def __init__(self, position, unit_type):
        self.unit_type = unit_type
        self.hit_point = 200
        self.position = position

    def is_opponent(self, other):
        return type(other) is Unit and ((self.unit_type == 'G' and other.unit_type == 'E') or (self.unit_type == 'E' and other.unit_type == 'G'))

    def attack(self, other):
        other.hit_point -= 3

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
                if type(cell) is Unit:
                    result.append(cell)
        return result

    # move a unit
    def move(self, unit):
        neighbors = Board.unit_neighbors(self.board, unit.position)
        for pos, neighbor in neighbors:
            if unit.is_opponent(neighbor):
                unit.attack(neighbor)
                if neighbor.hit_point <= 0:
                    r, c = neighbor.position
                    self.board[r][c] = '.'
                return
        reachable_units, distance_board = self.find_targets(unit)
        if len(reachable_units) > 0:
            # get all unit with same distance
            min_distance = reachable_units[0][0]
            selected_targets = filter(lambda u: u[0] == min_distance, reachable_units)
            for distance, unit in selected_targets:
                #pdb.set_trace()
                r, c = Board.backtrack_path(distance_board, unit.position, distance + 1)
                current_r, current_c = unit.position
                self.board[r][c] = unit
                self.board[current_r][current_c] = '.'
                unit.position = (r, c)

    # find nearest target
    def find_targets(self, unit):
        distance_board = Board.find_path(unit, 1, [[cell for cell in row] for row in self.board])
        reachable_units = []
        for row in distance_board:
            for cell in row:
                if unit.is_opponent(cell):
                    for position, neighbor_type in Board.unit_neighbors(distance_board, cell.position):
                        if type(neighbor_type) is int:
                            #if unit.position == (2, 1):
                            #    pdb.set_trace()
                            reachable_units.append((neighbor_type, unit))
                            break
        return sorted(reachable_units, key=lambda x: x[0]), distance_board

    def __str__(self):
        return Board.print_board(self.board)

    # return neighbor cells of an unit
    @staticmethod
    def unit_neighbors(board, position):
        row_num, col_num = position
        max_row, max_col = len(board), len(board[0])
        neighbors = [(row_num - 1, col_num), (row_num, col_num - 1), (row_num, col_num + 1), (row_num + 1, col_num)]
        return [((r, c), board[r][c]) for (r, c) in neighbors if r >= 0 and r < max_row and c >= 0 and c < max_col and board[r][c] != '#']

    @staticmethod
    def find_path(unit, distance, board):
        for (r, c), cell_type in Board.unit_neighbors(board, unit.position):
            if cell_type == '.':
                board[r][c] = distance
                Board.find_path(unit, distance + 1, board)
        return board

    @staticmethod
    def backtrack_path(distance_board, pos, current_distance):
        if current_distance == 1:
            return pos
        pdb.set_trace()
        for (r, c), cell_type in Board.unit_neighbors(distance_board, pos):
            if type(cell_type) is int and cell_type == current_distance - 1:
                return Board.backtrack_path(distance_board, (r, c), current_distance - 1) 

    @staticmethod
    def print_board(board):
        return "\n".join(["".join([cell.unit_type if type(cell) is Unit else str(cell) for cell in row]) for row in board])
