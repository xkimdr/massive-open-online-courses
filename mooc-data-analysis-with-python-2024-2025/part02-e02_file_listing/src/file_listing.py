#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename) as file:
        for line in file:
            string = line.strip()
            size = int(re.findall(r"hyad-all\s+([0-9]+)", string)[0])
            month = re.findall(r"[A-Z][a-z]{2}", string)[0]
            day = int(re.findall(r"[A-Z][a-z]{2}\s+([1-3]?[0-9])", string)[0])
            hour = int(re.findall(r"([0-2]?[0-9]):", string)[0])
            minute = int(re.findall(r":([0-6][0-9])", string)[0])
            filename = re.findall(r":[0-6][0-9]\s(.*)$", string)[0]
            tuple = (size, month, day, hour, minute, filename)
            result.append(tuple)
    return result


def main():
    print(file_listing("src/listing.txt"))


if __name__ == "__main__":
    main()
