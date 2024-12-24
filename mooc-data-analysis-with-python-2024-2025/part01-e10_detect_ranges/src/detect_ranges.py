#!/usr/bin/env python3


def detect_ranges(tL):
    sL = sorted(tL)
    lL = []
    tL = []
    rL = []
    for x in sL:
        try:
            if tL[-1] + 1 != x:
                lL.append(tL)
                tL = []
        except:
            pass
        tL.append(x)
    if len(tL) != 0:
        lL.append(tL)

    for x in lL:
        if len(x) == 1:
            rL.append(x[0])
        else:
            rL.append((x[0], x[-1] + 1))

    return rL


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
