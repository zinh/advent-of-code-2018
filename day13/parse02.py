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
            lines.append(line[0:-1])
    previous = {}
    original_map = [[map_direction(cell) for cell in line] for line in lines]
    carts = {(row, col): Cart((row, col), cell) for row, line in enumerate(lines) for col, cell in enumerate(line) if cell == '>' or cell == '<' or cell == '^' or cell == 'v'}
    while True:
        pos = {}
        new_carts = {}
        for position, cart in carts.items():
            cart.move(original_map)
            if pos.get(cart.position):
                new_carts.pop(cart.position, None)
            else:
                pos[cart.position] = True
                new_carts[cart.position] = cart
        carts = new_carts
        if len(carts.keys()) == 1:
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
