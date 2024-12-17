# Write your solution to exercise 2 here

from functools import reduce


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


class ShoppingList:
    def __init__(self) -> None:
        self.__products = {}

    def add_product(self, product: tuple) -> None:
        name = product[0]
        unitprice = product[1]
        unit = product[2]
        quantity = product[3]
        if name in self.__products:
            x: Product = self.__products[name]
            quantity += x.quantity
            if x.unitprice > unitprice:
                unitprice = x.unitprice
        self.__products[name] = Product(name, unitprice, unit, quantity)

    def return_product(self, name: str) -> str:
        if name not in self.__products:
            raise ValueError("Product is not found.")
        return f"{self.__products[name]}"

    def remove_product(self, name: str, quantity: float = 0) -> None:
        if name not in self.__products:
            raise ValueError("Product is not found.")
        x: Product = self.__products[name]
        if quantity == 0 or x.quantity <= quantity:
            self.__products.pop(name)
        else:
            self.__products[name] = Product(
                x.name, x.unitprice, x.unit, x.quantity - quantity
            )

    def change_product_unit_price(self, name: str, unitprice: float) -> None:
        if name not in self.__products:
            raise ValueError("Product is not found.")
        x: Product = self.__products[name]
        self.__products[name] = Product(x.name, unitprice, x.unit, x.quantity)

    def return_all_products(self) -> list:
        return [f"{x}" for x in self.__products.values()]

    def return_total_price_of_shopping_list(self) -> float:
        return reduce(lambda sum, x: sum + x.total_price, self.__products.values(), 0)


if __name__ == "__main__":
    apple = ("apple", 1.60, "kg", 2.2)  # 2.2 kg of apples
    potato = ("potato", 1.30, "kg", 5.0)  # 5 kg of potatoes
    banana = ("banana", 0.95, "kg", 1.2)  # 1.2 kg of bananas
    milk = ("milk", 1.25, "l", 2.0)  # 2 liters of milk
    bread = ("sourdough bread", 2.50, "piece", 3.0)  # 3 pieces of bread

    shopping_list = ShoppingList()

    shopping_list.add_product(apple)
    shopping_list.add_product(potato)
    shopping_list.add_product(banana)
    shopping_list.add_product(milk)
    shopping_list.add_product(bread)

    print("Product information at the beginning:")
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    # Check the information of the product "apple" in the shopping list
    print()
    print("The information for product apple:")
    print(shopping_list.return_product("apple"))

    # Notice that inflation has raised the price of bread
    shopping_list.change_product_unit_price("sourdough bread", 4.00)

    # There's a promotion at the store, and apples are on sale
    shopping_list.change_product_unit_price("apple", 1)

    print()
    print("After the changes:")
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    print()
    print("Removing 2 loaves of bread, all bananas, and more milk than available:")
    shopping_list.remove_product("sourdough bread", 2)
    shopping_list.remove_product("banana")
    shopping_list.remove_product("milk", 3)
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    print(
        "Total price of the shopping list:",
        shopping_list.return_total_price_of_shopping_list(),
    )
