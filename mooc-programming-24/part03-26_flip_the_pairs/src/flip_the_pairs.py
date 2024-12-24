# Write your solution here

num = int(input("Please type in a number: "))

i = 1

while i <= num:
    if num % 2 != 0 and i == num:
        print(num)
        break

    print(i + 1)
    print(i)

    i = i + 2
