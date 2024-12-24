# Write your solution here

from random import choice


def getDie(die: str):
    if die == "A":
        return [3, 3, 3, 3, 3, 6]
    elif die == "B":
        return [2, 2, 2, 5, 5, 5]
    else:
        return [1, 4, 4, 4, 4, 4]


def roll(die: str):
    l = getDie(die)
    return choice(l)


def play(die1: str, die2: str, times: int):
    a = 0
    b = 0
    c = 0
    for i in range(0, times):
        x = roll(die1)
        y = roll(die2)
        if x > y:
            a += 1
        elif x < y:
            b += 1
        else:
            c += 1
    return (a, b, c)


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
