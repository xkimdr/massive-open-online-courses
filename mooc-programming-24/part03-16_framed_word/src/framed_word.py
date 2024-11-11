# Write your solution here

word = input("Word: ")

length = len(word)

# top
print("*" * 30)

# middle
if length % 2 == 0:
    lpad = (28 - length) // 2
    rpad = lpad
else:
    lpad = (28 - length - 1) // 2
    rpad = lpad + 1

print("*" + " " * lpad + word + " " * rpad + "*")

# bottom
print("*" * 30)
