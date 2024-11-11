# Write your solution here


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def factorials(n: int):
    dict = {}
    for i in range(1, n + 1):
        dict[i] = factorial(i)
    return dict


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
