# Write your solution here
#  return : player won
#    1    :     1
#    2    :     2
#    0    :    tie
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for pieces in row:
            if pieces == 1:
                player1 += 1
            elif pieces == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0