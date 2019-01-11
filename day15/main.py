from board import Game

with open('input1') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

game = Game(lines)
print(game)
game.turn()
print(game)
#units = board.unit_positions()
#for u in units:
#    board.move(u)
#print('===')
#print(board)
