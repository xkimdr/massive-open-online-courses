# write your solution here


def largest():
    max = 0
    with open("numbers.txt") as new_file:
        for line in new_file:
            num = int(line.replace("\n", ""))
            if num > max:
                max = num
    return max


if __name__ == "__main__":
    print(largest())
