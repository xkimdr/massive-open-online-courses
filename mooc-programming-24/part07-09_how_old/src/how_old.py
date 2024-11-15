# Write your solution here

from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthday = datetime(year, month, day)
eve = datetime(1999, 12, 31)

if birthday > eve:
    print("You weren't born yet on the eve of the new millennium.")
else:
    diff = eve - birthday
    print(f"You were {diff.days} days old on the eve of the new millennium.")
