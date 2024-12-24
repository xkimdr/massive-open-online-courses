# tee ratkaisu tänne
# Write your solution here

import math


def get_station_data(filename: str):
    database = {}
    with open(filename) as file:
        for line in file:
            if "Longitude" in line:
                continue
            parts = line.strip().split(";")
            database[parts[3]] = (float(parts[0]), float(parts[1]))
    return database


def distance(stations: dict, station1: str, station2: str):
    x = (stations[station1][0] - stations[station2][0]) * 55.26
    y = (stations[station1][1] - stations[station2][1]) * 111.2
    return math.sqrt(x**2 + y**2)


def greatest_distance(stations: dict):
    s1, s2, gd = "", "", 0
    for station1 in stations:
        for station2 in stations:
            d = distance(stations, station1, station2)
            if d > gd:
                s1, s2, gd = station1, station2, d
    return s1, s2, gd


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data("stations1.csv")
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
