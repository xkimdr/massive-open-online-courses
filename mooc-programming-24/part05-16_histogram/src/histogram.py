# Write your solution here


def histogram(word):
    dict = {}
    for c in word:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    for k, v in dict.items():
        print(f"{k} {"*" * v}")


if __name__ == "__main__":
    histogram("statistically")
