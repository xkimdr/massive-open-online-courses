# tee ratkaisu tänne


sfile = input("Student information: ")
efile = input("Exercises completed: ")
epfile = input("Exam points: ")
cfile = input("Course information: ")

rtfile = "results.txt"
rcfile = "results.csv"

db = {}

with open(sfile) as file:
    for line in file:
        if "id" in line:
            continue
        parts = line.strip().split(";")
        id = int(parts[0])
        dict = {"name": f"{parts[1]} {parts[2]}"}
        db[id] = dict

with open(efile) as file:
    for line in file:
        if "id" in line:
            continue
        parts = line.strip().split(";")
        id = int(parts[0])
        sum = 0
        for x in parts[1:]:
            sum += int(x)
        db[id]["exec_nbr"] = sum
        db[id]["exec_pts"] = (sum * 10) // 40

with open(epfile) as file:
    for line in file:
        if "id" in line:
            continue
        parts = line.strip().split(";")
        id = int(parts[0])
        sum = 0
        for x in parts[1:]:
            sum += int(x)
        db[id]["exm_pts"] = sum
        db[id]["tot_pts"] = db[id]["exec_pts"] + db[id]["exm_pts"]
        if 28 <= db[id]["tot_pts"]:
            db[id]["grade"] = 5
        elif 24 <= db[id]["tot_pts"] <= 27:
            db[id]["grade"] = 4
        elif 21 <= db[id]["tot_pts"] <= 23:
            db[id]["grade"] = 3
        elif 18 <= db[id]["tot_pts"] <= 20:
            db[id]["grade"] = 2
        elif 15 <= db[id]["tot_pts"] <= 17:
            db[id]["grade"] = 1
        else:
            db[id]["grade"] = 0

name = ""
credits = 0

with open(cfile) as file:
    for line in file:
        if "name" in line:
            name = line.strip().split(": ")[1].strip()
        elif "credits" in line:
            credits = int(line.strip().split(": ")[1].strip())


with open(rtfile, "w") as file:
    l1 = f"{name}, {credits} credits"
    file.write(f"{l1}\n")
    file.write(f"{len(l1) * "="}\n")
    file.write(f"{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}\n")
    for id in db:
        file.write(f"{db[id]["name"]:<30}{db[id]["exec_nbr"]:<10}{db[id]["exec_pts"]:<10}{db[id]["exm_pts"]:<10}{db[id]["tot_pts"]:<10}{db[id]["grade"]:<10}\n")
     

with open(rcfile, "w") as file:
    for id in db:
        file.write(f"{id};{db[id]["name"]};{db[id]["grade"]}\n")

print(f"Results written to files {rtfile} and {rcfile}")
