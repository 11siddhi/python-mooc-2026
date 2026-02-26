# Write your solution here
# x: column | y: row
def play_turn(game_board: list, x: int, y: int, piece: str):
  length = len(game_board)
  if x < 0 or y < 0 or not x < length or not y < length: 
    return False

  if game_board[y][x]:
    return False
  else: 
    game_board[y][x] = piece
    return True
    

if __name__ == "__main__":
  game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
  print(play_turn(game_board, 2, 2, "X"))
  print(game_board)

  game_board = [['O', 'O', ''], ['X', '', ''], ['O', '', 'O']]
  print(play_turn(game_board, 3, 0, "X"))
  print(game_board)