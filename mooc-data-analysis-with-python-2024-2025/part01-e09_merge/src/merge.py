#!/usr/bin/env python3


def merge(L1, L2):
    c = 0
    k = 0
    n = len(L1)
    m = len(L2)
    L = []
    while True:
        if c == n and k == m:
            break
        elif c == n and k != m:
            L.append(L2[k])
            k += 1
        elif c != n and k == m:
            L.append(L1[c])
            c += 1
        elif L1[c] < L2[k]:
            L.append(L1[c])
            c += 1
        elif L1[c] > L2[k]:
            L.append(L2[k])
            k += 1
        else:
            L.append(L1[c])
            L.append(L2[k])
            c += 1
            k += 1
    return L


def main():
    print(merge([1, 2, 3], [2, 3, 6, 7]))


if __name__ == "__main__":
    main()
