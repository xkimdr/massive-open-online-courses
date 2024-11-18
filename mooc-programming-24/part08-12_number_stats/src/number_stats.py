# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        try:
            return self.get_sum() / self.count_numbers()
        except:
            return 0


def main():
    stats = NumberStats()
    odd = NumberStats()
    even = NumberStats()
    print("Please type in integer numbers:")
    while True:
        num = int(input())
        if num == -1:
            break
        stats.add_number(num)
        if num % 2 == 0:
            even.add_number(num)
        else:
            odd.add_number(num)
    print(f"Sum of numbers: {stats.get_sum()}")
    print(f"Mean of numbers: {stats.average()}")
    print(f"Sum of even numbers: {even.get_sum()}")
    print(f"Sum of odd numbers: {odd.get_sum()}")


main()
