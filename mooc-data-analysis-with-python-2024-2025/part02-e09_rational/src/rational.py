#!/usr/bin/env python3


class Rational(object):
    def __init__(self, a: int, b: int) -> None:
        if b == 0:
            raise ValueError("Denominator can't be 0")
        self.__a = a
        self.__b = b

    @property
    def a(self) -> int:
        return self.__a

    @property
    def b(self) -> int:
        return self.__b

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, value: "Rational") -> "Rational":
        return Rational(self.a * value.b + value.a * self.b, self.b * value.b)

    def __sub__(self, value: "Rational") -> "Rational":
        return Rational(self.a * value.b - value.a * self.b, self.b * value.b)

    def __mul__(self, value: "Rational") -> "Rational":
        return Rational(self.a * value.a, self.b * value.b)

    def __truediv__(self, value: "Rational") -> "Rational":
        return Rational(self.a * value.b, self.b * value.a)

    def __eq__(self, value: "Rational") -> bool:
        return self.a * value.b == value.a * self.b

    def __lt__(self, value: "Rational") -> bool:
        result = self - value
        return result.a / result.b < 0

    def __gt__(self, value: "Rational") -> bool:
        result = self - value
        return result.a / result.b > 0


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
