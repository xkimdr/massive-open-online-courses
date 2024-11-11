# Write your solution here


def no_vowels(string):
    str = string
    for c in ["a", "e", "i", "o", "u"]:
        str = str.replace(c, "")
    return str


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
