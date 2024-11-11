# Write your solution here


def transpose(matrix: list):
    t = []
    for row in matrix:
        t.append(row[:])
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            matrix[i][j] = t[j][i]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in m:
        print(row)
    print("")
    transpose(m)
    for row in m:
        print(row)
