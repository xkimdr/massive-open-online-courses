def balanced_brackets(my_string: str):
    array = [x for x in my_string if x in "()[]"]
    if len(array) == 0:
        return True
    if not (array[0] == "(" and array[-1] == ")") and not (
        array[0] == "[" and array[-1] == "]"
    ):
        return False
    # remove first and last character
    return balanced_brackets(array[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
