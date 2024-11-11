# write your solution here


def read_fruits():
    dict = {}
    with open("fruits.csv") as fruits:
        for fruit in fruits:
            list = fruit.replace("\n", "").split(";")
            dict[list[0]] = float(list[1])
    return dict


if __name__ == "__main__":
    print(read_fruits())
