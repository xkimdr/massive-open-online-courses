#!/usr/bin/env python3


def interleave(*lists):
    rL = []
    for x in list(zip(*lists)):
        rL.extend(x)
    return rL


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ["a", "b", "c"]))


if __name__ == "__main__":
    main()
