# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num, str):
    c = "*" if str == "" else str[0]
    print(c * num)


def shape(tsize, tch, ssize, sch):
    for i in range(tsize):
        line(i + 1, tch)
    for i in range(ssize):
        line(tsize, sch)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
