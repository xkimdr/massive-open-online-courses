# Write your solution here

upto = int(input("Limit: "))

sum = 0
i = 1

s = "The consecutive sum: "
while sum < upto:

    if sum == 0:
        s += f"{i}"
    else:
        s += f" + {i}"

    sum += i
    i += 1

print(f"{s} = {sum}")
