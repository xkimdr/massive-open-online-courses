#!/usr/bin/env python3


class Prepend(object):
    # Add the methods of the class here
    def __init__(self, string: str) -> None:
        self.__string = string

    def write(self, string: str) -> None:
        print(self.__string + string)


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
