# Write your solution here


class Checklist:
    def __init__(self, header: str, entries: list) -> None:
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int) -> None:
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(
        self, model: str, length: float, max_speed: int, bidirectional: bool
    ) -> None:
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


if __name__ == "__main__":
    pass
