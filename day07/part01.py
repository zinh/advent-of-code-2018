from reader import read_file

def process():
    edges = read_file('input')
    vertices = {v for edge in edges for v in edge}
    graph = {vertice: [] for vertice in vertices}
    positions = []
    for pre, pos in edges:
        graph[pre].append(pos)
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
