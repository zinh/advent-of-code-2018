import re

def read(file_name):
    points = []
    with open(file_name) as f:
        p = re.compile(r'position=<(.+)> velocity=<(.+)>')
        for line in f:
            m = p.match(line)
            coords, d = p.match(line).groups()
            x, y = coords.split(',')
            dx, dy = d.split(',')
            points.append(((int(x), int(y)), (int(dx), int(dy))))
    return points

def update(points):
    return [((x + dx, y + dy), (dx, dy)) for ((x, y), (dx, dy)) in points]

def get_coords(points):
    return [(x, y) for ((x, y), _) in points] 

def rectangle(points):
    coords = get_coords(points) #[(x, y) for ((x, y), _) in points]
    x_coords = {x for (x, _) in coords}
    y_coords = {y for (_, y) in coords}
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    return ((x_min, y_min), (x_max, y_max))

# count how many x equal, y equal
def stat(points):
    ((x_min, y_min), (x_max, y_max)) = rectangle(points)
    return (abs(x_max - x_min), abs(y_max - y_min))

def print_img(file_name, points):
    ((x_min, y_min), (x_max, y_max)) = rectangle(points)
    coords = get_coords(points)
    width = abs(x_max - x_min)
    height = abs(y_max - y_min)
    with open(file_name, 'w') as f:
        f.write('P1')
        f.write('\n')
        f.write(f'{width} {height}')
        f.write('\n')
        for y in range(y_min, y_max):
            arr = []
            for x in range(x_min, x_max):
                if (x, y) in coords:
                    arr.append('1')
                else:
                    arr.append('0')
            f.write(" ".join(arr))
            f.write('\n')

def run():
    points = read('input')
    # import pdb; pdb.set_trace()
    tick = 0
    lowest = (100000, 100000)
    while True:
        new_points = update(points)
        coords = stat(new_points)
        if coords[0] * coords[1] < lowest[0] * lowest[1]:
            lowest = coords
        points = new_points
        tick += 1
        if tick == 11000:
            break
    print(lowest)

run()
