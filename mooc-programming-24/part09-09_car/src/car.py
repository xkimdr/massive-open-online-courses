# WRITE YOUR SOLUTION HERE:


class Car:
    def __init__(self) -> None:
        self.__fuel = 0
        self.__travelled = 0

    def fill_up(self) -> None:
        self.__fuel = 60

    def drive(self, km: int) -> None:
        if km <= self.__fuel:
            self.__travelled += km
            self.__fuel -= km
        else:
            self.__travelled += self.__fuel
            self.__fuel = 0

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__travelled} km, petrol remaining {self.__fuel} litres"


if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
