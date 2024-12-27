#!/usr/bin/env python3

import re


def file_extensions(filename):
    x = []
    y = {}
    with open(filename) as file:
        for line in file:
            t = re.findall(r"(^.*?(\.([^\.]+))?)$", line.strip())[0]
            e = t[2]
            f = t[0]
            if len(t[1]) != 0:
                if e not in y:
                    y[e] = []
                y[e].append(f)
            else:
                x.append(f)
    return (x, y)


def main():
    x, y = file_extensions("src/filenames.txt")
    print(f"{len(x)} files with no extension")
    for a, b in sorted(y.items(), key=lambda k: (len(k[1]), k[0])):
        print(a, len(b))


if __name__ == "__main__":
    main()
