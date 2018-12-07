from reader import read_file

def filter_vertices(vertices, graph):
    lst = list(vertices - {v for arr in graph.values() for v in arr})
    lst.sort(key=lambda x: ord(x))
    return lst

def process():
    edges = read_file('input')
    vertices = {v for edge in edges for v in edge}
    duration = {v: (60 + ord(v) - 64) for v in vertices}
    graph = {vertice: [] for vertice in vertices}
    positions = []
    for pre, pos in edges:
        graph[pre].append(pos)
    max_worker = 5
    workers = [None for i in range(0, max_worker)]
    tick = 0
    while True:
        print(tick, workers)
        # Update worker
        new_workers = []
        # import pdb; pdb.set_trace()
        for worker in workers:
            if worker is None:
                new_workers.append(None)
            else:
                if duration[worker] == 1:
                    graph.pop(worker, None)
                    vertices.remove(worker)
                    new_workers.append(None)
                else:
                    duration[worker] -= 1
                    new_workers.append(worker)
        workers = new_workers
        # select next task
        next_vertices = list(filter(lambda x: x not in workers, filter_vertices(vertices, graph)))
        new_workers = []
        #if tick == 7:
        #    import pdb; pdb.set_trace()
        for idx, worker in enumerate(workers):
            if worker is None and next_vertices:
                new_workers.append(next_vertices.pop(0))
            else:
                new_workers.append(worker)
        workers = new_workers
        #import pdb; pdb.set_trace()
        #print(tick)
        if not graph:
            break
        tick += 1
    print(tick)

process()
