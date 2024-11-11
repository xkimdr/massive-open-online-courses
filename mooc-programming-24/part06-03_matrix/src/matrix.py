# write your solution here


def parse():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            row = []
            list = line.replace("\n", "").split(",")
            for x in list:
                row.append(int(x))
            matrix.append(row)
    return matrix


def matrix_sum():
    matrix = parse()
    s = 0
    for row in matrix:
        s += sum(row)
    return s


def matrix_max():
    matrix = parse()
    m = 0
    rm = []
    for row in matrix:
        rm.append(max(row))
    return max(rm)


def row_sums():
    matrix = parse()
    rs = []
    for row in matrix:
        rs.append(sum(row))
    return rs


if __name__ == "__main__":
    pass
