# Write your solution here

import json


class Player:
    def __init__(
        self,
        name: str,
        nationality: str,
        assists: int,
        goals: int,
        penalties: int,
        team: int,
        games: int,
    ):
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games

    @property
    def name(self):
        return self.__name

    @property
    def nationality(self):
        return self.__nationality

    @property
    def assists(self):
        return self.__assists

    @property
    def goals(self):
        return self.__goals

    @property
    def penalties(self):
        return self.__penalties

    @property
    def team(self):
        return self.__team

    @property
    def games(self):
        return self.__games

    def __str__(self):
        return f"{self.__name:20} {self.__team:4} {self.__goals:>2} + {self.__assists:>2} = {(self.__goals + self.__assists):>3}"


class Statistics:
    def __init__(self):
        self.__data = []

    def load_data_from_json(self, file_name: str):
        with open(file_name) as file:
            data = file.read()
        for x in json.loads(data):
            self.__data.append(
                Player(
                    x["name"],
                    x["nationality"],
                    x["assists"],
                    x["goals"],
                    x["penalties"],
                    x["team"],
                    x["games"],
                )
            )
        return f"read the data of {len(self.__data)} players"

    def search(self, name: str):
        for p in self.__data:
            if p.name == name:
                return f"{p}"
        else:
            raise ValueError

    def teams(self):
        return sorted(set(map(lambda x: x.team, self.__data)))

    def countries(self):
        return sorted(set(map(lambda x: x.nationality, self.__data)))

    def players_in_team(self, team: str):
        return map(
            lambda x: f"{x}",
            sorted(
                filter(lambda x: x.team == team, self.__data),
                key=lambda x: x.goals + x.assists,
                reverse=True,
            ),
        )

    def players_from_country(self, country: str):
        return map(
            lambda x: f"{x}",
            sorted(
                filter(lambda x: x.nationality == country, self.__data),
                key=lambda x: x.goals + x.assists,
                reverse=True,
            ),
        )

    def most_points(self, n: int):
        return map(
            lambda x: f"{x}",
            sorted(
                self.__data,
                key=lambda x: (x.goals + x.assists, x.goals),
                reverse=True,
            )[0:n],
        )

    def most_goals(self, n: int):
        return map(
            lambda x: f"{x}",
            sorted(
                self.__data,
                key=lambda x: (x.goals, -x.games),
                reverse=True,
            )[0:n],
        )


class UI:
    def __init__(self):
        self.__stats = Statistics()

    def start(self):
        self.__populate()
        print()
        self.__help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.__search()
            elif command == "2":
                self.__teams()
            elif command == "3":
                self.__countries()
            elif command == "4":
                self.__players_in_team()
            elif command == "5":
                self.__players_from_country()
            elif command == "6":
                self.__most_points()
            elif command == "7":
                self.__most_goals()
            else:
                self.__help()

    def __help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def __populate(self):
        file_name = input("file name: ")
        status = self.__stats.load_data_from_json(file_name)
        print(status)

    def __search(self):
        name = input("name: ")
        record = self.__stats.search(name)
        print(record)

    def __teams(self):
        for team in self.__stats.teams():
            print(team)

    def __countries(self):
        for country in self.__stats.countries():
            print(country)

    def __players_in_team(self):
        team = input("team: ")
        for player in self.__stats.players_in_team(team):
            print(player)

    def __players_from_country(self):
        team = input("country: ")
        for player in self.__stats.players_from_country(team):
            print(player)

    def __most_points(self):
        n = int(input("how many: "))
        for player in self.__stats.most_points(n):
            print(player)

    def __most_goals(self):
        n = int(input("how many: "))
        for player in self.__stats.most_goals(n):
            print(player)


UI().start()
