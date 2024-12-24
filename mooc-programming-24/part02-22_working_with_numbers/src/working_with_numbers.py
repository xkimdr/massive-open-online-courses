# Write your solution here

count = 0
sum = 0
positive = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish.")

while (number := int(input("Number: "))) != 0:
    count = count + 1
    sum = sum + number

    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
