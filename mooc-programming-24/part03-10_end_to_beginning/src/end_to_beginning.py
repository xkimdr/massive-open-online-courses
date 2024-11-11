# Write your solution here

str = input("Please type in a string: ")

length = len(str)

while length != 0:
    print(str[(length - 1)])
    length -= 1
