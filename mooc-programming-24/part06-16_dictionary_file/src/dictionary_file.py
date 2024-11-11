# Write your solution here

filename = "dictionary.txt"
dictionary = {}

with open(filename) as file:
    for line in file:
        parts = line.strip().split(";")
        dictionary[parts[0]] = parts[1]

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    cmd = int(input("Function: "))
    if cmd == 3:
        break
    elif cmd == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        dictionary[finnish] = english
        print("Dictionary entry added")
    elif cmd == 2:
        search = input("Search term: ")
        for finnish, english in dictionary.items():
            if search in finnish or search in english:
                print(f"{finnish} - {english}")


print("Bye!")

with open(filename, "w") as file:
    for finnish, english in dictionary.items():
        file.write(f"{finnish};{english}\n")
