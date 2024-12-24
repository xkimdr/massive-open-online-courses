# WRITE YOUR SOLUTION HERE:


class SimpleDate:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __in_days(self):
        return self.__year * 12 * 30 + self.__month * 30 + self.__day

    def __in_simpledate(self, x: int):
        year = x // (12 * 30)
        month = (x % (12 * 30)) // 30
        day = (x % (12 * 30)) % 30
        return SimpleDate(day, month, year)

    def __eq__(self, value: "SimpleDate") -> bool:
        return self.__in_days() == value.__in_days()

    def __ne__(self, value: "SimpleDate") -> bool:
        return self.__in_days() != value.__in_days()

    def __gt__(self, value: "SimpleDate") -> bool:
        return self.__in_days() > value.__in_days()

    def __lt__(self, value: "SimpleDate") -> bool:
        return self.__in_days() < value.__in_days()

    def __str__(self) -> str:
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __add__(self, value: int) -> "SimpleDate":
        x = self.__in_days() + value
        return self.__in_simpledate(x)

    def __sub__(self, value: "SimpleDate") -> "SimpleDate":
        x = self.__in_days() - value.__in_days()
        return abs(x)


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
