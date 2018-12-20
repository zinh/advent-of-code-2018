from board import Board

with open('input1') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

board = Board(lines)
print(board)
units = board.unit_positions()
for u in units:
    board.move(u)
print('===')
print(board)
