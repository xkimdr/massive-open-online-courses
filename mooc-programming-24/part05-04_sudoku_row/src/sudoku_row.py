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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
