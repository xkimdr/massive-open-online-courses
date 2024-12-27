#!/usr/bin/env python3

import re


def extract_numbers(s: str):
    result = []
    for x in s.split(" "):
        try:
            if re.match(r"^-?\d+(\.\d+)?$", x):
                result.append(float(x))
        except:
            pass
    return result


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
