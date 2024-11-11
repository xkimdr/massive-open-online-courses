# Write your solution here


def filter_solutions():
    correct = []
    incorrect = []

    with open("solutions.csv") as file:
        for line in file:
            parts = line.strip().split(";")
            if "+" in parts[1]:
                args = parts[1].split("+")
                sum = int(args[0]) + int(args[1])
                if sum == int(parts[-1]):
                    correct.append(line)
                else:
                    incorrect.append(line)
            elif "-" in parts[1]:
                args = parts[1].split("-")
                sum = int(args[0]) - int(args[1])
                if sum == int(parts[-1]):
                    correct.append(line)
                else:
                    incorrect.append(line)

    with open("correct.csv", "w") as file:
        for content in correct:
            file.write(content)

    with open("incorrect.csv", "w") as file:
        for content in incorrect:
            file.write(content)


if __name__ == "__main__":
    filter_solutions()
