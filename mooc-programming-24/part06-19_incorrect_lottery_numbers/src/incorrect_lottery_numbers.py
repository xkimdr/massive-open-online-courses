# Write your solution here


def filter_incorrect():
    correct = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            try:
                l = line.strip().split(";")
                int(l[0].split(" ")[1])
                wl = l[1].split(",")
                if len(wl) != 7:
                    raise
                dup = []
                for val in wl:
                    n = int(val)
                    if n not in range(1, 39):
                        raise
                    if n in dup:
                        raise
                    dup.append(n)
                correct.append(line)
            except:
                continue
    with open("correct_numbers.csv", "w") as file:
        for line in correct:
            file.write(line)


if __name__ == "__main__":
    filter_incorrect()
