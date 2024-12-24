# Write your solution here:

from random import sample


def word_generator(characters: str, length: int, amount: int):
    return ("".join(sample(characters, length)) for _ in range(1, amount + 1))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
