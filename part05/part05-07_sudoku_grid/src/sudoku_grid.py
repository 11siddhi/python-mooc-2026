# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    for num in row:
        if row.count(num) > 1 and num != 0:
            return False
    return True

def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []
    for row in sudoku:
        num = row[column_no]
        if num in numbers and num > 0:
            return False
        numbers.append(num)
    return True

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

def sudoku_grid_correct(sudoku: list) -> bool:
    block = 3  
    length = len(sudoku)
    for i in range(length):
        if i % block == 0: # runs only when row is 0, 3, 6
            for c in range(block):
                if not block_correct(sudoku, i, c*block):
                    return False
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
    return True
        

if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
    [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
    [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
    [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
    [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
    [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
    [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
    [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
    [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]
    print(sudoku_grid_correct(sudoku3))