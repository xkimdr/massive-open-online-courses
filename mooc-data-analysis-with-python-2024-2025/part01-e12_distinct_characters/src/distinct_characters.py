#!/usr/bin/env python3


def distinct_characters(L):
    rD = {}
    for x in L:
        rD[x] = len(set(y for y in x))
    return rD


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
