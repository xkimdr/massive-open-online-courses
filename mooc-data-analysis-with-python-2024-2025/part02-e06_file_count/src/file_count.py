#!/usr/bin/env python3

import sys
import re


def file_count(filename):
    cc = 0
    lc = 0
    wc = 0
    with open(filename) as file:
        for line in file:
            cc += len(line)
            lc += 1
            wc += len(re.findall(r"\S+", line.strip()))
    return (lc, wc, cc)


def main():
    for filename in sys.argv[1:]:
        result = file_count(filename)
        print(f"{result[0]}\t{result[1]}\t{result[2]}\t{filename}")


if __name__ == "__main__":
    main()
