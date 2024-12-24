# WRITE YOUR SOLUTION HERE:


class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        dict = {}
        for x in my_list:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        return sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        dict = {}
        for x in my_list:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        sum = 0
        for x in list:
            if x[1] < 2:
                break
            sum += 1
        return sum


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
