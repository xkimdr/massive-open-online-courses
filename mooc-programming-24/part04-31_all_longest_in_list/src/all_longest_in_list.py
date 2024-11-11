# Write your solution here


def all_the_longest(list):
    mlist = []
    ml = len(max(list, key=len))
    for item in list:
        if len(item) == ml and item not in mlist:
            mlist.append(item)
    return mlist


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
