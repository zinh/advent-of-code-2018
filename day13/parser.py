from graph import Graph

def parser(file_name):
    graph = Graph()
    with open(file_name) as f:
        row = 0
        lines = []
        for l in f:
            lines.append(l[0:-1])
        for row, line in enumerate(lines):
            for col, v in enumerate(line):
                if v == '^' or v == 'v':
                    graph.add_cart((row, col), v)
                    v = '|'
                if v == '<' or v == '>':
                    graph.add_cart((row, col), v)
                    v = '-'
                if v == '-':
                    graph.connect((row, col), (row, col - 1), '←')
                    graph.connect((row, col), (row, col + 1), '→')
                elif v == '|':
                    graph.connect((row, col), (row - 1, col), '↑')
                    graph.connect((row, col), (row + 1, col), '↓')
                elif v == '/':
                    if col - 1 >= 0 and lines[row][col - 1]:
                        graph.connect((row, col), (row, col - 1), '←')
                        graph.connect((row, col), (row - 1, col), '↑')
                    elif lines[row][col + 1]:
                        graph.connect((row, col), (row + 1, col), '↓')
                        graph.connect((row, col), (row, col + 1), '→')
                elif v == '\\':
                    if col - 1 >= 0 and lines[row][col - 1]:
                        graph.connect((row, col), (row, col - 1), '←')
                        graph.connect((row, col), (row + 1, col), '↓')
                    elif lines[row][col + 1]:
                        graph.connect((row, col), (row, col + 1), '→')
                        graph.connect((row, col), (row - 1, col), '↑')
                elif v == '+':
                    graph.connect((row, col), (row, col + 1), '→')
                    graph.connect((row, col), (row, col - 1), '←')
                    graph.connect((row, col), (row + 1, col), '↓')
                    graph.connect((row, col), (row - 1, col), '↑')
                else:
                    pass
                    # create cart
    return graph

g = parser('input')
#while True:
#    t = g.tick()
#    if t:
#        print(t)
#        break
