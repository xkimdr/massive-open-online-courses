# Write your solution here


def most_common_character(string):
    ch = ""
    c = 0
    for x in string:
        k = string.count(x)
        if k > c:
            c = k
            ch = x
    return ch


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
