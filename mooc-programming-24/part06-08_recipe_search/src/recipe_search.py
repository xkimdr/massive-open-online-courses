# Write your solution here


def parser(filename: str):
    database = {}
    list = []
    with open(filename) as file:
        for line in file:
            if len(line.strip()) != 0:
                list.append(line.strip())
            else:
                dict = {}
                dict["time"] = int(list[1])
                dict["ingredient"] = list[2:]
                database[list[0]] = dict
                list.clear()
        if len(list) != 0:
            dict = {}
            dict["time"] = int(list[1])
            dict["ingredient"] = list[2:]
            database[list[0]] = dict
            list.clear()
    return database


def search_by_name(filename: str, word: str):
    database = parser(filename)
    list = []
    for recipe in database:
        if word in recipe.lower():
            list.append(recipe)
    return list


def search_by_time(filename: str, prep_time: int):
    database = parser(filename)
    list = []
    for recipe in database:
        if database[recipe]["time"] <= prep_time:
            list.append(f"{recipe}, preparation time {database[recipe]["time"]} min")
    return list


def search_by_ingredient(filename: str, ingredient: str):
    database = parser(filename)
    list = []
    for recipe in database:
        if ingredient in database[recipe]["ingredient"]:
            list.append(f"{recipe}, preparation time {database[recipe]["time"]} min")
    return list



if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
    
    print()

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)
    
    print()

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
