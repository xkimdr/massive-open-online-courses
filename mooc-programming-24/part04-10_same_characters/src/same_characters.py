# Write your solution here
# You can test your function by calling it within the following block


def same_chars(str, i, j):
    return False if i >= len(str) or j >= len(str) else str[i] == str[j]


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
