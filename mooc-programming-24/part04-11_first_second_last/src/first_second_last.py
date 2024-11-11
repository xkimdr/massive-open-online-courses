# Write your solution here
# You can test your function by calling it within the following block


def first_word(str):
    words = str.split(" ")
    return words[0]


def second_word(str):
    words = str.split(" ")
    return words[1]


def last_word(str):
    words = str.split(" ")
    return words[-1]


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
