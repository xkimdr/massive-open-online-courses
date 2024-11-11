# Write your solution here

num = int(input("Please type in a number: "))

for i in range(num):
    for j in range(num):
        print(f"{(i + 1)} x {j + 1} = {(i + 1) * (j + 1)}")
