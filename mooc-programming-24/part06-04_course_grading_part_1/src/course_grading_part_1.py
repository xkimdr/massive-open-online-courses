# write your solution here

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

database = {}

with open(student_file) as f1:
    for line in f1:
        dict = {}
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        dict["fname"] = parts[1]
        dict["lname"] = parts[2]
        dict["exercise"] = []
        database[parts[0]] = dict

with open(exercise_file) as f2:
    for line in f2:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        list = parts[1:]
        for x in list:
            database[parts[0]]["exercise"].append(int(x))

for data in database:
    print(f"{database[data]["fname"]} {database[data]["lname"]} {sum(database[data]["exercise"])}")
