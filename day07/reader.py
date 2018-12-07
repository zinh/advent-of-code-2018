import re

def read_file(file_name):
    edges = []
    with open(file_name) as f:
        g = re.compile(r'Step (\w) must be finished before step (\w)')
        for line in f:
            pre, des = g.match(line).groups()
            edges.append([pre, des])
    return edges
