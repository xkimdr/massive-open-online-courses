# Write your solution here

from string import ascii_letters, punctuation


def separate_characters(my_string: str):
    x, y, z = "", "", ""
    for c in my_string:
        if c in ascii_letters:
            x += c
        elif c in punctuation:
            y += c
        else:
            z += c
    return x, y, z


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
