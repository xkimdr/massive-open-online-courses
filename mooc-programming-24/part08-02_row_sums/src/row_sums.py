# Write your solution here


def row_sums(my_matrix: list):
    index = 0
    for row in my_matrix:
        my_matrix[index].append(sum(row))
        index += 1


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
