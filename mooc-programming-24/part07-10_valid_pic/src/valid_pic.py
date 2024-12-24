# Write your solution here
from datetime import datetime


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    if pic[6] not in "+-A":
        return False
    yy = 1800
    if pic[6] == "-":
        yy = 1900
    elif pic[6] == "A":
        yy = 2000
    try:
        datetime(int(pic[4:6]) + yy, int(pic[2:4]), int(pic[:2]))
        yyy = int(pic[7:10])
    except:
        return False
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    index = int(pic[:6] + pic[7:10]) % 31
    if string[index] != pic[-1]:
        return False
    return True


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
