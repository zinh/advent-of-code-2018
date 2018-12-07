from reader import read_file, convert_to_graph

def process():
    graph = convert_to_graph(read_file('input'))
    positions = []
    while graph:
        vs = filter_vertices(vertices, graph)
        selected_vertice = vs[0]
        graph.pop(selected_vertice, None)
        vertices.remove(selected_vertice)
        positions.append(selected_vertice)
    print("".join(positions))

def filter_vertices(vertices, graph):
    lst = list(vertices - {v for arr in graph.values() for v in arr})
    lst.sort(key=lambda x: ord(x))
    return lst

process()
