# Write your solution here

num = 1

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break

    f = 1
    i = num
    while i != 1:
        f = f * i
        i = i - 1

    print(f"The factorial of the number {num} is {f}")

print("Thanks and bye!")
