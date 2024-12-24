#!/usr/bin/env python3


def triple(x):
    return x * 3


def square(x):
    return x**2


def main():
    for x in range(1, 11):
        a = triple(x)
        b = square(x)
        if b <= a:
            print(f"triple({x})=={a} square({x})=={b}")
        else:
            break


if __name__ == "__main__":
    main()
