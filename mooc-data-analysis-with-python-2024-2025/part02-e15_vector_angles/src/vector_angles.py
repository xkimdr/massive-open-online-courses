#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    a = np.sum(np.multiply(X, Y))
    b = np.sqrt(np.sum(np.square(X)))
    c = np.sqrt(np.sum(np.square(Y)))
    d = np.divide(a, np.multiply(b, c))
    e = np.arccos(d)
    f = np.divide(np.multiply(180, e), np.pi)
    return f


def main():
    np.random.seed(0)
    X = np.random.randint(0, 10, (2, 3))
    Y = np.random.randint(0, 10, (2, 3))
    print(X)
    print(Y)
    print(vector_angles(X, Y))


if __name__ == "__main__":
    main()
