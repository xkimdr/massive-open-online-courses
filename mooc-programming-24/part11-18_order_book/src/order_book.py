# Write your solution here:


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


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
