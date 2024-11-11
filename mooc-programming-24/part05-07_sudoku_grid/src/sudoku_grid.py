# Write your solution here


def row_correct(sudoku: list, row_no: int):
    nums = [0] * 9
    for i in sudoku[row_no]:
        if i == 0:
            continue
        if i >= 1 or i <= 9:
            nums[i - 1] += 1
        else:
            return False
    for i in nums:
        if i > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    nums = [0] * 9
    for row in sudoku:
        if row[column_no] < 0 or row[column_no] > 9:
            return False
        elif row[column_no] == 0:
            continue
        else:
            nums[row[column_no] - 1] += 1
    for i in nums:
        if i > 1:
            return False
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    nums = [0] * 9
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if 0 < sudoku[i][j] > 9:
                return False
            elif sudoku[i][j] == 0:
                continue
            else:
                nums[sudoku[i][j] - 1] += 1
    for i in nums:
        if i > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
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
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
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
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku = [
        [6, 4, 9, 2, 8, 3, 1, 5, 7],
        [0, 5, 0, 6, 4, 9, 2, 3, 8],
        [2, 3, 8, 1, 5, 7, 6, 4, 9],
        [9, 2, 3, 8, 1, 5, 0, 6, 4],
        [7, 6, 4, 9, 2, 3, 8, 1, 5],
        [8, 1, 5, 7, 0, 4, 9, 2, 0],
        [5, 7, 6, 4, 9, 2, 3, 2, 1],
        [4, 0, 2, 3, 8, 1, 5, 0, 6],
        [3, 0, 1, 5, 0, 6, 4, 9, 0],
    ]

    print(sudoku_grid_correct(sudoku))
