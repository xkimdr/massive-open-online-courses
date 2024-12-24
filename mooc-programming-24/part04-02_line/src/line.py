# Write your solution here
# You can test your function by calling it within the following block


def line(num, str):
    c = "*" if str == "" else str[0]
    print(c * num)


if __name__ == "__main__":
    line(5, "")
