from board import Board
import pdb

class Game:
    def __init__(self, lines, attack_point = 3):
        self.board = Board(lines)
        self.attack_point = attack_point
        self.elf_win = True

    def run(self):
        turn_count = 0
        while not self.turn():
            turn_count += 1
        return turn_count, self.total_hit_point()

    # one game turn
    def turn(self):
        ended = True
        for unit in self.board.units():
            if not unit.is_dead():
              target = self.attack(unit)
              if target:
                  ended = False
                  if target.is_dead() and target.is_elf():
                      self.elf_win = False
                      return True
              elif self.move(unit):
                  ended = False
                  target = self.attack(unit)
                  if target is not None and target.is_dead() and target.is_elf():
                      self.elf_win = False
                      return True
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
            unit.attack(target, self.attack_point)
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
