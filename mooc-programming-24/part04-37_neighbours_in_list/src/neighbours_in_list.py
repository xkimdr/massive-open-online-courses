# Write your solution here


def longest_series_of_neighbours(nums):
    list = []
    lists = []
    for num in nums:
        if len(list) == 0 or num == list[-1] + 1 or num == list[-1] - 1:
            list.append(num)
        else:
            lists.append(list)
            list = [num]
    lists.append(list)
    # print(lists)
    return len(max(lists, key=len))


if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10, 3]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2]
    print(longest_series_of_neighbours(my_list))

    my_list = []
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
