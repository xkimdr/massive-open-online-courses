#!/usr/bin/env python3


def reverse_dictionary(d):
    rD = {}
    for k, v in d.items():
        for x in v:
            if not x in rD:
                rD[x] = []
            rD[x].append(k)
    return rD


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }

    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
