from board import Board

with open('input1') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

board = Board(lines)
units = board.unit_positions()
for pos, u in units:
    print(board.unit_neighbors(pos))
