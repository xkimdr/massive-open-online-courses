#!/usr/bin/env python3

import numpy as np


def diamond(n):
    a = np.eye(n, dtype=int)
    b = a[:, 1::][:, ::-1]
    c = np.concatenate((b, a), axis=1)
    d = c[:-1, :][::-1, :]
    e = np.concatenate((c, d))
    return e


def main():
    print(diamond(3))


if __name__ == "__main__":
    main()
