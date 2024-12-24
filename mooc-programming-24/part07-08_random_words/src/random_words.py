# Write your solution here

from random import sample


def word_list():
    wl = []
    with open("words.txt") as file:
        for line in file:
            wl.append(line.strip())
    return wl


def words(n: int, beginning: str):
    wl = word_list()
    nl = []
    for word in wl:
        if beginning == word[: len(beginning)] and word not in nl:
            nl.append(word)
    if n > len(nl):
        raise ValueError(
            "There are not enough words beginning with the specified string"
        )
    return sample(nl, n)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
