# Write your solution here


def print_grid(grid):
    for row in grid:
        for elem in row:
            print(elem, end="")
        print()


def create_grid(num):
    grid = []
    for i in range(2 * num - 1):
        list = []
        for j in range(2 * num - 1):
            list.append("_")
        grid.append(list)
    return grid


def fill_pattern(grid):
    l = len(grid)
    m = l // 2
    grid[m][m] = "A"
    for i in range(1, m + 1):
        for x in range(m - i, m + i + 1):
            for y in range(m - i, m + i + 1):
                if grid[x][y] == "_":
                    grid[x][y] = chr(65 + i)


def main():
    num = int(input("Layers: "))
    grid = create_grid(num)
    fill_pattern(grid)
    print_grid(grid)


main()
