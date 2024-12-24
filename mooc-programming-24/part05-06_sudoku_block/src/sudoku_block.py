# Write your solution here


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


if __name__ == "__main__":
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
