# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning if beginning % 2 == 0 else beginning + 1
    while number <= maximum:
        yield number
        number += 2


if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)
