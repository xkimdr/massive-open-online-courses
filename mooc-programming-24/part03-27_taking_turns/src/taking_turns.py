# Write your solution here

num = int(input("Please type in a number: "))

i = 1

while i <= num - i + 1:
    if num % 2 != 0 and i == num - i + 1:
        print(i)
        break

    print(i)
    print(num - i + 1)

    i = i + 1
