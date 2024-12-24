# Write your solution here
# You can test your function by calling it within the following block


def spruce(num):
    print("a spruce!")
    for i in range(num):
        print(f"{(num - 1 - i) * " "}{(2 * i + 1) * "*"}")
    print(f"{" " * (num - 1)}*")


if __name__ == "__main__":
    spruce(5)
