# Write your solution here


def chessboard(num):
    for i in range(num):
        for j in range(num):
            if (i + j + 1) % 2 == 0:
                print(0, end="")
            else:
                print(1, end="")

        print("")


# Testing the function
if __name__ == "__main__":
    chessboard(3)
