# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    for num in row:
        if row.count(num) > 1 and num != 0:
            return False
    return True