import pdb 

class Cart:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.last_turn = None

    def move(self, state):
        if self.direction == '^':
            self.go_straight(state)
        elif self.direction == '>':
            self.go_right(state)
        elif self.direction == '<':
            self.go_left(state)
        elif self.direction == 'v':
            self.go_down(state)

    def go_straight(self, lines):
        row, col = self.position
        next_cell = lines[row - 1][col]
        if next_cell == '\\':
            self.direction = '<'
        elif next_cell == '/':
            self.direction = '>'
        elif next_cell == '+':
            if self.last_turn == 'left':
                self.direction = '^'
                self.last_turn = 'straight'
            elif self.last_turn == 'straight':
                self.direction = '>'
                self.last_turn = 'right'
            else:
                self.direction = '<'
                self.last_turn = 'left'
        self.position = (row - 1, col)

    def go_left(self, lines):
        row, col = self.position
        next_cell = lines[row][col - 1]
        if next_cell == '\\':
            self.direction = '^'
        elif next_cell == '/':
            self.direction = 'v'
        elif next_cell == '+':
            if self.last_turn == 'left':
                self.direction = '<'
                self.last_turn = 'straight'
            elif self.last_turn == 'straight':
                self.direction = '^'
                self.last_turn = 'right'
            else:
                self.direction = 'v'
                self.last_turn = 'left'
        self.position = (row, col - 1)

    def go_right(self, lines):
        row, col = self.position
        next_cell = lines[row][col + 1]
        if next_cell == '/':
            self.direction = '^'
        elif next_cell == '\\':
            self.direction = 'v'
        elif next_cell == '+':
            if self.last_turn == 'left':
                self.direction = '>'
                self.last_turn = 'straight'
            elif self.last_turn == 'straight':
                self.direction = 'v'
                self.last_turn = 'right'
            else:
                self.direction = '^'
                self.last_turn = 'left'
        self.position = (row, col + 1)

    def go_down(self, lines):
        row, col = self.position
        #if row + 1 >= len(lines):
        #    pdb.set_trace()
        #if col >= len(lines[row + 1]):
        #    pdb.set_trace()
        next_cell = lines[row + 1][col]
        if next_cell == '/':
            self.direction = '<'
        elif next_cell == '\\':
            self.direction = '>'
        elif next_cell == '+':
            if self.last_turn == 'left':
                self.direction = 'v'
                self.last_turn = 'straight'
            elif self.last_turn == 'straight':
                self.direction = '<'
                self.last_turn = 'right'
            else:
                self.direction = '>'
                self.last_turn = 'left'
        self.position = (row + 1, col)

def parse(file_name):
    lines = []
    with open(file_name) as f:
        for line in f:
            if line[-1] == '\n':
                lines.append(line[0:-1])
            else:
                lines.append(line)
    previous = {}
    original_map = [[map_direction(cell) for cell in line] for line in lines]
    carts = {(row, col): Cart((row, col), cell) for row, line in enumerate(lines) for col, cell in enumerate(line) if cell == '>' or cell == '<' or cell == '^' or cell == 'v'}
    tick = 0
    while True:
        new_carts = {}
        positions = sorted(carts.keys())
        while len(positions) > 0:
            position = positions[0]
            positions = positions[1:]
            cart = carts[position]
            cart.move(original_map)
            if new_carts.get(cart.position):
                new_carts.pop(cart.position, None)
            elif cart.position in positions:
                positions = list(filter(lambda p: p != cart.position, positions))
            else:
                new_carts[cart.position] = cart
        #print(tick)
        #print_map(original_map, carts.values())
        #tick += 1
        carts = new_carts
        #if tick > 10:
        #    break
        #print(len(carts.keys()))
        if len(carts.keys()) < 2:
            #pdb.set_trace()
            print(carts.keys())
            break

def map_direction(direction):
    if direction == '^' or direction == 'v':
        return '|'
    elif direction == '<' or direction == '>':
        return '-'
    return direction

def print_map(lines, carts = []):
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            cart = next((cart for cart in carts if cart.position == (row, col)), None)
            if cart:
                print(cart.direction, end='')
            else:
                print(cell, end='')
        print()

parse('input')
