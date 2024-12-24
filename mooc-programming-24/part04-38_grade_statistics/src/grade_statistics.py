# Write your solution here


def parse(str):
    data = []
    values = str.split(" ")
    for v in values:
        data.append(int(v))
    return data


def collect_data():
    data = []
    while True:
        str = input("Exam points and exercises completed: ")
        if len(str) == 0:
            break
        data.append(parse(str))
    return data


def grades(data):
    gl = []
    for p in data:
        tp = p[0] + p[1] // 10
        if p[0] < 10:
            gl.append(0)
        elif 28 <= tp:
            gl.append(5)
        elif 24 <= tp:
            gl.append(4)
        elif 21 <= tp:
            gl.append(3)
        elif 18 <= tp:
            gl.append(2)
        elif 15 <= tp:
            gl.append(1)
        elif 0 <= tp:
            gl.append(0)
    return gl


def grades_dst(gl):
    gd = [0, 0, 0, 0, 0, 0]
    for g in gl:
        gd[g] += 1
    return gd


def avg_points(data):
    sum = 0
    for v in data:
        sum += v[0] + v[1] // 10
    return sum / len(data)


def pass_per(gl):
    sum = 0
    for g in gl:
        if g != 0:
            sum += 1
    return sum / len(gl) * 100


def main():
    data = collect_data()
    print("Statistics:")
    print(f"Points average: {avg_points(data):.1f}")
    gl = grades(data)
    print(f"Pass percentage: {pass_per(gl):.1f}")
    print("Grade distribution:")
    gd = grades_dst(gl)
    for i in range(5, -1, -1):
        print(f"{i:3}: {"*" * gd[i]}")

main()
