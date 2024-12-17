# Write your solution to exercise 1 here


def main():
    strings = []
    while True:
        string = input("Enter a string: ")
        if len(string) == 0:
            break
        strings.append(string)

    min_no_of_chars = int(input("Minimum number of characters: "))

    cdict = {}
    for string in strings:
        for x in string:
            if x in cdict:
                cdict[x] += 1
            else:
                cdict[x] = 1

    sarray = sorted(cdict.items(), key=lambda x: x[1], reverse=True)
    print("Characters in order of occurrence:")
    for x in sarray:
        if x[1] >= min_no_of_chars:
            print(f'  Character "{x[0]}" was entered {x[1]} times')
        else:
            break


if __name__ == "__main__":
    main()
