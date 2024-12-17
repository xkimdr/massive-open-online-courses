# Write your solution to exercise 3 here


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


def parse(string: str) -> Product:
    try:
        parts = string.split(", ")
        name = parts[0].split(": ")[1]
        temp = parts[1].split(": ")[1].split("€")
        unitprice = float(temp[0])
        unit = temp[1][1:]
        quantity = float(parts[2].split(": ")[1][: -len(unit)])
        return Product(name, unitprice, unit, quantity)
    except:
        raise ValueError


def save_data(string_list: list, filename: str = "shoppinglist.csv") -> None:
    with open(filename, "w") as file:
        for string in string_list:
            x: Product = parse(string)
            file.write(
                f"{x.name};{x.unitprice:.2f};{x.unit};{x.quantity:.1f};{x.total_price:.2f}\n"
            )


def load_data(filename: str = "shoppinglist.csv") -> None:
    string_list = []
    try:
        with open(filename) as file:
            for line in file:
                try:
                    parts = line.strip().split(";")
                    x = Product(parts[0], float(parts[1]), parts[2], float(parts[3]))
                    string_list.append(f"{x}")
                except:
                    raise ValueError
    except FileNotFoundError:
        pass

    return string_list


if __name__ == "__main__":
    string_list2 = load_data(filename="file.csv")
    for i in range(len(string_list2)):
        print(string_list2[i])

    string_list = [
        "name: apple, unit price: 1.60€/kg, quantity: 2.2kg, total price: 3.52€",
        "name: potato, unit price: 1.30€/kg, quantity: 5.0kg, total price: 6.50€",
        "name: banana, unit price: 0.95€/kg, quantity: 1.2kg, total price: 1.14€",
        "name: milk, unit price: 1.25€/l, quantity: 2.0l, total price: 2.50€",
        "name: rye bread, unit price: 2.50€/piece, quantity: 3.0piece, total price: 7.50€",
    ]

    save_data(string_list)
    string_list2 = load_data()
    for i in range(len(string_list)):
        print(string_list[i] == string_list2[i])
