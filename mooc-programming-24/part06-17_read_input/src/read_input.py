# Write your solution here


def read_input(string, s, e):
    while True:
        try:
            value = int(input(string))
        except ValueError:
            value = -1
        if s <= value <= e:
            return value
        print(f"You must type in an integer between {s} and {e}")


if __name__ == "__main__":
    number = read_input("Enter a number", 1, 5)
    print("You typed in:", number)
