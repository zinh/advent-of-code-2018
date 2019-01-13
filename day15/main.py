from game import Game
import pdb

with open('input') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

elf_win = False
attack_point = 3
while not elf_win:
    game = Game(lines, attack_point)
    turn_count, total_hit_point = game.run()
    elf_win = game.elf_win
    if elf_win:
        print(attack_point, turn_count, total_hit_point)
    attack_point += 1
