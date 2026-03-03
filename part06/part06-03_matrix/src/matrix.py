# write your solution here
def read_matrix() -> list:
  m = []
  with open("matrix.txt") as matrix:
    for rows in matrix:
      rows = rows.replace("\n", "")
      rows = rows.split(",")
      m.append(strlist2intlist(rows))
  return m

def strlist2intlist(string_numbers: list) -> list:
  numbers = []
  for str_num in string_numbers:
    numbers.append(int(str_num))
  return numbers

def matrix_sum() -> int:
  total = 0
  matrix = read_matrix()
  for rows in matrix:
    total += sum(rows)
  return total

def matrix_max() -> int:
  big = 0
  file_opened = False

  matrix = read_matrix()
  for rows in matrix:
    n = max(rows)
    if not file_opened or n > big:
      file_opened = True 
      big = n 
  return big
      
def row_sums() -> list:
  row_sums = []
  matrix = read_matrix()
  for rows in matrix:
    row_sums.append(sum(rows))
  return row_sums

if __name__ == "__main__":
  print(matrix_max())
  print(matrix_sum())
  print(row_sums())