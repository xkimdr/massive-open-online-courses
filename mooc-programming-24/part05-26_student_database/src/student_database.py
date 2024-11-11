# Write your solution here


def add_student(database: dict, name: str):
    student = {"name": name, "course": {}, "avg": 0}
    database[name] = student


def calculate_avg(database: dict, name: str):
    sum = 0
    count = 0
    for cname in database[name]["course"]:
        sum += database[name]["course"][cname]
        count += 1
    database[name]["avg"] = sum / count


def add_course(database: dict, name: str, course: tuple):
    if (
        course[1] == 0
        or course[0] in database[name]["course"]
        and course[1] < database[name]["course"][course[0]]
    ):
        return
    database[name]["course"][course[0]] = course[1]
    calculate_avg(database, name)


def print_student(database: dict, name: str):
    if name in database:
        print(f"{name}:")
        l = len(database[name]["course"])
        if l == 0:
            print(" no completed courses")
        else:
            print(f" {l} completed courses:")
            for ccname in database[name]["course"]:
                print(f"  {ccname} {database[name]["course"][ccname]}")
            print(f" average grade {database[name]["avg"]:.1f}")
    else:
        print(f"{name}: no such person in the database")


def summary(database: dict):
    l = len(database)
    print(f"students {l}")
    cname = ""
    cc = 0
    bname = ""
    ba = 0
    for student in database:
        if len(database[student]["course"]) > cc :
            cc = len(database[student]["course"])
            cname = student
        if database[student]["avg"] > ba:
            ba = database[student]["avg"]
            bname = student
    print(f"most courses completed {cc} {cname}")
    print(f"best average grade {ba:.1f} {bname}")



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
