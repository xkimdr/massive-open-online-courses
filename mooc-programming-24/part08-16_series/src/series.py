# Write your solution here:


class Series:
    def __init__(self, title: str, no_of_seasons: int, genres: list) -> None:
        self.title = title
        self.no_of_seasons = no_of_seasons
        self.genres = genres
        self.ratings = []

    def __str__(self) -> str:
        rating_str = "no ratings"
        if len(self.ratings) > 0:
            rating_str = f"{len(self.ratings)} ratings, average {(sum(self.ratings) / len(self.ratings)):.1f} points"
        list = [
            f"{self.title} ({self.no_of_seasons} seasons)",
            f"genres: {", ".join(self.genres)}",
            rating_str,
        ]
        return "\n".join(list)

    def rate(self, rating: int):
        self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list):
    ll = []
    for series in series_list:
        if rating <= (sum(series.ratings) / len(series.ratings)):
            ll.append(series)
    return ll


def includes_genre(genre: str, series_list: list):
    ll = []
    for series in series_list:
        if genre in series.genres:
            ll.append(series)
    return ll


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
