#!/usr/bin/env python3


def transform(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return []
    return list(
        map(lambda x: (int(x[0]) * int(x[1])), zip(s1.split(" "), s2.split(" ")))
    )


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
