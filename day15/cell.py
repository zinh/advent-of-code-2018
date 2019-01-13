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

    def attack(self, other, point = 3):
        if self.is_elf():
            other.hit_point -= point 
        else:
            other.hit_point -= 3

    def is_dead(self):
        return self.hit_point <= 0

    def is_wall(self):
        return self.type == '#'

    def is_elf(self):
        return self.type == 'E'

    def __str__(self):
        return "({}, {}), HP={}".format(self.position[0], self.position[1], self.hit_point)
