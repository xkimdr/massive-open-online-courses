# Write your solution here
# If you use the classes made in the previous exercise, copy them here


class Task:
    __id = 0

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        Task.__id += 1
        self.__id = Task.__id
        self.__finished = False

    @property
    def description(self):
        return self.__description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload

    @property
    def id(self):
        return self.__id

    def is_finished(self):
        return self.__finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self) -> str:
        return f"{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {"FINISHED" if self.__finished else "NOT FINISHED"}"


class OrderBook:
    def __init__(self) -> None:
        self.__orders = []

    def add_order(self, description, programmer, workload):
        self.__orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return list(set(task.programmer for task in self.__orders))

    def mark_finished(self, id: int):
        for task in self.__orders:
            if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [task for task in self.__orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.__orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        no_of_finished_task = 0
        no_of_unfinished_task = 0
        total_workload_of_finished_task = 0
        total_workload_of_unfinished_task = 0
        found = False
        for task in self.__orders:
            if task.programmer == programmer:
                found = True
                if task.is_finished():
                    no_of_finished_task += 1
                    total_workload_of_finished_task += task.workload
                else:
                    no_of_unfinished_task += 1
                    total_workload_of_unfinished_task += task.workload
        if not found:
            raise ValueError
        return (
            no_of_finished_task,
            no_of_unfinished_task,
            total_workload_of_finished_task,
            total_workload_of_unfinished_task,
        )


class UI:
    def __init__(self) -> None:
        self.__orders = OrderBook()

    def start(self):
        self.__help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.__add_orders()
            elif command == "2":
                self.__finished_orders()
            elif command == "3":
                self.__unfinished_orders()
            elif command == "4":
                self.__mark_finished()
            elif command == "5":
                self.__programmers()
            elif command == "6":
                self.__status()
            else:
                self.__help()

    def __help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def __add_orders(self):
        description = input("description: ")
        parts = input("programmer and workload estimate: ").split()
        programmer = parts[0]
        try:
            workload = int(parts[1])
        except:
            print("erroneous input")
            return
        self.__orders.add_order(description, programmer, workload)
        print("added!")

    def __finished_orders(self):
        tasks = self.__orders.finished_orders()
        if len(tasks) == 0:
            print("no finished tasks")
        else:
            for task in tasks:
                print(task)

    def __unfinished_orders(self):
        tasks = self.__orders.unfinished_orders()
        if len(tasks) == 0:
            print("no unfinished tasks")
        else:
            for task in tasks:
                print(task)

    def __mark_finished(self):
        try:
            id = int(input("id: "))
            self.__orders.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")

    def __programmers(self):
        for programmer in self.__orders.programmers():
            print(programmer)

    def __status(self):
        programmer = input("programmer")
        try:
            stats = self.__orders.status_of_programmer(programmer)
        except:
            print("erroneous input")
            return
        print(
            f"tasks: finished {stats[0]} not finished {stats[1]}, hours: done {stats[2]} scheduled {stats[3]}"
        )


ui = UI()
ui.start()
