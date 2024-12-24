# Write your solution here

from string import ascii_letters, whitespace, digits


def change_case(orig_string: str):
    letters = []
    for x in orig_string:
        if x.islower():
            letters.append(x.upper())
        else:
            letters.append(x.lower())
    return "".join(letters)


def split_in_half(orig_string: str):
    mid = len(orig_string) // 2
    return (orig_string[0:mid], orig_string[mid:])


def remove_special_characters(orig_string: str):
    letters = []
    array = ascii_letters + whitespace + digits
    for x in orig_string:
        if x in array:
            letters.append(x)
    return "".join(letters)


if __name__ == "__main__":
    print(change_case("abFc"))
    print(split_in_half("abcdefg"))
    print(remove_special_characters("asddas^dssa*$sdad"))
