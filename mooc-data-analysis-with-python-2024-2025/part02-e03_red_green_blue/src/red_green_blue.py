#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename) as file:
        for line in file:
            if re.match(r"^!.*$", line):
                continue
            string = line.strip()
            parts = re.split(r"\s+", string)
            a = "\t".join(parts[:4])
            b = parts[4:]
            if len(b) == 0:
                result.append(a)
            else:
                result.append(a + " " + " ".join(b))
    return result


def main():
    for x in red_green_blue():
        print(repr(x))


if __name__ == "__main__":
    main()
