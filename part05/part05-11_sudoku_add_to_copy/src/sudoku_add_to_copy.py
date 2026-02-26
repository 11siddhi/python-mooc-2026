# Write your solution here
def print_sudoku(sudoku: list):
  length = len(sudoku)
  for i in range(length):
    if i % 3 == 0 and i != 0:
      print()
    for j in range(length):
      if j % 3 == 0 and j != 0:
        print(" ", end="")
      if sudoku[i][j] == 0:
        print("_", end=" ")
      else:
        print(sudoku[i][j], end=" ")
    print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int)-> list:
  new_sudoku = []
  length = len(sudoku)
  for i in range(length):
    row = []
    for j in range(length):
      if i == row_no and j == column_no:
        row.append(number)
      else:
        row.append(sudoku[i][j])
    new_sudoku.append(row)
  return new_sudoku
  

if __name__ == "__main__":
  sudoku  = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)

  print()
  print("Copy:")
  grid_copy_2 = copy_and_add(sudoku, 2, 0, 2)
  print_sudoku(grid_copy_2)

