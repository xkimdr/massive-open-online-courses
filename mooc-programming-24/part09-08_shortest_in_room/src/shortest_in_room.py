# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self) -> None:
        self.room = []

    def add(self, person: Person):
        self.room.append(person)

    def is_empty(self):
        return len(self.room) == 0

    def print_contents(self):
        height = 0
        output = []
        for person in self.room:
            output.append(f"{person.name} ({person.height} cm)")
            height += person.height
        print(
            f"There are {len(self.room)} persons in the room, and their combined height is {height} cm"
        )
        print("\n".join(output))

    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.room[0]
        for person in self.room:
            if shortest.height > person.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        shortest = self.shortest()
        if shortest == None:
            return None
        self.room.remove(shortest)
        return shortest


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
