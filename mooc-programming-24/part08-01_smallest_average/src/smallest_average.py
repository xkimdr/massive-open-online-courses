# Write your solution here


def avg(dict: dict):
    return (dict["result1"] + dict["result2"] + dict["result3"]) / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = avg(person1)
    avg2 = avg(person2)
    avg3 = avg(person3)
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg3 and avg2 < avg1:
        return person2
    else:
        return person3


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
