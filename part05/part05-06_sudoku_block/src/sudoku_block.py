# Write your solution here
def block_correct(sudoku: list, row_no: int, col_no: int) -> bool:
    block = 3
    numbers = []
    for r in range(block):
        for c in range(block):
            num = sudoku[row_no+r][col_no+c]
            if num in numbers and num > 0:
                return False
            numbers.append(num)
    return True

if __name__ == "__main__":
    sudoku = [
        [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
        [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
        [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
        [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
        [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
        [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
        [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
        [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
        [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
    ]
    print(block_correct(sudoku, 0, 0))