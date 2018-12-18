import os

class Forest:
    def __init__(self, lines):
        self.forest = lines
        self.max_row = len(lines)
        self.max_col = len(lines[0])

    def iterate(self):
        self.forest = [[self.generate((row_no, col_no), cell) for col_no, cell in enumerate(row)] for row_no, row in enumerate(self.forest)]
                
    def generate(self, pos, cell):
        adjs = self.adjacents(pos)
        if cell == '.':
            if len([1 for a in adjs if a == '|']) >= 3:
                return '|'
            else:
                return cell
        elif cell == '|':
            if len([1 for a in adjs if a == '#']) >= 3:
                return '#'
            else:
                return cell
        elif cell == '#':
            tree = len([1 for a in adjs if a == '|'])
            lumber = len([1 for a in adjs if a == '#'])
            if tree >= 1 and lumber >= 1:
                return cell
            else:
                return '.'

    def adjacents(self, position):
        row, col = position
        ads = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), 
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        return [self.forest[r][c] for r, c in ads if r >= 0 and r < self.max_row and c >= 0 and c < self.max_col]

    def value(self):
        tree = len([1 for row in self.forest for cell in row if cell == '|'])
        lumber = len([1 for row in self.forest for cell in row if cell == '#'])
        return tree * lumber

    def to_s(self):
        return '\n'.join([''.join(row) for row in self.forest])

    def __repr__(self):
        return self.to_s()

    def __str__(self):
        return self.to_s()

def process_file(file_name):
    a = []
    with open(file_name) as f:
        for line in f:
            a.append(line.strip())
    return a

forest = Forest(process_file('input'))
for i in range(0, 1000):
    forest.iterate()
    os.system('cls')
    print(forest)
