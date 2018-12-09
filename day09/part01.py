from linked_list import LinkedList

def game(player_count, last_marble):
    lst = LinkedList(0)
    players = [0 for p in range(player_count)]
    current_player = 0
    for step in range(1, last_marble + 1):
        if step % 23 != 0:
            lst.insert(1, step)
        else:
            score = step
            removed = lst.delete(-7)
            score += removed
            players[current_player] += score
        current_player = (current_player + 1) % player_count
    return players
