# Write your solution here


def no_shouting(strings):
    list = []
    for string in strings:
        if not string.isupper():
            list.append(string)
    return list


if __name__ == "__main__":
    my_list = [
        "ABC",
        "def",
        "UPPER",
        "ANOTHERUPPER",
        "lower",
        "another lower",
        "Capitalized",
    ]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
