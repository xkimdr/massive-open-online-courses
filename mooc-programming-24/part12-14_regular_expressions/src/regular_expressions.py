# Write your solution here
import re


def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) != None


def all_vowels(my_string: str):
    return re.search("^[aeiou]+$", my_string) != None


def time_of_day(my_string: str):
    return (
        re.search("24:00:00|((2[0-3]|[0-1][0-9])(:[0-5][0-9]){2})", my_string) != None
    )


if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
