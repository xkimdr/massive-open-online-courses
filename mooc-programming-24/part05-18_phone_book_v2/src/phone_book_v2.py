# Write your solution here


def getCmd():
    return int(input("command (1 search, 2 add, 3 quit): "))


def search(phonebook):
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")


def add(phonebook):
    name = input("name: ")
    number = input("number: ")
    if not name in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)
    print("ok!")


def main():
    phonebook = {}
    while True:
        cmd = getCmd()
        if cmd == 1:
            search(phonebook)
        elif cmd == 2:
            add(phonebook)
        elif cmd == 3:
            print("quitting...")
            break


main()
