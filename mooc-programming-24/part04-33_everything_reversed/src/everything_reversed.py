# Write your solution here


def everything_reversed(strings):
    list = []
    for string in strings:
        list.append(string[::-1])
    return list[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
