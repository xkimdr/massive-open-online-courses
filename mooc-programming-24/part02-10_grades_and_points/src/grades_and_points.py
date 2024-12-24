# Write your solution here

points = int(input("How many points [0-100]: "))

if points > 100:
    print("Grade: impossible!")
elif points >= 90:
    print("Grade: 5")
elif points >= 80:
    print("Grade: 4")
elif points >= 70:
    print("Grade: 3")
elif points >= 60:
    print("Grade: 2")
elif points >= 50:
    print("Grade: 1")
elif points >= 0:
    print("Grade: fail")
else:
    print("Grade: impossible!")
