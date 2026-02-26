# Write your solution here
def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []
    for row in sudoku:
        num = row[column_no]
        if num in numbers and num > 0:
            return False
        numbers.append(num)
    return True

