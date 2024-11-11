# Copy here code of line function from previous exercise
def line(num, str):
    c = "*" if str == "" else str[0]
    print(c * num)


def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size):
        line(i + 1, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
