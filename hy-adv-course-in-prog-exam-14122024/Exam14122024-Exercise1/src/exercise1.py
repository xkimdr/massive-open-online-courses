# Write your solution to exercise 1 here


class Product:
    def __init__(
        self, name: str, unitprice: float, unit: str, quantity: float = 0
    ) -> None:
        if len(name) < 3:
            raise ValueError("The name must be at least 3 characters long.")
        if unitprice <= 0:
            raise ValueError("The unitprice cannot be negative or zero.")
        if len(unit) == 0:
            raise ValueError("The unit cannot be empty.")
        if quantity < 0:
            raise ValueError("The quantity cannot be negative")
        self.__name = name
        self.__unitprice = unitprice
        self.__unit = unit
        self.__quantity = quantity
        self.__total_price = self.__unitprice * self.__quantity

    @property
    def name(self) -> str:
        return self.__name

    @property
    def unitprice(self) -> float:
        return self.__unitprice

    @property
    def unit(self) -> str:
        return self.__unit

    @property
    def quantity(self) -> float:
        return self.__quantity

    @property
    def total_price(self) -> float:
        return self.__total_price

    def __str__(self) -> str:
        return f"name: {self.name}, unit price: {self.unitprice:.2f}€/{self.unit}, quantity: {self.quantity:.1f}{self.unit}, total price: {self.total_price:.2f}€"

    def __add__(self, product: "Product") -> "Product":
        price = self.total_price + product.total_price
        return Product("dummy", price, "dummy_unit", 1)


if __name__ == "__main__":
    apple = Product("apple", 1.60, "kg", 1.0)
    pear = Product("pear", 2.00, "kg")
    print(apple)
    print(
        "After type conversion apple Product becomes a ",
        len(str(apple)),
        "characters long string",
    )
    print(pear)

    print()

    apple = Product("apple", 1.60, "kg", 2)
    potato = Product("potato", 1.30, "kg", 2)
    banana = Product("banana", 0.90, "kg", 3)
    bread = Product("sourdough bread", 2.70, "piece", 1)
    print("Apple price", apple.total_price)
    print("Total price:", (apple + potato + banana + bread).total_price)
