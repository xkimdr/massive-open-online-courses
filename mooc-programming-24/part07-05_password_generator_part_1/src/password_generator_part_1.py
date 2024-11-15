# Write your solution here
from string import ascii_lowercase
from random import sample


def generate_password(amount: int):
    return "".join(sample(ascii_lowercase, amount))


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
