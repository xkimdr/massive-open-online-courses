# Write your solution here:


class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"

    def name(self) -> str:
        return self.__name

    def weight(self) -> int:
        return self.__weight


class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.__items = []
        self.__max_weight = max_weight

    def add_item(self, item: Item) -> None:
        if self.weight() + item.weight() > self.__max_weight:
            return
        self.__items.append(item)

    def weight(self) -> int:
        sum = 0
        for item in self.__items:
            sum += item.weight()
        return sum

    def __str__(self) -> str:
        num = len(self.__items)
        return f"{num} {"items" if num != 1 else "item"} ({self.weight()} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        required_item = self.__items[0]
        for item in self.__items:
            if item.weight() > required_item.weight():
                required_item = item
        return required_item


class CargoHold:
    def __init__(self, max_weight: int) -> None:
        self.__suitcases = []
        self.__max_weight = max_weight

    def add_suitcase(self, suitcase: Suitcase) -> None:
        if self.__weight() + suitcase.weight() > self.__max_weight:
            return
        self.__suitcases.append(suitcase)

    def __weight(self) -> int:
        sum = 0
        for suitcase in self.__suitcases:
            sum += suitcase.weight()
        return sum

    def __str__(self) -> str:
        num = len(self.__suitcases)
        return f"{num} {"suitcases" if num != 1 else "suitcase"}, space for {self.__max_weight - self.__weight()} kg"

    def print_items(self) -> None:
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
