# Write your solution here


def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        file.write(f"{person[0]};{person[1]};{person[2]:.1f}\n")


if __name__ == "__main__":
    store_personal_data(("Abc", 12, 34.4))
