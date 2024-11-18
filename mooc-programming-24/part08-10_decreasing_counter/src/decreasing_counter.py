# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.inital_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1
        if self.value == -1:
            self.value = 0

    # Write the rest of the methods here!
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.inital_value


if __name__ == "__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
