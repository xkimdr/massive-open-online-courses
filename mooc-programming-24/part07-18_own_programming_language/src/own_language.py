# Write your solution here

from string import ascii_uppercase


def initalize_variables():
    variables = {}
    for x in ascii_uppercase:
        variables[x] = 0
    return variables


def mov(command: str, variables: dict):
    parts = command.split()
    variables[parts[1]] = (
        variables[parts[2]] if parts[2] in ascii_uppercase else int(parts[2])
    )


def add(command: str, variables: dict):
    parts = command.split()
    variables[parts[1]] += (
        variables[parts[2]] if parts[2] in ascii_uppercase else int(parts[2])
    )


def sub(command: str, variables: dict):
    parts = command.split()
    variables[parts[1]] -= (
        variables[parts[2]] if parts[2] in ascii_uppercase else int(parts[2])
    )


def mul(command: str, variables: dict):
    parts = command.split()
    variables[parts[1]] *= (
        variables[parts[2]] if parts[2] in ascii_uppercase else int(parts[2])
    )


def prnt(command: str, variables: dict, output: list):
    x = command[-1]
    output.append(variables[x] if x in ascii_uppercase else int(x))


def jump(command: str, program: list):
    location = command.split()[1]
    return program.index(f"{location}:")


def check(parts: list, variables: dict):
    x = variables[parts[0]] if parts[0] in ascii_uppercase else int(parts[0])
    y = variables[parts[2]] if parts[2] in ascii_uppercase else int(parts[2])
    if parts[1] == "==":
        return x == y
    elif parts[1] == "!=":
        return x != y
    elif parts[1] == ">":
        return x > y
    elif parts[1] == "<":
        return x < y
    elif parts[1] == "<=":
        return x <= y
    elif parts[1] == ">=":
        return x >= y
    else:
        return False


def run(program: list):
    output = []
    variables = initalize_variables()
    index = 0
    command: str = ""
    while index < len(program) and command != "END":
        command = program[index]
        if command == "END":
            break
        elif command.startswith("PRINT"):
            prnt(command, variables, output)
        elif command.startswith("MOV"):
            mov(command, variables)
        elif command.startswith("ADD"):
            add(command, variables)
        elif command.startswith("SUB"):
            sub(command, variables)
        elif command.startswith("MUL"):
            mul(command, variables)
        elif command.startswith("JUMP"):
            index = jump(command, program)
            continue
        elif command.startswith("IF"):
            parts = command.split()
            i = parts.index("JUMP")
            if check(parts[1:i], variables):
                command = " ".join(parts[i:])
                index = jump(command, program)
                continue
        index += 1
    return output


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
