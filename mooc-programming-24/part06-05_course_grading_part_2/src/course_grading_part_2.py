# wwite your solution here

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

database = {}

with open(student_file) as f1:
    for line in f1:
        dict = {}
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        dict = {
            "name": f"{parts[1]} {parts[2]}",
            "exec_nbr": 0,
            "exec_pts": 0,
            "exm_pts": 0,
            "tot_pts": 0,
            "grade": 0,
        }
        database[parts[0]] = dict

with open(exercise_file) as f2:
    for line in f2:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        list = parts[1:]
        sum = 0
        for x in list:
            sum += int(x)
        database[parts[0]]["exec_nbr"] = sum
        database[parts[0]]["exec_pts"] = (sum * 10) // 40

with open(exam_file) as f3:
    for line in f3:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        list = parts[1:]
        sum = 0
        for x in list:
            sum += int(x)
        database[parts[0]]["exm_pts"] = sum


for data in database:
    database[data]["tot_pts"] = database[data]["exec_pts"] + database[data]["exm_pts"]

    if 28 <= database[data]["tot_pts"]:
        database[data]["grade"] = 5
    elif 24 <= database[data]["tot_pts"] <= 27:
        database[data]["grade"] = 4
    elif 21 <= database[data]["tot_pts"] <= 23:
        database[data]["grade"] = 3
    elif 18 <= database[data]["tot_pts"] <= 20:
        database[data]["grade"] = 2
    elif 15 <= database[data]["tot_pts"] <= 17:
        database[data]["grade"] = 1
    elif 0 <= database[data]["tot_pts"] <= 14:
        database[data]["grade"] = 0


for data in database:
    print(f"{database[data]["name"]} {database[data]["grade"]}")
