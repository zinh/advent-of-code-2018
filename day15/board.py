from cell import Cell
import pdb

class Board:
    def __init__(self, lines, board = None):
        if board:
            self.board = board
        else:
            self.board = [[Cell((row_no, col_no), cell) for col_no, cell in enumerate(line)] 
                    for row_no, line in enumerate(lines)]
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
        return [self.board[r][c] for r, c in [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)] 
                if r >= 0 and r < self.max_row and c >= 0 and c < self.max_col and not self.board[r][c].is_wall()]

    def moveable_neighbors(self, cell):
        return [neighbor for neighbor in self.neighbors(cell) if neighbor.is_moveable()]

    # return all opponent of an unit
    def opponents(self, unit):
        return [other for other in self.units() if unit.is_opponent_of(other)]

    def remove(self, pos):
        r, c = pos
        self.board[r][c] = Cell(pos, '.')

    def find_shortest(self, from_unit, to_unit):
        distance_board = self.clone()
        distance, path, target = distance_board.find_shortest_recursive([from_unit], to_unit, 0)
        #if from_unit.position == (1, 4):
        #pdb.set_trace()
        #Board.print_board(distance_board.board)
        if distance is None:
            return None, None, None
        else:
            #print(from_unit.position, to_unit.position, path[0].position, distance)
            return distance, sorted(path, key=lambda x: (x.position[0], x.position[1]))[0], target

    def find_shortest_recursive(self, from_units, to_unit, current_distance):
        next_units = []
        found = False
        for from_unit in from_units:
            for neighbor in self.neighbors(from_unit):
                if neighbor.is_moveable() or (isinstance(neighbor.type, int) and neighbor.type > current_distance + 1):
                    neighbor.type = current_distance + 1
                    next_units.append(neighbor)
                elif neighbor.position == to_unit.position:
                    found = True
        if found:
            selected_target = sorted([neighbor for neighbor in self.neighbors(to_unit) if isinstance(neighbor.type, int)], 
                    key=lambda x: (x.type, x.position[0], x.position[1]))[0]
            min_distance = selected_target.type
            return min_distance, self.backtrack([to_unit], min_distance), selected_target
        if next_units:
            return self.find_shortest_recursive(next_units, to_unit, current_distance + 1)
        return None, None, None

    def backtrack(self, from_units, distance):
        # get lowest neighbor
        if distance == 0:
            return from_units
        next_targets = set()
        for unit in from_units:
            next_targets |= {neighbor for neighbor in self.neighbors(unit) if isinstance(neighbor.type, int) and neighbor.type == distance}
        #pdb.set_trace()
        if next_targets:
            return self.backtrack(next_targets, distance - 1)
        return None

    def move_unit(self, unit, destination):
        old_row, old_col = unit.position
        row, col = destination.position
        self.board[row][col] = unit
        self.board[old_row][old_col] = Cell(unit.position, '.')
        unit.position = destination.position

    def clone(self):
        return Board(None, board = [[Cell(cell.position, cell.type) for cell in row] for row in self.board])

    @staticmethod
    def print_board(board):
        s = ""
        for row in board:
            s += "".join([str(cell.type) for cell in row])
            for cell in row:
                if cell.is_unit():
                    s += " ({}) ".format(cell.hit_point)
            s += "\n"
        return s
        #return "\n".join(["".join([str(cell.type) for cell in row]) for row in board])
