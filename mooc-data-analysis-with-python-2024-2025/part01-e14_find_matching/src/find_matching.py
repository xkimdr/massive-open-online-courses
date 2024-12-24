#!/usr/bin/env python3


def find_matching(L, pattern):
    rL = []
    for i, x in enumerate(L):
        if pattern in x:
            rL.append(i)
    return rL


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
