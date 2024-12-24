# Write your solution here


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku


def print_sudoku(sudoku: list):
    rc = 0
    lc = 0
    for row in sudoku:
        for elem in row:
            if elem == 0:
                print("_", end="")
            else:
                print(elem, end="")
            print(" ", end="")
            lc += 1
            if lc == 3 or lc == 6:
                print(" ", end="")
        print("")
        lc = 0
        rc += 1
        if rc == 3 or rc == 6:
            print("")


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
