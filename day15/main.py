from game import Game
import pdb

with open('input4') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

game = Game(lines)
print(game)
turn_count = 0
while not game.turn():
    pdb.set_trace()
    turn_count += 1
print(game)
print(turn_count, game.total_hit_point())
game.print_hit_point()
#units = board.unit_positions()
#for u in units:
#    board.move(u)
#print('===')
#print(board)
