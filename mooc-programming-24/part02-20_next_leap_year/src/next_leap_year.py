# Write your solution here

y = int(input("Year: "))
ly = y

if ly % 4 == 0 and ly % 100 != 0 or ly % 400 == 0:
    ly = ly + 1

while not (ly % 4 == 0 and ly % 100 != 0 or ly % 400 == 0):
    ly = ly + 1


print(f"The next leap year after {y} is {ly}")
