# Write your solution here


def longest(strings: list):
    return max(strings, key=len)


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
