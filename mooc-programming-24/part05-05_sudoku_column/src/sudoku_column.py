# Write your solution here


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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
