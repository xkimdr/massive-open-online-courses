# Write your solution here

from datetime import datetime, timedelta

filename = input("Filename: ")
dateArray = input("Starting date: ").split(".")
no_of_days = int(input("How many days: "))

odate = datetime(int(dateArray[2]), int(dateArray[1]), int(dateArray[0]))
date = odate
one_day = timedelta(days=1)

print("Please type in screen time in minutes on each day (TV computer mobile):")

values = []
for i in range(no_of_days):
    ds = input(f"Screen time {date.strftime("%d.%m.%Y")}: ")
    values.append(ds)
    date = date + one_day

date = date - one_day

with open(filename, "w") as file:
    file.write(
        f"Time period: {odate.strftime("%d.%m.%Y")}-{date.strftime("%d.%m.%Y")}\n"
    )
    total_time = 0
    avg_time = 0
    schedule = []
    date = odate
    for string in values:
        parts = string.split(" ")
        total_time += int(parts[0]) + int(parts[1]) + int(parts[2])
        schedule.append(f"{date.strftime("%d.%m.%Y")}: {"/".join(parts)}")
        date = date + one_day
    file.write(f"Total minutes: {total_time}\n")
    file.write(f"Average minutes: {total_time / no_of_days}\n")
    for sch in schedule:
        file.write(f"{sch}\n")

print(f"Data stored in file {filename}")
