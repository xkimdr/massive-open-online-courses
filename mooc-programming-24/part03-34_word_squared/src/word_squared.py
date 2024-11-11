# Write your solution here


def squared(word, num):
    x = 0
    for i in range(num):
        for j in range(num):
            print(word[x], end="")
            if x + 1 == len(word):
                x = 0
            else:
                x = x + 1

        print("")


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
