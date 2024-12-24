# WRITE YOUR SOLUTION HERE:


class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations = []

    def add_observation(self, observation: str) -> None:
        self.__observations.append(observation)

    def latest_observation(self) -> str:
        if len(self.__observations) == 0:
            return ""
        return self.__observations[-1]

    def number_of_observations(self) -> int:
        return len(self.__observations)

    def __str__(self) -> str:
        return f"{self.__name}, {self.number_of_observations()} observations"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
