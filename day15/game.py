from board import Board
import pdb

class Game:
    def __init__(self, lines):
        self.board = Board(lines)

    # one game turn
    def turn(self):
        ended = True
        for unit in self.board.units():
            if not unit.is_dead():
              if self.attack(unit):
                  ended = False
              elif self.move(unit):
                  ended = False
                  self.attack(unit)
        return ended

    # move a unit
    def move(self, unit):
        paths = []
        for opponent in self.board.opponents(unit):
            distance, next_step, target = self.board.find_shortest(unit, opponent)
            if distance is not None:
                paths.append((distance, next_step, target))
        if paths:
            paths.sort(key=lambda x: (x[0], x[2].position[0], x[2].position[1]))
            _, next_step, target = paths[0]
            self.board.move_unit(unit, next_step)
            return next_step
        return None

    def attack(self, unit):
        neighbor_units = [cell for cell in self.board.neighbors(unit) if unit.is_opponent_of(cell)]
        #if unit.position == (2, 3):
        #    pdb.set_trace()
        if neighbor_units:
            neighbor_units.sort(key=lambda u: (u.hit_point, u.position[0], u.position[1]))
            target = neighbor_units[0]
            unit.attack(target)
            if target.is_dead():
                self.board.remove(target.position)
            return target
        return None

    def total_hit_point(self):
        return sum([unit.hit_point for unit in self.board.units()])

    def print_hit_point(self):
        for unit in self.board.units():
            print(unit.position, unit.hit_point)


    def __str__(self):
        return str(self.board)
