# Write your solution here

entries = []

with open("diary.txt") as file:
    for line in file:
        entries.append(line.strip())

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    cmd = int(input("Function: "))

    if cmd == 0:
        print("Bye now!")
        break
    elif cmd == 1:
        entries.append(input("Diary entry: "))
        print("Diary saved")
    elif cmd == 2:
        for entry in entries:
            print(entry)

with open("diary.txt", "w") as file:
    for entry in entries:
        file.write(entry + "\n")
