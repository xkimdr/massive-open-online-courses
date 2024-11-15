# Write your solution here

import csv
from datetime import datetime, timedelta


def final_points():
    records = {}
    with open("start_times.csv") as file1:
        for line in csv.reader(file1, delimiter=";"):
            records[line[0]] = {
                "start_time": datetime.strptime(line[1], "%H:%M"),
                "tasks": [],
                "points": [],
                "end_time": [],
                "final_points": {},
            }
    with open("submissions.csv") as file2:
        for line in csv.reader(file2, delimiter=";"):
            name = line[0]
            tasks = int(line[1])
            points = int(line[2])
            time = datetime.strptime(line[3], "%H:%M")
            if time - records[name]["start_time"] > timedelta(hours=3):
                continue
            records[name]["tasks"].append(tasks)
            records[name]["points"].append(points)
            records[name]["end_time"].append(time)
            if (
                records[name]["final_points"].get(tasks) is None
                or records[name]["final_points"][tasks] < points
            ):
                records[name]["final_points"][tasks] = points
    data = {}
    for name in records:
        sum = 0
        for _, val in records[name]["final_points"].items():
            sum += val
        data[name] = sum
    return data


if __name__ == "__main__":
    print(final_points())
