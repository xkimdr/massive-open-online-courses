# Write your solution here

import urllib.request
import json


def retrieve_all():
    request = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    )
    records = json.loads(request.read())
    data = []
    for record in records:
        if record["enabled"]:
            tp = (
                record["fullName"],
                record["name"],
                record["year"],
                sum(record["exercises"]),
            )
            data.append(tp)
    return data


def retrieve_course(course_name: str):
    request = urllib.request.urlopen(
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    records = json.loads(request.read())
    weeks = len(records)
    students = []
    hours = 0
    exercises = 0
    for record in records:
        students.append(records[record]["students"])
        hours += records[record]["hour_total"]
        exercises += records[record]["exercise_total"]

    students = max(students)

    data = {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours // students,
        "exercises": exercises,
        "exercises_average": exercises // students,
    }
    return data


if __name__ == "__main__":
    # print(retrieve_all())
    print(retrieve_course("docker2019"))
