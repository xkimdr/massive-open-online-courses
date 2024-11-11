# Write your solution here

str = input("Please type in a string: ")

if len(str) <= 20:
    print(f"{"*" * (20 - len(str))}{str}")
