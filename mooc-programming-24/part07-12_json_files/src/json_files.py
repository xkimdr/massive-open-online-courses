# Write your solution here

import json


def parse(filename: str):
    with open(filename) as file:
        return json.loads(file.read())


def print_persons(filename: str):
    data = parse(filename)
    for record in data:
        string = f"{record["name"]} {record["age"]} years ("
        for hobbies in record["hobbies"]:
            string = f"{string}{hobbies}, "
        if len(record["hobbies"]) == 0:
            string = string + ")"
        else:
            string = string[:-2] + ")"
        print(string)


if __name__ == "__main__":
    print_persons("file1.json")
