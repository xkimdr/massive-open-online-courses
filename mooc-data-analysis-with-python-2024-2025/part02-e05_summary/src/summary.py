#!/usr/bin/env python3

import sys
from math import sqrt


def summary(filename):
    values = []
    with open(filename) as file:
        for line in file:
            try:
                value = float(line.strip())
                values.append(value)
            except:
                pass
    n = len(values)
    if n != 0:
        total = sum(values)
        average = total / n
        standard_deviation = sqrt(
            sum([(value - average) ** 2 for value in values]) / (n - 1)
        )
        return (total, average, standard_deviation)
    else:
        return (0, 0, 0)


def main():
    for filename in sys.argv[1:]:
        result = summary(filename)
        output = f"File: {filename} Sum: {result[0]:.6f} Average: {result[1]:.6f} Stddev: {result[2]:.6f}"
        print(output)


if __name__ == "__main__":
    main()
