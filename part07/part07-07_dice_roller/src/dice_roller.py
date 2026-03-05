# Write your solution here
from random import choice

def roll(die: str) -> int:
  A = [3, 3, 3, 3, 3, 6]
  B = [2, 2, 2, 5, 5, 5]
  C = [1, 4, 4, 4, 4, 4] 

  if die == "A":
    return choice(A)
  if die == 'B':
    return choice(B)
  if die == 'C':
    return choice(C)

def play(die1: str, die2: str, times: int) -> tuple:
  player1_won = 0
  player2_won = 0
  tie = 0

  for i in range(times):
    player1 = roll(die1)
    player2 = roll(die2)
    if player1 > player2:
      player1_won += 1
    elif player2 > player1:
      player2_won += 1
    else:
      tie += 1
      
  return (player1_won, player2_won, tie)


if __name__ == "__main__":
  # for i in range(20):
  #     print(roll("A"), " ", end="")
  # print()
  # for i in range(20):
  #     print(roll("B"), " ", end="")
  # print()
  # for i in range(20):
  #     print(roll("C"), " ", end="")
  result = play("A", "C", 1000)
  print(result)
  result = play("B", "B", 1000)
  print(result)
