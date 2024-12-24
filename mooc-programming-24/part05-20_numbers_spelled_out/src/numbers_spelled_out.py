# Write your solution here


def number_to_word(number):
    l1 = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
    ]
    l2 = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if 0 <= number <= 20:
        return f"{l1[number]}"
    elif 21 <= number <= 99:
        ones = number % 10
        tens = number // 10
        if ones != 0:
            return f"{l2[tens]}-{l1[ones]}"
        else:
            return f"{l2[tens]}"


def dict_of_numbers():
    dict = {}
    for i in range(0, 100):
        dict[i] = number_to_word(i)
    return dict


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
