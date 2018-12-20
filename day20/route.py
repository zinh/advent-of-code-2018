def parse(file_name):
    routes = []
    with open(file_name) as f:
        f.read(1)
        c = f.read(1)
        while c != '$':
            routes.append(c)
            c = f.read(1)

def main():
    route = parse('input1')
    arr = {}
