# Write your solution here
def print_matrix(matrix: list):
  for row in matrix:
    for col in row:
      print(col, end=" ")
    print()

def transpose(matrix: list):
  length = len(matrix)
  for row in range(length):
    for col in range(length):
      if not col > row:
        continue
      temp = matrix[row][col]
      matrix[row][col] = matrix[col][row]
      matrix[col][row] = temp
      


if __name__ == "__main__":
  # matrix = [[1,2,3], [4,5,6], [7,8,9]]
  # print_matrix(matrix)
  # transpose(matrix)
  # print("---------")
  # print_matrix(matrix)
  # print("---------")

  # matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
  # print_matrix(matrix)
  # transpose(matrix)
  # print("---------")
  # print_matrix(matrix)
  # print("---------")

  matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
  print_matrix(matrix)
  transpose(matrix)
  print("---------")
  print_matrix(matrix)



