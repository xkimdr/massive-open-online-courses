# Write your solution here

word = input("Please type in a string: ")

for i in range(len(word)):
    print(word[-1 * i - 1 :])
