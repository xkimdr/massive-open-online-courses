# Write your solution here
from random import sample, shuffle, randint
from string import ascii_lowercase, digits


def generate_strong_password(amount: int, num_flag: bool, special_flag: bool):
    specials = ["!", "?", "=", "+", "-", "(", ")", "#"]
    if num_flag is False and special_flag is False:
        return "".join(sample(ascii_lowercase, amount))
    elif num_flag is True and special_flag is False:
        la = randint(1, amount - 1)
        x = amount - la
        nl = sample(ascii_lowercase, la)
        while x > len(digits):
            y = randint(1, len(digits))
            nl += sample(digits, y)
            x -= y
        nl += sample(digits, x)
        shuffle(nl)
        return "".join(nl)
    elif num_flag is False and special_flag is True:
        la = randint(1, amount - 1)
        x = amount - la
        nl = sample(ascii_lowercase, la)
        while x > len(specials):
            y = randint(1, len(specials))
            nl += sample(specials, y)
            x -= y
        nl += sample(specials, x)
        shuffle(nl)
        return "".join(nl)
    else:
        la = randint(1, amount - 2)
        lb = randint(1, amount - 1 - la)
        nl = (
            sample(ascii_lowercase, la)
            + sample(digits, lb)
            + sample(specials, amount - la - lb)
        )
        shuffle(nl)
        return "".join(nl)


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(16, True, False))
