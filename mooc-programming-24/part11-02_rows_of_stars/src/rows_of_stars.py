# WRITE YOUR SOLUTION HERE:


def rows_of_stars(numbers: list):
    return ["*" * num for num in numbers]


if __name__ == "__main__":
    rows = rows_of_stars([1, 2, 3, 4])
    for row in rows:
        print(row)

    print()

    rows = rows_of_stars([4, 3, 2, 1, 10])
    for row in rows:
        print(row)
