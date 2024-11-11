# Write your solution here


def who_won(game_board: list):
    p1 = 0
    p2 = 0
    for row in game_board:
        for elem in row:
            if elem == 1:
                p1 += 1
            elif elem == 2:
                p2 += 1
    if p1 > p2:
        return 1
    elif p1 < p2:
        return 2
    else:
        return 0


if __name__ == "__main__":
    list = [
        [2, 2, 0, 2, 1, 0, 2, 2, 0],
        [2, 0, 2, 0, 1, 1, 1, 1, 2],
        [2, 1, 2, 2, 0, 2, 1, 2, 1],
        [2, 1, 2, 1, 0, 1, 1, 1, 2],
        [0, 2, 1, 1, 1, 0, 1, 2, 1],
        [2, 2, 1, 1, 2, 2, 2, 0, 0],
        [1, 0, 0, 2, 0, 0, 2, 1, 1],
        [2, 0, 0, 1, 2, 0, 2, 1, 2],
        [2, 1, 2, 0, 2, 1, 2, 1, 2],
    ]
    print(who_won(list))

    list = [[1]]
    print(who_won(list))

    list = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(list))
