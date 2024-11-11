# Write your solution here


def length_of_longest(strings):
    mlen = 0
    for string in strings:
        l = len(string)
        if l > mlen:
            mlen = l
    return mlen


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
