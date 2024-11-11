# Write your solution here


# You can test your function by calling it within the following block
def print_many_times(word, num):
    while num != 0:
        print(word)
        num = num - 1


if __name__ == "__main__":
    print_many_times("python", 5)
