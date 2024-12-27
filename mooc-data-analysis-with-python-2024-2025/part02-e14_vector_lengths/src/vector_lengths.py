#!/usr/bin/env python3

import numpy as np

# import scipy.linalg


def vector_lengths(a):
    x = np.square(a)
    y = np.sum(x, axis=1)
    z = np.sqrt(y)
    return z


def main():
    vectors = np.arange(12).reshape(3, 4)
    print(vector_lengths(vectors))


if __name__ == "__main__":
    main()
