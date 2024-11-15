# Write your solution here

import csv
from datetime import timedelta, datetime


def cheaters():
    records = {}
    with open("start_times.csv") as file1:
        for line in csv.reader(file1, delimiter=";"):
            records[line[0]] = {
                "start_time": datetime.strptime(line[1], "%H:%M"),
                "tasks": [],
                "points": [],
                "end_time": [],
            }
    with open("submissions.csv") as file2:
        for line in csv.reader(file2, delimiter=";"):
            records[line[0]]["tasks"].append(int(line[1]))
            records[line[0]]["points"].append(int(line[2]))
            records[line[0]]["end_time"].append(datetime.strptime(line[3], "%H:%M"))
    cheated = []
    for name in records:
        for time in records[name]["end_time"]:
            if time - records[name]["start_time"] > timedelta(hours=3):
                cheated.append(name)
                break
    return cheated


if __name__ == "__main__":
    print(cheaters())
