class Vertice:
    def __init__(self, label):
        self.label = label

    def left(self, vertice):
        self.left = vertice

    def right(self, vertice):
        self.right = vertice

    def top(self, vertice):
        self.top = vertice

    def bottom(self, vertice):
        self.bottom = vertice

class Graph:
    def __init__(self):
        self.vertices = {}

    def connect(self, label1, label2):
        v1 = self.vertices.setdefault(label1, Vertice(label1, []))
        v2 = self.vertices.setdefault(label2, Vertice(label2, []))

class Cart:
    def __init__(self, vertice):
        pass

    def run(self):
        pass

def parser(file_name):
    graph = Graph()
    with open(file_name) as f:
        row = 0
        for l in f:
            lines.append(l[0:-1])
        for row, line in enumerate(lines):
            for col, v in enumerate(line):
                if v == '-':
                    graph.connect((row, col), (row, col - 1))
                    graph.connect((row, col), (row, col + 1))
                elif v == '|':
                    graph.connect((row, col), (row - 1, col))
                    graph.connect((row, col), (row + 1, col))
                elif v == '/':
                    graph.connect((row, col), (row, col))
                elif v == '\\':
                  pass
                elif v == '+':
                    graph.connect((row, col), (row, col + 1))
                    graph.connect((row, col), (row, col - 1))
                    graph.connect((row, col), (row + 1, col))
                    graph.connect((row, col), (row - 1, col))
                else:
                    pass
                    # create cart

    return graph
