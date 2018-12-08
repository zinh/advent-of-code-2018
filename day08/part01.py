import sys

sys.setrecursionlimit(20000)

class Node:
    def __init__(self, meta, children):
        self.meta = meta
        self.children = children

    def sum_meta(self):
        return sum(self.meta) + sum([child.sum_meta() for child in self.children])

    def flatten(self):
        return [len(self.children)] + [len(self.meta)] + [c for child in self.children for c in child.flatten() ]  + self.meta

    def value(self):
        if self.children:
            s = 0
            for m in self.meta:
                if m <= 0 or m > len(self.children):
                    next
                else:
                    s += self.children[m - 1].value()
            return s
        else:
            return sum(self.meta)

def reader(file_name):
    with open(file_name) as f:
        content = f.read()
        return [int(n) for n in content.strip().split(' ')]

def convert_to_tree(data):
    #import pdb; pdb.set_trace()
    children_count = data[0]
    meta_count = data[1]
    if children_count == 0:
        if meta_count == 0:
            return (Node([], []), data[2:])
        else:
            return (Node(data[2:(2 + meta_count)], []), data[2 + meta_count:])
    else:
        remain_data = data[2:]
        children = []
        for c in range(0, children_count):
            child, remain_data = convert_to_tree(remain_data)
            children.append(child)
        if meta_count == 0:
            return Node([], children), remain_data
        else:
            return Node(remain_data[0:meta_count], children), remain_data[meta_count:]

#data = reader('input')
#root, _ = convert_to_tree(data)
#print(root.value())
