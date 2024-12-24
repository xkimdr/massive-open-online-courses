# Write your solution here
from math import sqrt


def prime_numbers():
    number = 2
    while True:
        if number in [2, 3]:
            yield number
        else:
            for x in range(2, int(sqrt(number)) + 1):
                if number % x == 0:
                    break
            else:
                yield number
        number += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
