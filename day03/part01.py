import re

n = 1000
grid = [[0 for j in range(0, n)] for i in range(0, n)]

with open('input') as f:
    p = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for line in f:
        _, left, top, width, height = [int(v) for v in p.match(line).groups()]
        for x in range(left + 1, left + width + 1):
            for y in range(top + 1, top + height + 1):
                grid[x][y] += 1

with open('input') as f:
    p = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for line in f:
        claim_no, left, top, width, height = [int(v) for v in p.match(line).groups()]
        if all([grid[x][y] <= 1 for x in range(left + 1, left + width + 1) for y in range(top + 1, top + height + 1)]):
            print(claim_no)
