# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:0>2} eur"

    def __eq__(self, value: object) -> bool:
        if type(value) != Money:
            return False
        if self is value:
            return True
        if self.__euros == value.__euros and self.__cents == value.__cents:
            return True
        return False

    def __add__(self, value: "Money") -> "Money":
        cents = self.__cents + value.__cents
        euros = self.__euros + value.__euros
        if cents > 99:
            euros += cents // 100
            cents = cents % 100
        return Money(euros, cents)

    def __sub__(self, value: "Money") -> "Money":
        cents = self.__cents - value.__cents
        euros = self.__euros - value.__euros
        if cents < 0:
            cents += 100
            euros -= 1
        if euros < 0:
            raise ValueError("a negative result is not allowed")
        return Money(euros, cents)

    def __gt__(self, value: "Money") -> bool:
        if self.__euros > value.__euros:
            return True
        elif self.__euros < value.__euros:
            return False
        else:
            if self.__cents > value.__cents:
                return True
            else:
                return False

    def __lt__(self, value: "Money") -> bool:
        if self.__euros < value.__euros:
            return True
        elif self.__euros > value.__euros:
            return False
        else:
            if self.__cents < value.__cents:
                return True
            else:
                return False

    def __ne__(self, value: object) -> bool:
        if type(value) != Money:
            return True
        if self is value:
            return False
        if self.__euros != value.__euros or self.__cents != value.__cents:
            return True
        return False


if __name__ == "__main__":

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
