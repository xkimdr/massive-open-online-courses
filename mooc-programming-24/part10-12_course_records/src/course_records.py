# tee ratkaisusi tänne


class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def __str__(self) -> str:
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits


class Records:
    def __init__(self) -> None:
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name in self.__courses:
            course = self.__courses[name]
            course_grade = course.grade()
            if course_grade > grade:
                grade = course_grade
        self.__courses[name] = Course(name, grade, credits)

    def print_course_info(self, name: str):
        if name in self.__courses:
            print(self.__courses[name])
        else:
            print("no entry for this course")

    def stats(self):
        no_of_courses = len(self.__courses)
        total_credits = 0
        grade_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for course in self.__courses.values():
            total_credits += course.credits()
            grade = course.grade()
            grade_distribution[grade] += 1
        array = sorted(grade_distribution.items(), reverse=True)
        sum = 0
        for val in array:
            if val[1] == 0:
                continue
            sum += val[0] * val[1]
        print(f"{no_of_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {(sum / no_of_courses):.1f}")
        print(f"grade distribution")
        for val in array:
            print(f"{val[0]}: {"x"*val[1]}")


class UI:
    def __init__(self) -> None:
        self.__records = Records()

    def start(self):
        self.__menu()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.__add_course()
            elif command == 2:
                self.__get_course_data()
            elif command == 3:
                self.__stats()
            else:
                self.__menu()

    def __menu(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def __add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__records.add_course(name, grade, credits)

    def __get_course_data(self):
        name = input("course: ")
        self.__records.print_course_info(name)

    def __stats(self):
        self.__records.stats()


UI().start()
